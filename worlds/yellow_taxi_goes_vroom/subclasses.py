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

        # Event locations
        if self.name == "Morio's Lab":
            doggo = YTGVLocation(world.player, "Doggo", None, self)
            self.locations.append(doggo)

        if self.name == "Bombeach":
            bombcar = YTGVLocation(world.player, "Bombcar", None, self)
            self.locations.append(bombcar)

        if self.name == "Pizza Time":
            pizza_king = YTGVLocation(world.player, "Pizza King", None, self)
            self.locations.append(pizza_king)

        if self.name == "Crash Test Industries":
            orange_button = YTGVLocation(world.player, "Orange Button", None, self)
            self.locations.append(orange_button)

        if self.name == "Morio's Mind":
            pass_key = YTGVLocation(world.player, "Passkey", None, self)
            self.locations.append(pass_key)

        if self.name == "Spaceship":
            granny = YTGVLocation(world.player, "Granny", None, self)
            self.locations.append(granny)

        self.multiworld.regions.append(self)

class YTGVItem(Item):
    game = "Yellow Taxi Goes Vroom"
