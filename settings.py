from typing import NamedTuple


class Zone(NamedTuple):
    id: int
    name: str
    zone_type: str
    tag_class_name: str
    items_range: range


URL = 'https://stat.artcore24.ru/'
ZONES = (
    Zone(
        id=1,
        name='A ZONE',
        zone_type='pc',
        tag_class_name='azone',
        items_range=range(1, 9)
    ),
    Zone(
        id=2,
        name='B ZONE',
        zone_type='pc',
        tag_class_name='bzone',
        items_range=range(9, 17)
    ),
    Zone(
        id=3,
        name='C ZONE',
        zone_type='pc',
        tag_class_name='czone',
        items_range=range(17, 25)
    ),
    Zone(
        id=4,
        name='Y ZONE',
        zone_type='pc',
        tag_class_name='yzone',
        items_range=range(25, 37)
    ),
    Zone(
        id=5,
        name='X ZONE',
        zone_type='pc',
        tag_class_name='xzone',
        items_range=range(42, 48)
    ),
    Zone(
        id=6,
        name='2F ROOM',
        zone_type='pc',
        tag_class_name='twofroomzone',
        items_range=range(40, 42)
    ),
    Zone(
        id=7,
        name='ONE G',
        zone_type='pc',
        tag_class_name='onegzone',
        items_range=range(37, 38)
    ),
    Zone(
        id=8,
        name='CHILL OUT',
        zone_type='pc',
        tag_class_name='chilloutzone',
        items_range=range(38, 39)
    ),
    Zone(
        id=9,
        name='CHILL OUT 2',
        zone_type='pc',
        tag_class_name='chillout2zone',
        items_range=range(39, 40)
    ),
    Zone(
        id=10,
        name='SIX GODS',
        zone_type='pc',
        tag_class_name='sixgodszone',
        items_range=range(48, 54)
    ),
    Zone(
        id=11,
        name='SIX GODS',
        zone_type='console',
        tag_class_name='sixgods2zone',
        items_range=range(54, 55)
    ),
    Zone(
        id=12,
        name='1 ROOM',
        zone_type='console',
        tag_class_name='room1zone',
        items_range=range(56, 57)
    ),
    Zone(
        id=13,
        name='2 ROOM',
        zone_type='console',
        tag_class_name='room2zone',
        items_range=range(57, 58)
    ),
    Zone(
        id=14,
        name='3 ROOM',
        zone_type='console',
        tag_class_name='room3zone',
        items_range=range(58, 59)
    ),
    Zone(
        id=15,
        name='4 ROOM',
        zone_type='console',
        tag_class_name='room4zone',
        items_range=range(59, 60)
    ),
    Zone(
        id=16,
        name='5 ROOM',
        zone_type='console',
        tag_class_name='room5zone',
        items_range=range(60, 61)
    ),
    Zone(
        id=17,
        name='6 ROOM',
        zone_type='console',
        tag_class_name='room6zone',
        items_range=range(61, 62)
    ),
)
