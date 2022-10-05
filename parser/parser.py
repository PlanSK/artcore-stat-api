import requests
from bs4 import BeautifulSoup
from pydantic import BaseModel

from .settings import URL, ZONES, Zone


class Console(BaseModel):
    id: int
    name: str
    is_busy: bool


class GameZone(BaseModel):
    id: int
    name: str
    all_items: list
    busy_items: list
    free_items: list


class Zones(BaseModel):
    pc_zones_list: list[GameZone] = []
    console_zones_list: list[Console] = []


def get_stat_page(url: str) -> str:
    """
    Return text of page on request url.
    """
    request = requests.get(url)
    request.encoding = 'utf-8'
    if request.status_code != 200:
        raise ValueError('Status code is not 200')
    return request.text


def get_current_loads(zone: Zone,
                      bs_object: BeautifulSoup) -> GameZone | Console:
    """
    Return dict with load of zone
    """
    tag_list = bs_object.find_all('p', zone.tag_class_name)
    all_items_set = set(
        (int(tag.get_text(strip=True)), tag.img.attrs.get('src'))
        for tag in tag_list
        if int(tag.get_text(strip=True)) in zone.items_range
    )
    all_items_list = list(zone.items_range)
    busy_items = [
        item_id for item_id, img_name in all_items_set
        if img_name.find('red') >= 0
    ]
    if zone.zone_type == 'pc':
        return GameZone(
            id=zone.id,
            name=zone.name,
            all_items=all_items_list,
            busy_items=busy_items,
            free_items=list(set(all_items_list) - set(busy_items)),
        )

    is_busy = True if busy_items else False
    return Console(
        id=zone.id,
        name=zone.name,
        is_busy=is_busy
    )


def get_zones_data(url: str) -> Zones:
    """
    Return list with loads data PC and CONSOLE zones
    or empty list if url address is not available.
    """
    try:
        html = get_stat_page(url)
    except:
        return Zones()
    bs_object = BeautifulSoup(html, "lxml")
    zones_data = Zones()
    for zone in ZONES:
        current_zone = get_current_loads(zone=zone, bs_object=bs_object)
        if isinstance(current_zone, GameZone):
            zones_data.pc_zones_list.append(current_zone)
        elif isinstance(current_zone, Console):
            zones_data.console_zones_list.append(current_zone)
        else:
            raise TypeError('Unknown type data of zone')


    return zones_data


if __name__ == "__main__":
    print(get_zones_data(URL))
