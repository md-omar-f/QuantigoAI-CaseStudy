# importing json module

import json

# opening the json file from a folder

with open("input/pos_10010.png.json", "r") as input_file:
    data = json.load(input_file)

# deleting the objects with "classTitle" other than "Vehicle" and "License Plate"

    for obj in data["objects"]:
        if obj["classTitle"] != "Vehicle" and obj["classTitle"] != "License Plate":
            data["objects"].remove(obj)

# Writing data the output file in output folder

with open("output/formatted_pos_0.png.json", "w") as output_file:
    json.dump(data, output_file, indent=4)
