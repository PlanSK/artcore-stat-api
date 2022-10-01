from typing import Union

import requests
from bs4 import BeautifulSoup
from pydantic import BaseModel

from settings import PC, CONSOLE, URL, Zone


class GameZone(BaseModel):
    id: int
    name: str
    all_items: int
    busy_items: int
    free_items: int

class ZonesLoadData(BaseModel):
    pc_zone: list[GameZone]
    console_zone: list[GameZone]


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
    limit = bs_object.find_all('p', zone.tag)
    tags_set = set(
        tag for tag in limit
        if int(tag.get_text(strip=True)) in zone.items_range
    )
    all_count = len(tags_set)
    busy_items = [
        tag for tag in tags_set 
        if (tag.img.attrs.get('src') and
                tag.img.attrs.get('src').find('red') >= 0)
    ]
    busy_count = len(busy_items)
    return GameZone(
        id=zone.id,
        name=zone.name,
        all_items=all_count,
        busy_items=busy_count,
        free_items=all_count - busy_count,
    )


def get_zone_data(url: str) -> Union[ZonesLoadData, None]:
    """
    Return JSON with loads data PC and CONSOLE zones
    or None if url address is not available.
    """
    try:
        html = get_stat_page(url)
    except:
        return None
    bs_object = BeautifulSoup(html, "lxml")
    pc_zone = [
        get_current_loads(zone=zone, bs_object=bs_object) for zone in PC
    ]
    console_zone = [
        get_current_loads(zone=zone, bs_object=bs_object) for zone in CONSOLE
    ]

    return ZonesLoadData(pc_zone=pc_zone, console_zone=console_zone)


if __name__ == "__main__":
    print(get_zone_data(URL))
