import json
import pkgutil

location_table = json.loads(pkgutil.get_data(__name__, "locations.json"))

lookup_id_to_name = {}
for item in location_table:
    lookup_id_to_name[item["id"]] = item["name"]

lookup_id_to_name[None] = "Utopia Complete"
lookup_name_to_id = {name: id for id, name in lookup_id_to_name.items()}