import random
import string
from typing import List


class TextMasker:
    def __init__(self, seed: int | None = None):
        if seed is not None:
            random.seed(seed)

    def inject_noise(self, text: str, amount: int | None = None) -> str:
        if amount is None:
            amount = max(1, len(text) // 3)

        chars = list(text)
        for _ in range(amount):
            chars.insert(
                random.randint(0, len(chars)),
                random.choice(string.ascii_letters + string.digits),
            )
        return "".join(chars)

    def reverse_text(self, text: str) -> str:
        return text[::-1]

    def fragment_text(self, text: str) -> str:
        return " + ".join(f"'{c}'" for c in text)

    def unicode_mask(self, text: str) -> str:
        return "".join(f"\\u{ord(c):04x}" for c in text)

    def layered_mask(self, text: str, steps: List[str]) -> str:
        for step in steps:
            text = getattr(self, step)(text)
        return text
