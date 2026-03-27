import sys
from pathlib import Path

# Ensure project root is on sys.path when running directly
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from a11y_dev_helper import describe_code_file  # type: ignore
from a11y_dev_helper.placeholder_client import PlaceholderLLMClient  # type: ignore


def main() -> None:
    client = PlaceholderLLMClient()
    this_file = Path(__file__).resolve()
    description = describe_code_file(this_file, llm_client=client)
    print(description)


if __name__ == "__main__":
    main()