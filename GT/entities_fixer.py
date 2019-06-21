#!/usr/bin/env python3
import json
import os
from ast import literal_eval

jr = {}
with open("json_files.json") as json_files:
    for json_file_row in json_files:
        current_json_file_row = literal_eval(json_file_row)
        jr[current_json_file_row["resource_id"]] = str(current_json_file_row["source_name"]) + "//" + \
                                                   str(current_json_file_row["json_number"])

new_instances = []
with open("entities.json") as entities:
    with open("entities_fixed.json", mode='w') as fixed_entities:
        for entity_row in entities:
            current_entity_row = literal_eval(entity_row)
            instances = current_entity_row["instances"]
            new_instances = []
            for instance in instances:
                new_instances.append(jr[instance])
            current_entity_row["instances"] = new_instances
            fixed_entities.write(json.dumps(current_entity_row))
            fixed_entities.write("\n")
