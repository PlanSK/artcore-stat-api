from typing import NamedTuple


class Zone(NamedTuple):
    id: int
    name: str
    tag: str
    items_range: range


URL = 'https://stat.artcore24.ru/'
PC = (
    Zone(
        id=1,
        name='A ZONE',
        tag='azone',
        items_range=range(1, 9)
    ),
    Zone(
        id=2,
        name='B ZONE',
        tag='bzone',
        items_range=range(9, 17)
    ),
    Zone(
        id=3,
        name='C ZONE',
        tag='czone',
        items_range=range(17, 25)
    ),
    Zone(
        id=4,
        name='Y ZONE',
        tag='yzone',
        items_range=range(25, 37)
    ),
    Zone(
        id=5,
        name='X ZONE',
        tag='xzone',
        items_range=range(42, 48)
    ),
    Zone(
        id=6,
        name='2F ROOM',
        tag='twofroomzone',
        items_range=range(40, 42)
    ),
    Zone(
        id=7,
        name='ONE G',
        tag='onegzone',
        items_range=range(37, 38)
    ),
    Zone(
        id=8,
        name='CHILL OUT',
        tag='chilloutzone',
        items_range=range(38, 39)
    ),
    Zone(
        id=9,
        name='CHILL OUT 2',
        tag='chillout2zone',
        items_range=range(39, 40)
    ),
    Zone(
        id=10,
        name='SIX GODS',
        tag='sixgodszone',
        items_range=range(48, 54)
    )
)
CONSOLE = (
    Zone(
        id=11,
        name='SIX GODS',
        tag='sixgods2zone',
        items_range=range(54, 55)
    ),
    Zone(
        id=12,
        name='1 ROOM',
        tag='room1zone',
        items_range=range(56, 57)
    ),
    Zone(
        id=13,
        name='2 ROOM',
        tag='room2zone',
        items_range=range(57, 58)
    ),
    Zone(
        id=14,
        name='3 ROOM',
        tag='room3zone',
        items_range=range(58, 59)
    ),
    Zone(
        id=15,
        name='4 ROOM',
        tag='room4zone',
        items_range=range(59, 60)
    ),
    Zone(
        id=16,
        name='5 ROOM',
        tag='room5zone',
        items_range=range(60, 61)
    ),
    Zone(
        id=17,
        name='6 ROOM',
        tag='room6zone',
        items_range=range(61, 62)
    ),
)
