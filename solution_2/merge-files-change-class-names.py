# importing json module

import json

# let's define our input files in an array

file_dir = ["input/pos_0.png.json", "input/pos_10010.png.json", "input/pos_10492.png.json"]

# json file merge function


def merge_json(files):
    result = []
    for file in files:
        with open(file, "r") as input_file:
            result.append(json.load(input_file))

    # iterating items to modify "clssTitle" values

    for item in result:
        for obj in item["objects"]:
            if obj["classTitle"] == "Vehicle":
                obj["classTitle"] = "Car"
            elif obj["classTitle"] == "License Plate":
                obj["classTitle"] = "Number"

    # Writing to the merged_file in output folder

    with open("output/merged_file.json", "w") as output_file:
        json.dump(result, output_file, indent=4)


merge_json(file_dir)
