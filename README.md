Below is a README.md you can paste directly and tweak later.

A11y Dev Helper
A11y Dev Helper is an open-source AI-oriented tool that turns source code structures into clear, screen-reader-friendly explanations, summaries, and navigation cues for blind and low-vision developers.

Note: The default “AI client” is a placeholder. It shows you exactly where to plug in your own language model, but does not call any real provider.

Why this project exists
Many blind and low-vision developers rely on screen readers to work with code, but modern codebases are large, nested, and visually structured in ways that are hard to pick up line-by-line. A11y Dev Helper provides a simple way to:

Parse a code file.

Extract its structure (functions, classes, methods, docstrings).

Feed that structure to an AI client.

Get back a concise, linear description that works well with screen readers.

The goal is not to replace screen readers, but to give blind devs a quick mental map of “what’s in this file and where should I start?” before they dive in.

What it does (v0)
Parses a Python file using the standard library (ast).

Builds a plain-text prompt describing:

File path

Module docstring

Top-level functions (names, line numbers, short docstrings)

Classes and their methods

Designs the prompt specifically for blind and low-vision developers:

No visual references like “see above” or “on the left”

Short sentences and simple structure

Emphasis on “where to start reading”

Passes the prompt to a pluggable AI client (BaseLLMClient) to generate:

A high-level explanation

A summary of main components

Suggested navigation cues (e.g., which function/class to read first)

The repo ships with:

PlaceholderLLMClient – a stub that returns a template explanation, so the full flow works out-of-the-box without any API keys.

Extensible architecture so you can easily add a real LLM client in your own fork or project.

Who this is for
Blind and low-vision developers who want a higher-level overview of a file before reading it line-by-line with a screen reader.

Tool builders who want to integrate AI-generated structural descriptions into editors, CLIs, or educational tools.

Accessibility-focused contributors who want to experiment with better ways to represent code structure and navigation in text.

Project status
This is an early, experimental version focused on single-file Python parsing and a clean, provider-agnostic core. The aim is to grow into a small ecosystem of:

Multiple language parsers (JS/TS, Java, etc.).

Better navigation cues and landmarks.

Optional editor / CLI integrations built on top.