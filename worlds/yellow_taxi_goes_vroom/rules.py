from __future__ import annotations

from typing import TYPE_CHECKING, Dict

from worlds.generic.Rules import CollectionRule

from .subclasses import YTGVItem

if TYPE_CHECKING:
    from . import YTGVWorld

class YTGVRules:
    world: YTGVWorld
    connection_rules: Dict[str, CollectionRule]
    location_rules: Dict[str, CollectionRule]
    event_bombcar: YTGVItem
    event_noble_knight: YTGVItem
    event_orange_button: YTGVItem
    event_now_i_remember: YTGVItem
    event_she_is_fine_now: YTGVItem

    def __init__(self, world: YTGVWorld):
        self.world = world
        self.event_doggo = self.world.create_item("Doggo")
        self.event_bombcar = self.world.create_item("Bomboss defeated")
        self.event_noble_knight = self.world.create_item("Noble Knight!")
        self.event_orange_button = self.world.create_item("Orange Button")
        self.event_now_i_remember = self.world.create_item("Now I remember!")
        self.event_she_is_fine_now = self.world.create_item("She is fine now!")
        player = world.player
        options = world.options

        self.connection_rules = {
            "Granny's Island -> Ice-Cream truck":
                lambda state: state.has(self.event_bombcar.name, player),
            "Granny's Island -> Pizza Oven":
                lambda state: state.has(self.event_noble_knight.name, player),
            "Granny's Island -> Fecal Matters":
                lambda state: state.has(self.event_doggo.name, player),
            "Granny's Island -> Crash Again":
                lambda state: state.has(self.event_orange_button.name, player),
            "Granny's Island -> Flushed Away":
                lambda state: state.has(self.event_orange_button.name, player),
            "Granny's Island -> Moon":
                lambda state: state.has(self.event_she_is_fine_now.name, player),
            "Granny's Island -> Mosk's Rocket":
                lambda state: state.has(self.event_she_is_fine_now.name, player),
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
                lambda state: (
                    state.has("Gear", player, options.maurizios_city_required_gears) and
                    state.has("Golden Spring", player)
                ),
            "Morio's Lab -> Crash Test Industries":
                lambda state: (
                    state.has("Gear", player, options.crash_test_industries_required_gears) and
                    state.has("Golden Spring", player)
                ),
            "Morio's Lab -> Morio's Mind":
                lambda state: (
                    state.has(self.event_orange_button.name, player) and
                    state.has("Golden Spring", player)
                ),
            "Morio's Lab -> Observing":
                lambda state: state.has(self.event_now_i_remember.name, player),
            "Morio's Lab -> Anticipation":
                lambda state: (
                    state.has("Golden Propeller", player) and
                    state.has("Gear", player, options.anticipation_required_gears)
                ),
        }

        self.location_rules = {
            "Doggo":
                lambda state: state.has("Golden Spring", player),
        }

    def set(self):
        player = self.world.player
        world = self.world
        multiworld = self.world.multiworld

        for entrance_name, rule in self.connection_rules.items():
            entrance = world.get_entrance(entrance_name)
            entrance.access_rule = rule

        for location_name, rule in self.location_rules.items():
            location = world.get_location(location_name)
            location.access_rule = rule

        # Place events
        world.get_location("Bombcar").place_locked_item(self.event_bombcar)
        world.get_location("Doggo").place_locked_item(self.event_doggo)
        world.get_location("Pizza King").place_locked_item(self.event_noble_knight)
        world.get_location("Orange Button").place_locked_item(self.event_orange_button)
        world.get_location("Passkey").place_locked_item(self.event_now_i_remember)
        world.get_location("Granny").place_locked_item(self.event_she_is_fine_now)

        # Set up completion
        multiworld.completion_condition[player] = lambda state: state.has(self.event_she_is_fine_now.name, player)
