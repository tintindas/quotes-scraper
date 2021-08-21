from .constants import BASE_URL


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

    result_url = base_url.replace("[QUERY]", query_string)

    return result_url


def insert_page_number(base_url: str = BASE_URL, page_number: int = 1) -> str:
    """Inserts page number into given base_url

    Args:
        page_number (int): The page number to be scraped. Defaults to 1.
        base_url (str, optional): Goodreads URL. Defaults to BASE_URL.

    Returns:
        str: URL with page number parameter set.
    """

    page_number_string = str(page_number)

    result_url = base_url.replace("[PAGE]", page_number_string)

    return result_url
