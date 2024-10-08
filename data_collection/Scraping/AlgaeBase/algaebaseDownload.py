import json
from utils import Downloader
import os
import random

d = Downloader()
results = list()

json_path = "/mnt/c/Users/paige/Desktop/algaebase/"
finished_path = "/mnt/c/Users/paige/Desktop/finished/"

def download_images(filename):
    with open(os.path.join(json_path, filename), "r") as f:
        results = json.load(f)
    os.rename(os.path.join(json_path, filename), os.path.join(finished_path, filename))


    desk_path = "/mnt/c/Users/paige/Desktop/microbe_images/"
    count = random.randint(0,500) * 1000
    for item in results:
        if item == '':
            continue
        count += 1
        print(f"Dowloading v1_{count}.jpg into folder {os.path.join(desk_path, filename[:-5])}")
        print(item)
        if item[1:-1].split(".")[-1] in ["gif", ".gif", "GIF", ".GIF"]:
            d.download_gif(item[1:-1], os.path.join(desk_path, filename[:-5]), f"v1_{count}.jpg")
        else:
            d.download_jpg(item[1:-1], os.path.join(desk_path, filename[:-5]), f"v1_{count}.jpg")
        
for filename in os.listdir(json_path):
    download_images(filename)


