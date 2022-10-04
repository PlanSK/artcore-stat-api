from fastapi import FastAPI

from parser import get_zones_data, GameZone, Console, Zones
from settings import URL

app = FastAPI()


@app.get('/')
async def return_all_data() -> Zones:
    """
    Return all availabled data
    """
    return get_zones_data(URL)


@app.get('/id/{zone_id}')
async def return_zone_by_id(zone_id: int) -> list[GameZone | Console]:
    """
    Return list with zone data by zone id
    """
    pc_list = [
        zone for zone in get_zones_data(URL).pc_zones_list
        if zone.id == zone_id
    ]
    console_list = [
        zone for zone in get_zones_data(URL).console_zones_list
        if zone.id == zone_id
    ]
    return pc_list + console_list


@app.get('/console/')
async def return_consoles_list() -> list[Console]:
    """
    Returns all consoles zone list
    """
    return get_zones_data(URL).console_zones_list


@app.get('/console/{item_id}')
async def return_console_by_id(item_id: int) -> list[Console]:
    """
    Returns Console zone data by id
    """
    return [
        zone for zone in get_zones_data(URL).console_zones_list
        if zone.id == item_id
    ]


@app.get('/game_zone/')
async def return_game_zones_list() -> list[GameZone]:
    """
    Returns all game zones list with pc
    """
    return get_zones_data(URL).pc_zones_list


@app.get('/game_zone/{item_id}')
async def return_game_zone_by_id(item_id: int) -> list[GameZone]:
    """
    Returns GameZone zone data by id
    """
    return [
        zone for zone in get_zones_data(URL).pc_zones_list
        if zone.id == item_id
    ]
