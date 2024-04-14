from __future__ import annotations

from typing import TYPE_CHECKING, List, Optional

from BaseClasses import Item, Location, Region
from .constants import ID_BY_LOCATION, LOCATIONS, LOCATIONS_BY_REGION

if TYPE_CHECKING:
    from . import YTGVWorld

class YTGVLocation(Location):
    game = "Yellow Taxi Goes Vroom"

class YTGVRegion(Region):
    def __init__(self, name: str, world: YTGVWorld):
        super().__init__(name, world.player, world.multiworld)

        locations: List[str] = LOCATIONS_BY_REGION.get(name, []).copy()

        id_by_location = {
            name: ID_BY_LOCATION[name]
            for name in locations
        }

        self.add_locations(id_by_location, YTGVLocation)
        self.multiworld.regions.append(self)

class YTGVItem(Item):
    game = "Yellow Taxi Goes Vroom"
