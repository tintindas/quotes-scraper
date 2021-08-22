from quotes_scraper.common.quote import Quote
from typing import List
from bs4.element import ResultSet, Tag
from pytest import raises
from requests import HTTPError
from bs4 import BeautifulSoup
from ..scraper import web_scraper


quote_element_1 = """<div class="quoteText">
                "Tomorrow may be hell, but today was a good writing day, and on the good writing days nothing else matters."
                <br/>
                —
                  <a class="authorOrTitle" href="/author/quotes/1221698.Neil_Gaiman" title="Neil Gaiman quotes">Neil Gaiman</a>
</div>"""

quote_element_2 = """
<div class="quoteText">
                "She says nothing at all, but simply stares upward into the dark sky and watches, with sad eyes, the slow dance of the infinite stars."
                <br/>
                —
                  <a class="authorOrTitle" href="/author/quotes/1221698.Neil_Gaiman" title="Neil Gaiman quotes">Neil Gaiman</a>
                  (<a class="authorOrTitle" href="/book/show/16793.Stardust">Stardust</a>)
              </div>
"""

markup_1 = f"""<table class="tableList">
<tbody>
    <tr>
        <td>
            {quote_element_1}
        </td>
    </tr>
    <tr>
        <td>
            {quote_element_2}
        </td>
    </tr>
</tbody>
</table>
"""

markup_2 = """<table class="tableList">
<tbody>
    <tr>
        <td>
            <div>Lorem ipsum</div>
        </td>
    </tr>
    <tr>
        <td>
            <div>Lorem ipsum</div>
        </td>
    </tr>
</tbody>
</table>
"""

soup_1 = BeautifulSoup(markup_1, "html.parser")
soup_2 = BeautifulSoup(markup_2, "html.parser")
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
def test_extract_quote_elements_with_valid_input() -> None:
    """Should get list of BeautifulSoup objects.
    """
    return_value = web_scraper.extract_quote_elements(soup_1)

    assert type(return_value) is ResultSet
    assert len(return_value) == 2
    assert type(return_value[0]) is Tag


def test_extract_quote_elements_with_no_quotes() -> None:
    """Should return empty result set.
    """

    return_value = web_scraper.extract_quote_elements(soup_2)

    assert type(return_value) is ResultSet
    assert len(return_value) == 0


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
        BeautifulSoup(quote_element_1, "html.parser"))
    assert type(quote) is Quote
    assert quote.get_text() == '"Tomorrow may be hell, but today was a good writing day, and on the good writing days nothing else matters."'
    assert quote.get_author() == "Neil Gaiman"
    assert quote.get_source() == None


def test_extract_quote_data_with_source() -> None:
    """Should return Quote object with all properties set.
    """
    quote = web_scraper.extract_quote_data(
        BeautifulSoup(quote_element_2, "html.parser"))
    assert type(quote) is Quote
    assert quote.get_text() == '"She says nothing at all, but simply stares upward into the dark sky and watches, with sad eyes, the slow dance of the infinite stars."'
    assert quote.get_author() == "Neil Gaiman"
    assert quote.get_source() == "Stardust"


def test_extract_quote_data_with_invalid_input() -> None:
    """Should raise Value Error.
    """
    with raises(ValueError):
        web_scraper.extract_quote_data(
            BeautifulSoup("Gibberish", "html.parser"))
