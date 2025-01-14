from binascii import hexlify
from typing import Any, Dict, List, Optional

from BaseClasses import ItemClassification
from worlds.AutoWorld import World

from .subclasses import YTGVItem, YTGVRegion
from .options import YTGVOptions
from .constants import ITEMS, BUNNIES, GEARS, LOCATIONS, REGION_CONNECTIONS
from .rules import YTGVRules

class YTGVWorld(World):
    """Make full use of your advanced move-set to navigate hand-crafted retro worlds
    without a jump button in this vibrant love letter to the N64 era of collectathons!"""
    
    game = "Yellow Taxi Goes Vroom"
    # web = YellowTaxiGoesVroomWebWorld()

    options_dataclass = YTGVOptions
    options: YTGVOptions

    base_id: int = int(hexlify(b'ytgv'), 16) # 0x79746776

    item_name_to_id = {
        name: id
        for id, name in enumerate(ITEMS, base_id)
    }
    location_name_to_id = {
        name: id
        for id, name in enumerate(LOCATIONS, base_id)
    }
    location_name_groups = {}
    location_name_groups = {}

    total_gears: int = 0
    created_gears: int = 0
    required_gears: int = 0

    total_bunnies: int = 0
    created_bunnies: int = 0
    required_bunnies: int = 0

    def create_item(self, name: str) -> YTGVItem:
        item_id: Optional[int] = self.item_name_to_id.get(name, None)

        if name == "Gear":
            self.created_gears += 1
        
        if name == "Bunny":
            self.created_bunnies += 1

        item_classification = (
            ItemClassification.progression if item_id is None
            else self.get_item_classification(name)
        )

        return YTGVItem(name, item_classification, item_id, self.player)

    def create_regions(self) -> None:
        regions: List[YTGVRegion] = [
            YTGVRegion(name, self)
            for name in REGION_CONNECTIONS.keys()
        ]

        for region in regions:
            if region.name not in REGION_CONNECTIONS:
                raise f"Region `{region.name}` is missing in REGION_CONNECTIONS"

            exits: List[str] = REGION_CONNECTIONS[region.name]
            region.add_exits(exits)

    def create_items(self) -> None:
        self.create_gears()
        self.create_bunnies()
        self.create_other_items()

    def create_gears(self) -> None:
        self.total_gears = len(GEARS) # TODO: create option
        self.required_gears = max([
            self.options.morios_island_required_gears,
            self.options.bombeach_required_gears,
            self.options.arcade_plaza_required_gears,
            self.options.pizza_time_required_gears,
            self.options.tosla_square_required_gears,
            self.options.maurizios_city_required_gears,
            self.options.crash_test_industries_required_gears,
            self.options.morios_mind_required_gears,
            self.options.observing_required_gears,
            self.options.anticipation_required_gears,
        ])
    
        gears = [
            self.create_item("Gear")
            for _ in range(self.total_gears)
        ]

        self.created_gears = len(gears)

        # Lock first 3 gears to prevent unnecessary BK at the start
        morio = self.get_location("Granny's Island | Gear 1")
        morio.place_locked_item(gears.pop())
        morio = self.get_location("Granny's Island | Gear 27")
        morio.place_locked_item(gears.pop())
        morio = self.get_location("Granny's Island | Gear 26")
        morio.place_locked_item(gears.pop())


        self.multiworld.itempool += gears

    def create_bunnies(self) -> None:
        self.total_bunnies = len(BUNNIES) # TODO: create option
        self.required_bunnies = 0 # TODO: create option

        for location_name in BUNNIES:
            bunny = self.create_item("Bunny")
            self.created_bunnies += 1
            # TODO: lock bunnies until implemented properly
            location = self.get_location(location_name)
            location.place_locked_item(bunny)
            # self.multiworld.itempool.append(bunny)

    def create_other_items(self) -> None:
        golden_spring = self.create_item("Golden Spring")
        golden_propeller = self.create_item("Golden Propeller")

        # TODO: lock golden items until implemented properly
        self.get_location("Golden Spring").place_locked_item(golden_spring)
        self.get_location("Golden Propeller").place_locked_item(golden_propeller)
        # self.multiworld.itempool += [
        #     golden_spring,
        #     golden_propeller,
        # ]

    def set_rules(self) -> None:
        YTGVRules(self).set()
    
    def get_item_classification(self, name: str) -> ItemClassification:
        if name == "Gear" and self.created_gears <= self.required_gears:
            return ItemClassification.progression

        if name == "Bunny" and self.created_bunnies <= self.required_bunnies:
            return ItemClassification.progression

        if name == "Golden Spring":
            return ItemClassification.progression

        if name == "Golden Propeller":
            return ItemClassification.progression

        return ItemClassification.filler

    def fill_slot_data(self) -> Dict[str, Any]:
        return self.options.as_dict(
            "morios_island_required_gears",
            "bombeach_required_gears",
            "arcade_plaza_required_gears",
            "pizza_time_required_gears",
            "tosla_square_required_gears",
            "maurizios_city_required_gears",
            "crash_test_industries_required_gears",
            "morios_mind_required_gears",
            "observing_required_gears",
            "anticipation_required_gears",
        )