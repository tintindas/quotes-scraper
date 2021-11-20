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

    def get_text(self) -> str:
        """Get quote text

        Returns:
            str: quote text
        """
        return self.text

    def set_text(self, text: str) -> None:
        """Set text property of quote object.

        Args:
            text (str): Quote text.
        """
        self.text = text

    def get_author(self) -> str:
        """Get author of quote

        Returns:
            str: author of quote
        """
        return self.author

    def set_author(self, author: str) -> None:
        """Set author property of quote object

        Args:
            author (str): author of quote.
        """
        self.author = author

    def get_source(self) -> str:
        """Get source of quote.

        Returns:
            str: source of quote
        """
        return self.source

    def set_source(self, source: str) -> None:
        """Set source property of quote object.

        Args:
            source (str): Source of quote
        """
        self.source = source

    def get_tags(self) -> List:
        """Get tags associated with quote.

        Returns:
            List: List of tags
        """
        return self.tags

    def set_tags(self, tags: List) -> None:
        """Set tags associated with quote

        Args:
            tags (List): List of tags
        """
        self.tags = tags
