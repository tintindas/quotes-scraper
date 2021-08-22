from .constants import BASE_URL
from .constants import PAGE_PLACEHOLDER
from .constants import QUERY_PLACEHOLDER


def insert_query(query: str, base_url: str = BASE_URL) -> str:
    """Inserts query into the base url and returns the resulting url

    Args:
        query (str): Author or keyword.
        base_url (str, optional): Goodreads search URL. Defaults to BASE_URL.

    Returns:
        str: URL with query parameter set.
    """

    query_words = query.split(" ")
    query_string = "+".join(query_words)

    result_url = base_url.replace(QUERY_PLACEHOLDER, query_string)

    return result_url


def insert_page_number(page_number: int = 1, base_url: str = BASE_URL) -> str:
    """Inserts page number into given base_url

    Args:
        page_number (int): The page number to be scraped. Defaults to 1.
        base_url (str, optional): Goodreads URL. Defaults to BASE_URL.

    Returns:
        str: URL with page number parameter set.
    """

    page_number_string = str(page_number) if page_number else "1"

    result_url = base_url.replace(PAGE_PLACEHOLDER, page_number_string)

    return result_url


def strip_quotes(text: str) -> str:
    """Removes quotes from the beginning and end of input string.

    Args:
        text (str): Text to be formatted.

    Returns:
        str: Input string minus any quotes at the start or the end of the string.
    """
    return text.removeprefix('"').removesuffix('"')
