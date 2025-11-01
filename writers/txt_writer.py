from .base_writer import BaseWriter

class TextWriter(BaseWriter):
    def render(self, text: str) -> str:
        # Strip markdown formatting for plain text
        cleaned = text.replace("#", "").replace("*", "")
        return cleaned
