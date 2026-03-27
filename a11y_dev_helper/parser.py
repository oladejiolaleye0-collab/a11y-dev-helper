import ast
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional


@dataclass
class FunctionInfo:
    name: str
    lineno: int
    docstring: Optional[str] = None


@dataclass
class ClassInfo:
    name: str
    lineno: int
    docstring: Optional[str] = None
    methods: List[FunctionInfo] = field(default_factory=list)


@dataclass
class ModuleStructure:
    path: str
    module_docstring: Optional[str]
    functions: List[FunctionInfo]
    classes: List[ClassInfo]


def parse_python_file(path: str | Path) -> ModuleStructure:
    """
    Parse a Python file and return a simple structural representation.

    This is deliberately minimal and focused on:
    - module docstring
    - top-level functions
    - classes and their methods
    """
    file_path = Path(path)
    source = file_path.read_text(encoding="utf-8")

    tree = ast.parse(source, filename=str(file_path))
    module_docstring = ast.get_docstring(tree)

    functions: List[FunctionInfo] = []
    classes: List[ClassInfo] = []

    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            functions.append(
                FunctionInfo(
                    name=node.name,
                    lineno=node.lineno,
                    docstring=ast.get_docstring(node),
                )
            )
        elif isinstance(node, ast.ClassDef):
            class_doc = ast.get_docstring(node)
            methods: List[FunctionInfo] = []
            for sub in node.body:
                if isinstance(sub, ast.FunctionDef):
                    methods.append(
                        FunctionInfo(
                            name=sub.name,
                            lineno=sub.lineno,
                            docstring=ast.get_docstring(sub),
                        )
                    )
            classes.append(
                ClassInfo(
                    name=node.name,
                    lineno=node.lineno,
                    docstring=class_doc,
                    methods=methods,
                )
            )

    return ModuleStructure(
        path=str(file_path),
        module_docstring=module_docstring,
        functions=functions,
        classes=classes,
    )