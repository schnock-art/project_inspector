from .base_writer import BaseWriter

class MarkdownWriter(BaseWriter):
    def render(self, text: str) -> str:
        return text  # Markdown is already markdown 😎
