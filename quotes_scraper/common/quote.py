from typing import List


class Quote:
    text: str
    author: str
    source: str
    tags: List

    def __init__(self, text: str, author: str, source: str, tags: List):
        """Initialises quote object with text, author and source provided.

        Args:
            text (str): Text of quote
            author (str): Author 
            source (str): Source material
        """
        self.text = text
        self.author = author
        self.source = source
        self.tags = tags

    def __str__(self) -> str:
        return f"""Quote {{\n\ttext: {self.text},\n\tauthor: {self.author},\n\tsource: {self.source},\n\ttags: {self.tags}\n}}
        """
