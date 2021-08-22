from bs4.element import ResultSet, Tag
from quotes_scraper.common.quote import Quote
from typing import List
import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
from ..common.utils import strip_quotes


def get_page(url: str) -> BeautifulSoup:
    """Make a get request for the provided url and return a BeautifulSoup object of the html document if request is successful else raise an HTTPError.

    Args:
        url (str): URL to fetch.

    Returns:
        BeautifulSoup: The response HTML document wrapped in a BeautifulSoup object.
    """
    response = requests.get(url)
    response.raise_for_status()

    return BeautifulSoup(response.text, 'html.parser')


def extract_quote_elements(html: BeautifulSoup) -> ResultSet:
    """Returns a list of BeautifulSoup elements which have the class quoteText.

    Args:
        html (BeautifulSoup): HTML document to scan wrapped in BeautifulSoup object.

    Returns:
        List of BeautifulSoup objects.
    """
    quotes_table = html.find("table", class_="tableList")
    quote_elements = quotes_table.find_all(
        "div", class_="quoteText") if quotes_table else ResultSet([])
    return quote_elements


def extract_quote_data(quote_element: Tag) -> Quote:
    """Extract quote text, author and source from input.

    Args:
        quote_element (Tag): Element to extract data from.

    Returns:
        Quote: Quote object with extacted data.
    """
    if(quote_element.find("div", class_="quoteText") == None):
        raise ValueError

    quote_text = strip_quotes([
        string for string in quote_element.stripped_strings][0]) if quote_element else None
    links = quote_element.find_all("a", class_="authorOrTitle")
    author = links[0].string if len(links) else None
    source = links[1].string if len(links) > 1 else None

    return Quote(quote_text, author, source)
