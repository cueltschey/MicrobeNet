import os
import json


info = None

with open("/media/chasuelt/MICROBES/index.json", "r") as f:
    info = json.load(f)

good = 0
bad = 0

def sort_by_category(dirname, category):
    successful = 0
    size = len(os.listdir(dirname))
    for file in os.listdir(dirname):
        if "phylum" in file:
            sort_by_category(os.path.join(dirname, file), "class")
        try:
            if not os.path.exists(os.path.join(dirname, f"{category}_" + info[file][category])):
                os.mkdir(os.path.join(dirname, f"{category}_" + info[file][category]))
            os.rename(os.path.join(dirname, file), os.path.join(dirname, f"{category}_" + info[file][category], file))
            print(file, "moved")
            successful += 1
        except:
            print("fail")
    print(f"Stats: {(successful / size) * 100}%")


def unpack_dir(dirname):
    size = len(os.listdir(dirname))
    for file in os.listdir(dirname):
        print(file)
        for subfile in os.listdir(os.path.join(dirname, file)):
            if os.path.isdir(os.path.join(dirname, file, subfile)):
                print(file, "moved")
                os.rename(os.path.join(dirname, file, subfile), os.path.join(dirname, file, "..", subfile))

sort_by_category("/home/chasuelt/Desktop/Backup_Images/superkingdom_Eukaryota/", "class")
#unpack_dir("/home/chasuelt/Desktop/Backup_Images/Eukaryota")
#unpack_dir("/home/chasuelt/Desktop/Backup_Images/")
