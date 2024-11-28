from dataclasses import dataclass
from BaseClasses import Item, ItemClassification, Region
from Options import DeathLinkMixin, PerGameCommonOptions
from worlds.AutoWorld import World
from .regions import *

@dataclass
class AssOptions(DeathLinkMixin, PerGameCommonOptions):
    pass

class ASSItem(Item):
    game = "ASS"

class AssWorld(World):
    """
    A.S.S. (Archipelago Super Shenanigans) is a chaotic multiworld randomizer game filled with
    absurd challenges and quirky characters. Players explore bizarre islands, tackle ridiculous
    mini-games, and collect outrageous items in a hilariously unpredictable adventure.
    Expect laughter, mayhem, and a whole lot of silliness!
    """
    game = "ASS"
    options_dataclass = AssOptions
    options: AssOptions

    base_offset = 0xA55_000

    item_name_to_id = {
        "A": base_offset + 0,
        "S": base_offset + 1,
    }

    location_name_to_id = {
        WHERE_THE_SUN_DONT_SHINE: base_offset + 0,
        UP_YOURS: base_offset + 1,
        THE_REAR_END: base_offset + 2,
    }

    required_client_version = (0, 4, 4)

    def create_regions(self) -> None:
        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)

        nether_region = Region("Nether", self.player, self.multiworld)
        self.multiworld.regions.append(nether_region)

        menu_region.connect(nether_region)

        nether_region.add_locations({
            WHERE_THE_SUN_DONT_SHINE: self.location_name_to_id[WHERE_THE_SUN_DONT_SHINE],
            UP_YOURS: self.location_name_to_id[UP_YOURS],
            THE_REAR_END: self.location_name_to_id[THE_REAR_END],
        })

    def create_items(self) -> None:
        self.multiworld.itempool.extend([
            self.create_item("A"),
            self.create_item("S"),
            self.create_item("S"),
        ])

    def set_rules(self) -> None:
        pass

    def create_item(self, name: str) -> ASSItem:
        item_id: int | None = self.item_name_to_id.get(name, None)

        return ASSItem(
            name,
            ItemClassification.progression,
            item_id,
            self.player
        )
