from abc import ABC, abstractmethod
from typing import Any


class BaseLLMClient(ABC):
    """
    Abstract base class for language model clients.

    Library users should subclass this and implement `generate()`
    using any provider they like (OpenAI, local model, etc).
    """

    @abstractmethod
    def generate(self, prompt: str, **kwargs: Any) -> str:
        """
        Given a prompt, return generated text.

        This method should be synchronous and return plain text suitable
        for screen readers (no markdown tables, no code fencing required).
        """
        raise NotImplementedError