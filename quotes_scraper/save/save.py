import csv
from datetime import date
from typing import List

from quotes_scraper.common.quote import Quote


def save_to_csv(data: List[Quote], filename: str = None) -> None:
    field_names = ["text", "author", "source", "tags"]

    if not filename:
        today = date.today()
        filename = f"quotes_{today.strftime('%d-%b-%Y')}.csv"

    if ".csv" not in filename:
        filename = filename + ".csv"

    with open(filename, 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(data)
