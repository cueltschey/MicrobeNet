import json
from utils import Downloader
import os
import random

d = Downloader()
results = list()

json_path = "/media/chasuelt/MICROBES/realmicrolife/"
finished_path = "/media/chasuelt/MICROBES/finished_json/"

def download_images(filename):
    with open(os.path.join(json_path, filename), "r") as f:
        results = json.load(f)
    os.rename(os.path.join(json_path, filename), os.path.join(finished_path, filename))


    desk_path = "/home/chasuelt/Desktop/microbe_images/"
    count = random.randint(500,1000) * 1000
    for item in results[3:]:
        count += 1
        genus = item["name"].replace(' ', '')
        print(f"Dowloading realmicro_{count}.jpg into folder {os.path.join(desk_path, genus)}")
        if item["image_url"][1:-1].split(".")[-1] in ["gif", ".gif", "GIF", ".GIF"]:
            d.download_gif(item["image_url"], os.path.join(desk_path, genus), f"realmicro_{count}.jpg")
        else:
            d.download_jpg(item["image_url"], os.path.join(desk_path, genus), f"realmicro_{count}.jpg")
        
for filename in os.listdir(json_path):
    if filename.split(".")[1] != "json":
        continue
    download_images(filename)


