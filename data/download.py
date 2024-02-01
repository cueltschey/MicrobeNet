import json
from utils import Downloader

download = Downloader()



results = list()

with open("inaturalist.json", "r") as f:
    results = json.load(f)


desk_path = "C:\\Users\\paige\\Desktop\\microbe_images"
count = 0
for item in results:
    count += 1
    genus = ""
    if item["name"].split(" ")[0] == "Genus":
        genus = item["name"].split(" ")[1]
    else:
        genus = item["name"].split(" ")[0]

    download.download_image(item["image_url"], desk_path, f"{genus}\\inaturalist_{count}")


