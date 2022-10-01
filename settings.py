from typing import NamedTuple


class Zone(NamedTuple):
    tag: str
    items_range: range


URL = 'https://stat.artcore24.ru/'
PC = {
    'A ZONE': Zone(tag='azone', items_range=range(1, 9)),
    'B ZONE': Zone(tag='bzone', items_range=range(9, 17)),
    'C ZONE': Zone(tag='czone', items_range=range(17, 24)),
    'Y ZONE': Zone(tag='yzone', items_range=range(25, 37)),
    'X ZONE': Zone(tag='xzone', items_range=range(42, 48)),
    '2F ROOM': Zone(tag='twofroomzone', items_range=range(40, 42)),
    'ONE G': Zone(tag='onegzone', items_range=range(37, 38)),
    'CHILL OUT': Zone(tag='chilloutzone', items_range=range(38, 39)),
    'CHILL OUT 2': Zone(tag='chillout2zone', items_range=range(39, 40)),
    'SIX GODS': Zone(tag='sixgodszone', items_range=range(48, 54))
}
CONSOLE = {
    'SIX GODS': Zone(tag='sixgods2zone', items_range=range(54, 55)),
    '1 ROOM': Zone(tag='room1zone', items_range=range(56, 57)),
    '2 ROOM': Zone(tag='room2zone', items_range=range(57, 58)),
    '3 ROOM': Zone(tag='room3zone', items_range=range(58, 59)),
    '4 ROOM': Zone(tag='room4zone', items_range=range(59, 60)),
    '5 ROOM': Zone(tag='room5zone', items_range=range(60, 61)),
    '6 ROOM': Zone(tag='room6zone', items_range=range(61, 62)),
}
