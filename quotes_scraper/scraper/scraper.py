import requests
from ..common import constants

page = requests.get(constants.BASE_URL)

print(page.text)
