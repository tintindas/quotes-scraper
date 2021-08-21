from typing import List
import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError
from ..common import utils


def extract_quote_elements(url: str) -> List:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as err:
        return [err]

    document = BeautifulSoup(response.text, 'html.parser')
    quotes_table = document.find("table", class_="tableList")
    quote_elements = quotes_table.find_all("div", class_="quoteText")
    return len(quote_elements)


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


def extract_quote_data(quote_element: BeautifulSoup):

    quote_text = [string for string in quote_element.stripped_strings][0]
    links = quote_element.find_all("a", class_="authorOrTitle")
    author = links[0].string if len(links) else None
    source = links[1].string if len(links) > 1 else None
    return {quote_text, author, source}
