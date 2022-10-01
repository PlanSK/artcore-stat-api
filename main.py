from typing import NamedTuple

import requests
from bs4 import BeautifulSoup


class Zone(NamedTuple):
    tag: str
    pc_range: range


URL = 'https://stat.artcore24.ru/'

PC = {
    'A ZONE': Zone(tag='azone', pc_range=range(1, 9)),
    'B ZONE': Zone(tag='bzone', pc_range=range(9, 17)),
    'C ZONE': Zone(tag='czone', pc_range=range(17, 24)),
    'Y ZONE': Zone(tag='yzone', pc_range=range(25, 37)),
    'X ZONE': Zone(tag='xzone', pc_range=range(42, 48)),
    '2F ROOM': Zone(tag='twofroomzone', pc_range=range(40, 42)),
    'ONE G': Zone(tag='onegzone', pc_range=range(37, 38)),
    'CHILL OUT': Zone(tag='chilloutzone', pc_range=range(38, 39)),
    'CHILL OUT 2': Zone(tag='chillout2zone', pc_range=range(39, 40)),
    'SIX GODS': Zone(tag='sixgodszone', pc_range=range(48, 54))
}

CONSOLE = {
    'SIX GODS': Zone(tag='sixgods2zone', pc_range=range(54, 55)),
    '1 ROOM': Zone(tag='room1zone', pc_range=range(56, 57)),
    '2 ROOM': Zone(tag='room2zone', pc_range=range(57, 58)),
    '3 ROOM': Zone(tag='room3zone', pc_range=range(58, 59)),
    '4 ROOM': Zone(tag='room4zone', pc_range=range(59, 60)),
    '5 ROOM': Zone(tag='room5zone', pc_range=range(60, 61)),
    '6 ROOM': Zone(tag='room6zone', pc_range=range(61, 62)),
}


def get_stat_page(url: str) -> str:
    request = requests.get(url)
    request.encoding = 'utf-8'
    if request.status_code == 200:
        return request.text
    raise ValueError('Status code is not 200')


def get_current_loads():
    pass


def get_zone_data(html: str):
    bs_object = BeautifulSoup(html, "lxml")
    for title, params in PC.items():
        limit = bs_object.find_all('p', 'czone')
    list_num = set(tag for tag in limit if int(tag.text.strip()) in range(17, 25))
    return list_num


if __name__ == "__main__":
    html = get_stat_page(URL)
    print(parse_html(html))