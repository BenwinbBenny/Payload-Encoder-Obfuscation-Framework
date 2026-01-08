import base64
import codecs


class EncoderEngine:
    def base64_wrap(self, text: str) -> str:
        return base64.b64encode(text.encode()).decode()

    def base64_unwrap(self, text: str) -> str:
        return base64.b64decode(text.encode()).decode()

    def rot_cipher(self, text: str) -> str:
        return codecs.encode(text, "rot_13")

    def xor_mask(self, text: str, key: str = "veil") -> str:
        output = []
        for i, c in enumerate(text):
            output.append(f"{ord(c) ^ ord(key[i % len(key)]):02x}")
        return "".join(output)

    def xor_unmask(self, text: str, key: str = "veil") -> str:
        chars = []
        for i in range(0, len(text), 2):
            b = int(text[i:i+2], 16)
            chars.append(chr(b ^ ord(key[(i // 2) % len(key)])))
        return "".join(chars)
