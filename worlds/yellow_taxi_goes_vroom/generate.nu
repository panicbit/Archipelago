
let base_id = 'ytgv' | into binary | encode hex | into int --radix 16 # 0x79746776

def main [] {
    let map_infos = open map_infos.json
    let items = $map_infos | create_items | to json --indent 4
    let gears = $map_infos | create_gears | to json --indent 4
    let bunnies = $map_infos | create_bunnies | to json --indent 4
    let locations = $map_infos | create_locations | to json --indent 4
    let locations_by_region = $map_infos | create_locations_by_region | to json --indent 4
    let region_connections = $map_infos | create_region_connections | to json --indent 4
    let id_by_location = $map_infos | create_id_by_location | to json --indent 4
$"# THIS FILE IS GENERATED.
# DO NOT MODIFY MANUALLY.
# USE `generate.nu` TO REGENERATE.

from typing import List, Dict

ItemName = str
ItemId = int
LocationName = str
LocationId = int
RegionName = str

ITEMS: List[LocationName] = ($items)

GEARS: List[LocationName] = ($gears)

BUNNIES: List[LocationName] = ($bunnies)

LOCATIONS: List[LocationName] = ($locations)

LOCATIONS_BY_REGION: Dict[RegionName, LocationName] = ($locations_by_region)

REGION_CONNECTIONS: Dict[RegionName, List[RegionName]] = ($region_connections)

ID_BY_LOCATION: Dict[LocationName, LocationId] = ($id_by_location)"
}

def "main items" [] {
    open map_infos.json
    | create_items
    | to json --indent 4
}

# generate a list of all gears from `map_infos.json`
def "main gears"  [] {
    open map_infos.json
    | create_gears
    | to json --indent 4
}

# generate a list of all bunnies from `map_info.json`
def "main bunnies"  [] {
    open map_infos.json
    | create_bunnies
    | to json --indent 4
}   

# generate a list of locations by region from `map_info.json`
def "main locations"  [] {
    open map_infos.json
    create_locations
    | to json --indent 4
}

# generate a list of locations by region from `map_info.json`
def "main regions-to-locations"  [] {
    open map_infos.json
    | create_locations_by_region
    | to json --indent 4
}

# generate a list of region to region connections
def "main region-connections" [] {
    open map_infos.json
    | create_region_connections
    | to json --indent 4
}

def create_gears [] {
    calculate_gears
    | get gears
    | flatten
    | sort --natural
}

def create_bunnies [] {
    calculate_bunnies
    | get bunnies
    | flatten
    | sort --natural
}

def create_locations [] {
    create_locations_by_region
    | transpose _ locations
    | get locations
    | flatten
    | sort --natural
}

def create_locations_by_region [] {
    calculate_gears
    | calculate_bunnies
    | each {|area|
        {
            k: $area.localAreaName,
            v: ($area.gears ++ $area.bunnies)
        }
    }
    | transpose -r --as-record
    | sort -n
    | update "Tosla Offices" { append "Golden Spring" }
    | update "Observing" { append "Golden Propeller" }
}

def create_id_by_location [] {
    create_locations
    | enumerate
    | select item index
    | update index { $in + $base_id }
    | transpose -r --as-record
}

def calculate_bunnies [] {
    update bunnyIds { sort }
    | insert bunnies {|area|
        $area.bunnyIds | each {|bunnyId|
            let levelName = match $area.localAreaName {
                "Granny's Island" => "Morio's Lab",
                "Morio's Home" => "Morio's Island",
                _ => $area.localLevelName
            }
            
            $"($levelName) | Bunny ($bunnyId + 1)"
        }
    }
}

def calculate_gears [] {
    update gearIds { sort }
    | insert gears {|area|
        $area.gearIds | enumerate | each {|gear|
            if ($area.gearIds | length) > 1 {
                $"($area.localAreaName) | Gear ($gear.index + 1)"
            } else {
                $"($area.localAreaName) | Gear"
            }
        }
    }
}

def gears_for_map [$map] {
    $map.gearIds | enumerate | each {|gear|
        if ($map.gearIds | length) > 1 {
            $"($map.localAreaName) | Gear ($gear.index + 1)"
        } else {
            $"($map.localAreaName) | Gear"
        }
    }
}

def create_items [] {
    [
        "Gear",
        "Bunny",
        "Golden Spring",
        "Golden Propeller",
    ]
}

def create_region_connections [] {
    {
        '400°': [
            'Pizza Time',
        ],
        '600°': [
            'Pizza Time',
        ],
        '900°': [
            'Pizza Time',
        ],
        'Anticipation': [
            "Morio's Lab",
            'Tosla HQ',
        ],
        'Arcade Panik': [
            "Morio's Lab",
            'Flipper',
        ],
        'Arcade Plaza': [
            "Morio's Lab",
            'Arcade Panik',
        ],
        'Bomb-it': [
            "Mosk's Rocket",
        ],
        'Bombeach': [
            "Morio's Lab",
            'Cave',
        ],
        'Buttons Smashing': [
            "Mosk's Rocket",
        ],
        'Cave': [
            'Bombeach',
        ],
        'Conveyor Belts': [
            "Mosk's Rocket",
        ],
        'Costipation': [
            "Mosk's Rocket",
        ],
        'Crash Again': [
            "Granny's Island",
        ],
        'Crash Test Industries': [
            "Morio's Lab",
            'Pipe-Zone',
        ],
        'Dreaming': [
            "Morio's Mind",
        ],
        'Eye surgery': [
            "Mosk's Rocket",
        ],
        'Far far away': [
            "Mosk's Rocket",
        ],
        'Fecal Matters': [
            "Granny's Island",
        ],
        'Flipper': [
            'Arcade Panik',
        ],
        'Flushed Away': [
            "Granny's Island",
        ],
        "Granny's Island": [
            "Morio's Lab",
            'Ice-Cream truck',
            'Law Firm',
            'Crash Again',
            'Pizza Oven',
            'Gym Gears',
            'Fecal Matters',
            'Flushed Away',
            'Moon',
            "Mosk's Rocket",
        ],
        'Gym Gears': [
            "Granny's Island",
        ],
        'Heroic Moves': [
            "Mosk's Rocket",
        ],
        'Ice-Cream truck': [
            "Granny's Island",
        ],
        'Infiltration': [
            "Mosk's Rocket",
        ],
        'Lab Memories': [
            "Mosk's Rocket",
        ],
        'Law Firm': [
            "Granny's Island",
        ],
        "Maurizio's City": [
            'Purple Tunnel',
        ],
        'Menu': [
            "Morio's Lab",
        ],
        'Mid air': [
            "Mosk's Rocket",
        ],
        'Moon': [
            "Granny's Island",
            'Spaceship',
        ],
        "Morio's Home": [
            "Morio's Island",
            'Weird Tunnels',
        ],
        "Morio's Island": [
            "Morio's Lab",
            "Morio's Home",
        ],
        "Morio's Lab": [
            "Granny's Island",
            "Morio's Island",
            'Bombeach',
            'Arcade Plaza',
            'Pizza Time',
            'Tosla Square',
            "Maurizio's City",
            'Crash Test Industries',
            "Morio's Mind",
            'Observing',
            'Anticipation'
        ],
        "Morio's Mind": [
            "Morio's Lab",
            'Dreaming',
        ],
        "Mosk's Rocket": [
            "Granny's Island",
            'Far far away',
            'Infiltration',
            'Mid air',
            'Eye surgery',
            'Conveyor Belts',
            'Heroic Moves',
            'Smelly Slimes',
            'Costipation',
            'Podium',
            'Stealthy',
            'Pepperoni',
            'Buttons Smashing',
            'Bomb-it',
            'Welcoming Climbs',
            'Lab Memories',
        ],
        'Observing': [
            "Morio's Lab",
            'The green place',
            'Rooftops',
        ],
        'Pepperoni': [
            "Mosk's Rocket",
        ],
        'Pipe-Zone': [
            'Crash Test Industries',
        ],
        'Pizza Oven': [
            "Granny's Island",
        ],
        'Pizza Time': [
            "Morio's Lab",
            '400°',
            '600°',
            '900°',
        ],
        'Podium': [
            "Mosk's Rocket",
        ],
        'Purple Tunnel': [
            "Maurizio's City",
        ],
        'Rooftops': [
            'Observing',
        ],
        'Smelly Slimes': [
            "Mosk's Rocket",
        ],
        'Spaceship': [
            "Granny's Island",
        ],
        'Stealthy': [
            "Mosk's Rocket",
        ],
        'The green place': [
            'Observing',
        ],
        'Tosla HQ': [
            "Morio's Lab", 'Moon',
        ],
        'Tosla Offices': [
            'Tosla Square',
        ],
        'Tosla Square': [
            "Morio's Lab",
            'Tosla Offices',
        ],
        'Weird Tunnels': [
            "Morio's Home",
        ],
        'Welcoming Climbs': [
            "Mosk's Rocket",
        ],
    }
}