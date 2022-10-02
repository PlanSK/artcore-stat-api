from typing import Union

import requests
from bs4 import BeautifulSoup
from pydantic import BaseModel

from settings import URL, ZONES, Zone


class GameZone(BaseModel):
    id: int
    name: str
    zone_type: str
    all_items: int
    busy_items: int
    free_items: int


def get_stat_page(url: str) -> str:
    """
    Return text of page on request url.
    """
    request = requests.get(url)
    request.encoding = 'utf-8'
    if request.status_code != 200:
        raise ValueError('Status code is not 200')
    return request.text


def get_current_loads(zone: Zone, bs_object: BeautifulSoup) -> GameZone:
    """
    Return dict with load of zone
    """
    tag_list = bs_object.find_all('p', zone.tag_class_name)
    tags_set = set(
        (int(tag.get_text(strip=True)), tag.img.attrs.get('src'))
        for tag in tag_list
        if int(tag.get_text(strip=True)) in zone.items_range
    )
    busy_items = [
        item_id for item_id, img_name in tags_set
        if img_name.find('red') >= 0
    ]
    all_count = len(tags_set)
    busy_count = len(busy_items)
    return GameZone(
        id=zone.id,
        name=zone.name,
        zone_type=zone.zone_type,
        all_items=all_count,
        busy_items=busy_count,
        free_items=all_count - busy_count,
    )


def get_zone_data(url: str) -> list[GameZone]:
    """
    Return JSON with loads data PC and CONSOLE zones
    or None if url address is not available.
    """
    try:
        html = get_stat_page(url)
    except:
        return []
    bs_object = BeautifulSoup(html, "lxml")
    zone_list = [
        get_current_loads(zone=zone, bs_object=bs_object) for zone in ZONES
    ]

    return zone_list


if __name__ == "__main__":
    print(get_zone_data(URL))
