import json

import requests
from bs4 import BeautifulSoup

from settings import PC, CONSOLE, URL, Zone


def get_stat_page(url: str) -> str:
    request = requests.get(url)
    request.encoding = 'utf-8'
    if request.status_code == 200:
        return request.text
    raise ValueError('Status code is not 200')


def get_current_loads(params: Zone, bs_object: BeautifulSoup) -> dict:
    limit = bs_object.find_all('p', params.tag)
    tags_set = set(
        tag for tag in limit
        if int(tag.get_text(strip=True)) in params.items_range
    )
    all_count = len(tags_set)
    busy_items = [
        tag for tag in tags_set 
        if (tag.img.attrs.get('src') and
                tag.img.attrs.get('src').find('red') >= 0)
    ]
    busy_count = len(busy_items)
    return {
        'all': all_count,
        'busy': busy_count,
        'free': all_count - busy_count,
    }


def get_zone_data(url: str):
    html = get_stat_page(URL)
    bs_object = BeautifulSoup(html, "lxml")
    pc_dict = {}
    console_dict = {}
    for title, params in PC.items():
        pc_dict.update({
            title: get_current_loads(params=params, bs_object=bs_object)
        })
    for title, params in CONSOLE.items():
        console_dict.update({
            title: get_current_loads(params=params, bs_object=bs_object)
        })
    return json.dumps(
        {
            'PC': pc_dict,
            'CONSOLE': console_dict,
        }
    )


if __name__ == "__main__":
    print(get_zone_data(URL))
