class BaseWriter:
    def render(self, text: str) -> str:
        raise NotImplementedError