#!/usr/bin/env python3
import json
import csv
import os
import time

# List of all keys from json files
key_list = ["file_path"]
# List of json. Every element is a json dictionary
json_list = []
# Current json selected
current_json = {}
# Extension of json file
json_extension = ".json"
# Name of csv file that will be created in the current directory
csv_file_name = "final_case_sensitive.csv"

# The program measure the execution time. That's the start
start_time = time.time()

# Start from the current directory.
# Find every json file in the subdirectories, save all the keys (with duplicates) and the content of json files.
# IMPORTANT: skip (key,value) pairs if value is a list
for paths, subdirs, files in os.walk("."):
    for file in files:
        file_path = os.path.join(paths, file)
        filename, file_extension = os.path.splitext(file_path)
        if file_extension == json_extension:
            # Uncomment this print to see in the terminal the json that is about to be examined
            # print(file_path)
            with open(file_path) as json_file:
                json_content = json.load(json_file)
                current_json = {}
                file_path_fixed = ""
                for key, value in json_content.items():
                    key_list.append(key)
                    if isinstance(value, list):
                        continue
                    current_json[key] = value
                file_path_fixed = file_path[2:]
                file_path_fixed = file_path_fixed[:-5].replace("/", "//")
                current_json["file_path"] = file_path_fixed
                json_list.append(current_json)

print("Number of columns with duplicates: " + str(len(key_list)))

# Cut duplicates
key_list = list(dict.fromkeys(key_list))

print("Number of columns without duplicates: " + str(len(key_list)))

print("Number of rows: " + str(len(json_list) + 1))

# That's useful for my project. It moves "file_path" and "<page title>" in front of key_list.
# If you are not me, skip this one. If you are me, damn you are awesome!
key_list.insert(0, key_list.pop(key_list.index("<page title>")))
key_list.insert(0, key_list.pop(key_list.index("file_path")))

print("Writing file " + csv_file_name)

# Write a single csv file with the content of every json found
with open(csv_file_name, mode='w') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=key_list)
    csv_writer.writeheader()
    for i in range(0, len(json_list)):
        csv_writer.writerow(json_list[i])

# And that's the end of the time counter
stop_time = time.time()

print("Execution completed. Yey. It took " +
      str("%.2f" % round((stop_time - start_time), 2)) + " seconds or, if you prefer, " +
str("%.2f" % round(((stop_time - start_time) / 60), 2)) + " minutes")
