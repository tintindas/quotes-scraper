import logging
from typing import List

import requests
from bs4 import BeautifulSoup
from bs4.element import ResultSet, Tag
from quotes_scraper.common.quote import Quote
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
    quotes_table = html.find("div", class_="leftContainer")
    quote_elements = quotes_table.select(
        "div.quote.mediumText") if quotes_table else ResultSet([])
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

    quote = quote_element.find("div", class_="quoteText")

    quote_text = strip_quotes([
        string for string in quote.stripped_strings][0]) if quote else None
    author = quote.find("span", class_="authorOrTitle").string.strip().strip(",") if quote.find(
        "span", class_="authorOrTitle") else None
    source = quote.find("a", class_="authorOrTitle").string.strip() if quote.find(
        "a", class_="authorOrTitle") else None

    tag_container = quote_element.select("div.greyText.smallText.left")[
        0] if quote_element.select("div.greyText.smallText.left") else []
    tag_elements = [tag.string for tag in tag_container.find_all("a")]

    return Quote(quote_text, author, source, tag_elements)
