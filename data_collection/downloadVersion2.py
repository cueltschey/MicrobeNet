import json
from utils import Downloader
import os
import random

d = Downloader()
results = list()

json_path = "/media/chasuelt/MICROBES/inaturalist/"
finished_path = "/media/chasuelt/MICROBES/finished_json/"

def download_images(filename):
    with open(os.path.join(json_path, filename), "r") as f:
        results = json.load(f)
    os.rename(os.path.join(json_path, filename), os.path.join(finished_path, filename))


    desk_path = "/media/chasuelt/MICROBES/microbe_images/"
    count = random.randint(0,500) * 1000
    for item in results[3:]:
        count += 1
        genus = ""
        if item["name"].split(" ")[0] == "Genus":
            genus = item["name"].split(" ")[1]
        else:
            genus = item["name"].split(" ")[0]
        print(f"Dowloading v1_{count}.jpg into folder {os.path.join(desk_path, filename[:-5])}")
        if item["image_url"][1:-1].split(".")[-1] in ["gif", ".gif", "GIF", ".GIF"]:
            d.download_gif(item["image_url"][1:-1], os.path.join(desk_path, filename[:-5]), f"v1_{count}.jpg")
        else:
            d.download_jpg(item["image_url"][1:-1], os.path.join(desk_path, filename[:-5]), f"v1_{count}.jpg")
        
for filename in os.listdir(json_path):
    if filename == "python" or filename == "__pycache__":
        continue
    download_images(filename)


