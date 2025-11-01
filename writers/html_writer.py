from .base_writer import BaseWriter


class HTMLWriter(BaseWriter):
    def render(self, text: str) -> str:
        return f"""
<html>
<head>
<meta charset="UTF-8">
<title>ProjectDoc</title>
</head>
<body>
{text}
</body>
</html>
"""
