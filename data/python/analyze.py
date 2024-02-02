import json
import os

analysis = list()

def get_length(directory, file):
    filepath = os.path.join(directory, file)
    data = list()
    with open(filepath, "r") as f:
        data = json.load(f)
    count = 0
    for item in data:
        count += 1
    print(filepath, count)
    analysis.append({filepath:count})
    return count

directory = os.getcwd()
total = 0

for filename in os.listdir(directory):
    if len(filename.split(".")) < 2:
        continue
    if filename.split(".")[1] == "json":
      total += get_length(directory, filename)

print("Total images: ", total)




    
