import json
from utils import Downloader
import os

d = Downloader()
results = list()

with open("inaturalist.json", "r") as f:
    results = json.load(f)


desk_path = "C:\\Users\\paige\\Desktop\\microbe_images"
count = 200
for item in results:
    count += 1
    genus = ""
    if item["name"].split(" ")[0] == "Genus":
        genus = item["name"].split(" ")[1]
    else:
        genus = item["name"].split(" ")[0]

    d.download_image(item["image_url"][1:-1], os.path.join(desk_path, genus), f"inaturalist_{count}.jpg")
    

