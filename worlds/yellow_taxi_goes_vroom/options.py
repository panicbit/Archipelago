from dataclasses import dataclass

from Options import DeathLink, DeathLinkMixin, PerGameCommonOptions, Range

class MoriosIslandRequiredGears(Range):
    """Number of gears required to open \"Morio's Home\""""
    display_name = "Morio's Home Required Gears"
    range_start = 0
    range_end = 250
    default = 3

class BombeachRequiredGears(Range):
    """Number of gears required to open \"Bombeach\""""
    display_name = "Bombeach Required Gears"
    range_start = 0
    range_end = 250
    default = 6

class ArcadePlazaRequiredGears(Range):
    """Number of gears required to open \"Arcade Plaza\""""
    display_name = "Arcade Plaza Required Gears"
    range_start = 0
    range_end = 250
    default = 18

class PizzaTimeRequiredGears(Range):
    """Number of gears required to open \"Pizza Time\""""
    display_name = "Pizza Time Required Gears"
    range_start = 0
    range_end = 250
    default = 32

class ToslaSquareRequiredGears(Range):
    """Number of gears required to open \"Tosla Square\""""
    display_name = "Tosla Square Required Gears"
    range_start = 0
    range_end = 250
    default = 50

class MauriziosCityRequiredGears(Range):
    """Number of gears required to open \"Maurizios City\""""
    display_name = "Maurizios City Required Gears"
    range_start = 0
    range_end = 250
    default = 65

class CrashTestIndustriesRequiredGears(Range):
    """Number of gears required to open \"Crash Test Industries\""""
    display_name = "Crash Test Industries Required Gears"
    range_start = 0
    range_end = 250
    default = 80

class MoriosMindRequiredGears(Range):
    """Number of gears required to open \"Morios Mind\""""
    display_name = "Morios Mind Required Gears"
    range_start = 0
    range_end = 250
    default = 0

class ObservingRequiredGears(Range):
    """Number of gears required to open \"Observing\""""
    display_name = "Observing Required Gears"
    range_start = 0
    range_end = 250
    default = 0

class AnticipationRequiredGears(Range):
    """Number of gears required to open \"Anticipation\""""
    display_name = "Anticipation Required Gears"
    range_start = 0
    range_end = 250
    default = 130

@dataclass
class YTGVOptions(PerGameCommonOptions, DeathLinkMixin):
    morios_island_required_gears: MoriosIslandRequiredGears
    bombeach_required_gears: BombeachRequiredGears
    arcade_plaza_required_gears: ArcadePlazaRequiredGears
    pizza_time_required_gears: PizzaTimeRequiredGears
    tosla_square_required_gears: ToslaSquareRequiredGears
    maurizios_city_required_gears: MauriziosCityRequiredGears
    crash_test_industries_required_gears: CrashTestIndustriesRequiredGears
    morios_mind_required_gears: MoriosMindRequiredGears
    observing_required_gears: ObservingRequiredGears
    anticipation_required_gears: AnticipationRequiredGears
