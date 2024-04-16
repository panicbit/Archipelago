from __future__ import annotations

from typing import TYPE_CHECKING, Dict

from worlds.generic.Rules import CollectionRule

if TYPE_CHECKING:
    from . import YTGVWorld

class YTGVRules:
    world: YTGVWorld
    connection_rules: Dict[str, CollectionRule]

    def __init__(self, world: YTGVWorld):
        self.world = world
        player = world.player
        options = world.options

        self.connection_rules = {
            "Morio's Lab -> Morio's Island":
                lambda state: state.has("Gear", player, options.morios_island_required_gears),
            "Morio's Lab -> Bombeach":
                lambda state: state.has("Gear", player, options.bombeach_required_gears),
            "Morio's Lab -> Arcade Plaza":
                lambda state: state.has("Gear", player, options.arcade_plaza_required_gears),
            "Morio's Lab -> Pizza Time":
                lambda state: state.has("Gear", player, options.pizza_time_required_gears),
            "Morio's Lab -> Tosla Square":
                lambda state: state.has("Gear", player, options.tosla_square_required_gears),
            "Morio's Lab -> Maurizio's City":
                lambda state: state.has("Gear", player, options.maurizios_city_required_gears),
            "Morio's Lab -> Crash Test Industries":
                lambda state: state.has("Gear", player, options.crash_test_industries_required_gears),
            "Morio's Lab -> Anticipation":
                lambda state: state.has("Gear", player, options.anticipation_required_gears),
        }

    def set(self):
        player = self.world.player
        multiworld = self.world.multiworld

        for entrance_name, rule in self.connection_rules.items():
            entrance = multiworld.get_entrance(entrance_name, player)
            entrance.access_rule = rule

        # Set up completion
        event_she_is_fine_now = self.world.create_item("She is fine now!");
        multiworld.get_location("Granny", player).place_locked_item(event_she_is_fine_now)
        multiworld.completion_condition[player] = lambda state: state.has(event_she_is_fine_now.name, player)
