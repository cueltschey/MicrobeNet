import json
from utils import Downloader
import os
import random

d = Downloader()
results = list()

json_path = "/mnt/c/Users/paige/Desktop/inaturalist/"
finished_path = "/mnt/c/Users/paige/Desktop/finished/"

def download_images(filename):
    with open(os.path.join(json_path, filename), "r") as f:
        results = json.load(f)
    os.rename(os.path.join(json_path, filename), os.path.join(finished_path, filename))


    desk_path = "/mnt/c/Users/paige/Desktop/microbe_images/"
    count = random.randint(0,500) * 1000
    for item in results[3:]:
        count += 1
        genus = ""
        if item["name"].split(" ")[0] == "Genus":
            genus = item["name"].split(" ")[1]
        else:
            genus = item["name"].split(" ")[0]
        print(f"Dowloading v1_{count}.jpg into folder {os.path.join(desk_path, filename[:-5])}")

        d.download_image(item["image_url"][1:-1], os.path.join(desk_path, filename[:-5]), f"v1_{count}.jpg")
        
for filename in os.listdir(json_path)[3:]:
    if filename == "python" or filename == "__pycache__":
        continue
    download_images(filename)


