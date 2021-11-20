from quotes_scraper.common.quote import Quote
from typing import List
from bs4.element import ResultSet, Tag
from pytest import raises
from requests import HTTPError
from bs4 import BeautifulSoup
from ..scraper import web_scraper
from .mock_data.quotes_elements import quote_element_1, quote_element_2

# ** ---------------------------- Get Page Tests ---------------------------- ** #


def test_get_page_with_valid_url() -> None:
    """Should return beautiful soup object.
    """
    URL = "https://www.goodreads.com/search?page=1&q=neil+gaiman&search_type=quotes"

    assert type(web_scraper.get_page(URL)) is BeautifulSoup


def test_get_page_with_invalid_url() -> None:
    """Should raise HTTP Error.
    """
    URL = "https://www.github.com/tintindas/invalid"

    with raises(HTTPError):
        web_scraper.get_page(URL)


# ** ---------------------------- Extract Quote Elements Tests ---------------------------- ** #
def test_extract_quote_elements_with_invalid_input() -> None:
    """Should return empty result set.
    """

    return_value = web_scraper.extract_quote_elements(
        BeautifulSoup("Gibberish", "html.parser"))

    assert type(return_value) is ResultSet
    assert len(return_value) == 0


# ** ---------------------------- Extract Quote Data Tests ---------------------------- ** #
def test_extract_quote_data_without_source() -> None:
    """Should return Quote Object with source set to None."""

    quote = web_scraper.extract_quote_data(
        BeautifulSoup(quote_element_2, "html.parser"))
    assert type(quote) is Quote
    assert quote.get_text() == "Tomorrow may be hell, but today was a good writing day, and on the good writing days nothing else matters."
    assert quote.get_author() == "Neil Gaiman"
    assert quote.get_source() == None
    assert quote.get_tags() == ["writing"]


def test_extract_quote_data_with_source() -> None:
    """Should return Quote object with all properties set.
    """
    quote = web_scraper.extract_quote_data(
        BeautifulSoup(quote_element_1, "html.parser"))
    assert type(quote) is Quote
    assert quote.get_text() == "Fairy tales are more than true: not because they tell us that dragons exist, but because they tell us that dragons can be beaten."
    assert quote.get_author() == "Neil Gaiman"
    assert quote.get_source() == "Coraline"
    assert quote.get_tags() == ['books', 'dragons', 'fairy-tales',
                                'inspirational', 'paraphrasing-g-k-chesterton']


def test_extract_quote_data_with_invalid_input() -> None:
    """Should raise Value Error.
    """
    with raises(ValueError):
        web_scraper.extract_quote_data(
            BeautifulSoup("Gibberish", "html.parser"))
