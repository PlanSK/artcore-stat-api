from fastapi import FastAPI

from parser import get_zone_data, GameZone
from settings import URL

app = FastAPI()


@app.get('/')
async def return_all_data() -> list[GameZone]:
    """
    Return all availabled data
    """
    return get_zone_data(URL)


@app.get('/id/{zone_id}')
async def return_zone_by_id(zone_id: int) -> list[GameZone]:
    """
    Return zone data by zone id
    """
    return [zone for zone in get_zone_data(URL) if zone.id == zone_id]


@app.get('/type/{zone_type}')
async def return_zone_by_type(zone_type: str) -> list[GameZone]:
    """
    Returns zone list by zone type
    """
    return [
        zone for zone in get_zone_data(URL)
        if zone.zone_type == zone_type
    ]
