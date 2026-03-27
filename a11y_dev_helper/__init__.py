"""
a11y_dev_helper

Core public interface for generating screen-reader-friendly descriptions
of source code files for blind and low-vision developers.
"""

from .summarizer import describe_code_file
from .models import BaseLLMClient