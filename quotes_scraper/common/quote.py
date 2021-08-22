class Quote:
    text: str
    author: str
    source: str

    def __init__(self, text: str, author: str, source: str):
        """Initialises quote object with text, author and source provided.

        Args:
            text (str): Text of quote
            author (str): Author 
            source (str): Source material
        """
        self.text = text
        self.author = author
        self.source = source

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
