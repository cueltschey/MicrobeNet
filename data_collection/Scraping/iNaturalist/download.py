import json
from utils import Downloader
import os
import random

d = Downloader()
results = list()

json_path = "/mnt/c/Users/chase ueltschey/Desktop/json_three/"

def download_images(filename):
    with open(os.path.join(json_path, filename), "r") as f:
        results = json.load(f)


    desk_path = "/mnt/c/Users/chase ueltschey/Desktop/microbe_images/"
    count = random.randint(0,200) * 100
    for item in results[3:]:
        count += 1
        genus = ""
        if item["name"].split(" ")[0] == "Genus":
            genus = item["name"].split(" ")[1]
        else:
            genus = item["name"].split(" ")[0]
        print(f"Dowloading inaturalist_{count}.jpg into folder {os.path.join(desk_path, filename[:-5])}")

        d.download_image(item["image_url"], os.path.join(desk_path, filename[:-5]), f"pis_{count}.jpg")
        
for filename in os.listdir(json_path):
    if filename == "python" or filename == "__pycache__":
        continue
    download_images(filename)


