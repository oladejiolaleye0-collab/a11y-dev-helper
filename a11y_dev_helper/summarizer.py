from __future__ import annotations

from pathlib import Path
from typing import Optional

from .models import BaseLLMClient
from .parser import ModuleStructure, parse_python_file


def _structure_to_prompt(structure: ModuleStructure) -> str:
    """
    Convert parsed structure into a plain-text prompt for the LLM.

    The prompt is designed for generating descriptions that are easy
    to read with a screen reader.
    """
    lines: list[str] = []

    lines.append("You are helping a blind software developer understand a code file.")
    lines.append("Describe the structure of the file in simple, concise language.")
    lines.append("Avoid visual terms like 'see above' or 'on the left'.")
    lines.append("Use short paragraphs and numbered lists when helpful.")
    lines.append("Do not include code blocks; use plain text only.")
    lines.append("")

    lines.append(f"File path: {structure.path}")

    if structure.module_docstring:
        lines.append("Module docstring:")
        lines.append(structure.module_docstring)
        lines.append("")

    if structure.functions:
        lines.append(f"There are {len(structure.functions)} top-level functions:")
        for fn in structure.functions:
            lines.append(f"- Function '{fn.name}' starting around line {fn.lineno}.")
            if fn.docstring:
                lines.append(f"  Short description: {fn.docstring[:200]}")
        lines.append("")

    if structure.classes:
        lines.append(f"There are {len(structure.classes)} classes:")
        for cls in structure.classes:
            lines.append(f"- Class '{cls.name}' starting around line {cls.lineno}.")
            if cls.docstring:
                lines.append(f"  Short description: {cls.docstring[:200]}")
            if cls.methods:
                lines.append(f"  It has {len(cls.methods)} methods:")
                for m in cls.methods:
                    lines.append(f"    - Method '{m.name}' at line {m.lineno}.")
        lines.append("")

    lines.append(
        "Now provide a structured description that includes: "
        "1) a high-level summary of the file's purpose, "
        "2) the main components and how they relate, and "
        "3) suggestions for where a blind developer might start reading."
    )

    return "\n".join(lines)


def describe_code_file(
    path: str | Path,
    llm_client: BaseLLMClient,
    language: Optional[str] = "python",
) -> str:
    """
    Describe a code file in a way that is friendly to screen readers.

    Parameters
    ----------
    path:
        Path to the source file.
    llm_client:
        An implementation of BaseLLMClient that actually calls a model.
    language:
        Programming language of the file. Currently only 'python' is supported.

    Returns
    -------
    str
        Plain-text description suitable for blind and low-vision developers.
    """
    if language != "python":
        raise ValueError("Only 'python' is supported in v0.")

    structure = parse_python_file(path)
    prompt = _structure_to_prompt(structure)
    description = llm_client.generate(prompt)
    return description