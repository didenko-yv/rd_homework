import datetime
import json
from pathlib import Path
from time import sleep
import requests

from shared import prepare_raw_dir


AUTH_TOKEN = "2b8d97ce57d401abd89f45b0079d8790edd940e6"


def sales_loader(sales_date: str):
    sales_page = 1
    while True:
        response = requests.get(
            url="https://fake-api-vycpfa6oca-uc.a.run.app/sales",
            params={"date": sales_date, "page": sales_page},
            headers={"Authorization": AUTH_TOKEN},
        )
        if response.status_code != 200:
            break
        yield sales_page, response.json()
        sales_page += 1


def get_json_save_path(dir_path: Path, sales_date: str, page_number=None):
    if page_number:
        return dir_path.joinpath(f"{sales_date}_{page_number}.json")
    return dir_path.joinpath(f"{sales_date}.json")


def save_to_file(data, save_path: Path):
    save_file = open(save_path, "w")
    json.dump(data, save_file)
    save_file.close()


def load_sales_data(sales_date: datetime.date, raw_dir: Path, total: bool = False):
    path = Path(raw_dir)
    prepare_raw_dir(path)

    all_day_sales = []
    for sales_page, sales_data in sales_loader(sales_date):
        if total:
            all_day_sales += sales_data
            continue

        save_path = get_json_save_path(path, sales_date, sales_page)
        save_to_file(sales_data, save_path)
    if total:
        save_path = get_json_save_path(path, sales_date)
        save_to_file(all_day_sales, save_path)
