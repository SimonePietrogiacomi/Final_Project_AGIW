#!/usr/bin/env python3
import json
import os
from ast import literal_eval
import csv


key_list = ["instance0", "instance1"]
with open("entities_fixed.json") as entities:
    with open("gt.csv", mode='w') as gt:
        csv_writer = csv.writer(gt, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(key_list)
        entities_list = []
        for entity_row in entities:
            current_entity_row = literal_eval(entity_row)
            instance0 = current_entity_row["instances"][0]
            for instance in current_entity_row["instances"]:
                if instance:
                    if instance != instance0 and (instance != "www.ukdigitalcameras.co.uk//288" and instance != "www.ukdigitalcameras.co.uk//257"):
                        csv_writer.writerow([instance0, instance])
                        instance0 = instance
