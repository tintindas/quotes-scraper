import pytest
from ..common import utils
from ..common.constants import PAGE_PLACEHOLDER, QUERY_PLACEHOLDER, BASE_URL

# ** ---------------------------- Insert Query Tests ---------------------------- ** #


def test_insert_query_with_valid_input() -> None:
    """Should insert the query string in place of the query placeholder.
    """

    assert utils.insert_query(
        "Neil Gaiman") == f"https://www.goodreads.com/search?page={PAGE_PLACEHOLDER}&q=Neil+Gaiman&search_type=quotes"


def test_insert_query_without_input() -> None:
    """Should throw TypeError when insert query is called without any arguments.
    """

    with pytest.raises(TypeError):
        utils.insert_query()


def test_insert_query_with_empty_input() -> None:
    """Should replace the query placeholder with an empty string.
    """

    assert utils.insert_query(
        "") == f"https://www.goodreads.com/search?page={PAGE_PLACEHOLDER}&q=&search_type=quotes"


def test_insert_query_with_base_input() -> None:
    """Should replace the query placeholder in the base url provided.
    """

    assert utils.insert_query(
        "Terry Pratchett", "prefix [QUERY] suffix") == "prefix Terry+Pratchett suffix"


# ** ---------------------------- Insert Page Number Tests ---------------------------- ** #
def test_insert_page_number_with_valid_input() -> None:
    """Should replace the page number placeholder with the input number.
    """

    assert utils.insert_page_number(
        5) == f"https://www.goodreads.com/search?page=5&q={QUERY_PLACEHOLDER}&search_type=quotes"


def test_insert_page_number_without_input() -> None:
    """Should replace the page number placeholder with the 1.
    """

    assert utils.insert_page_number(
    ) == f"https://www.goodreads.com/search?page=1&q={QUERY_PLACEHOLDER}&search_type=quotes"


def test_insert_page_number_with_empty_input() -> None:
    """Should replace the page number placeholder with the 1.
    """

    assert utils.insert_page_number(
        "") == f"https://www.goodreads.com/search?page=1&q={QUERY_PLACEHOLDER}&search_type=quotes"


def test_insert_page_number_with_base_url() -> None:
    """Should replace the page number placeholder in given url.
    """

    assert utils.insert_page_number(
        2, "prefix [PAGE] suffix") == "prefix 2 suffix"
