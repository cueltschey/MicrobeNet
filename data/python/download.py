import json
from utils import Downloader
import os
import random

d = Downloader()
results = list()

json_path = "../"

def download_images(filename):
    with open(os.path.join(json_path, filename), "r") as f:
        results = json.load(f)


    desk_path = "../../../microbe_images/"
    count = random.randint(0,200) * 100
    for item in results:
        count += 1
        genus = ""
        if item["name"].split(" ")[0] == "Genus":
            genus = item["name"].split(" ")[1]
        else:
            genus = item["name"].split(" ")[0]
        print(f"Dowloading inaturalist_{count}.jpg into folder {os.path.join(desk_path, genus)}")

        d.download_image(item["image_url"][1:-1], os.path.join(desk_path, genus), f"inaturalist_{count}.jpg")
        
for filename in os.listdir(json_path):
    download_images(filename)


