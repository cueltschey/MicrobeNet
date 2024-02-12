import os
import requests
import json
import random


def download_jpg(url, folder_path, filename):
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)
    response = requests.get(url, stream=True)
    with open(os.path.join(folder_path, filename), 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)


output_dir = "/mnt/c/Users/paige/Desktop/microbe_images/"
input_dir = "/mnt/c/Users/paige/Desktop/json_finished/"

name_count = random.randint(300, 1000)

for json_file in os.listdir(input_dir):
    iter_count = 0
    json_data = list()
    with open(os.path.join(input_dir, json_file), "r") as f:
        json_data = json.load(f)
    print(f"\n\nDownloading from: {json_file} #{iter_count}\n\n")

    for item in json_data:
        iter_count += 1
        if 'Z' in item["image_url"].split("/"):
            print("Downloading: ", item["name"])
            download_jpg(item["image_url"].replace("Z", "C"), os.path.join(output_dir, json_file[:-5]), f"pis_{name_count + iter_count}.jpg")
        else:
            print("Skipping: ", item["name"])
