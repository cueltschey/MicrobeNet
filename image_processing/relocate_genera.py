import os
import json


info = None

with open("/media/chasuelt/MICROBES/index.json", "r") as f:
    info = json.load(f)

good = 0
bad = 0

def sort_by_category(dirname, category):
    for file in os.listdir(dirname):
        try:
            if not os.path.exists(os.path.join(dirname, info[file][category])):
                os.mkdir(os.path.join(dirname, info[file][category]))
            os.rename(os.path.join(dirname, file), os.path.join(dirname, info[file][category], file))
            print(file, "moved")
        except:
            print("fail")


# sort_by_category("/home/chasuelt/Desktop/Backup_Images/Eukaryota/", "kingdom")
