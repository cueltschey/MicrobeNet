import os
import json
from PIL import Image



def find_few():
    for directory in os.listdir("../../../microbe_images/"):
        count = 0
        for file in os.listdir(os.path.join("../../../microbe_images/",directory)):
            count += 1
        if count < 30 and directory != "few":
            print(directory, count)
            os.rename(os.path.join("../../../microbe_images/", directory), os.path.join("../../../microbe_images/few", directory))

def find_some():
    for directory in os.listdir("../../../microbe_images/"):
        count = 0
        for file in os.listdir(os.path.join("../../../microbe_images/",directory)):
            count += 1
        if count < 100 and directory != "30-100":
            print(directory, count)
            os.rename(os.path.join("../../../microbe_images/", directory), os.path.join("../../../microbe_images/30-100", directory))

def find_many():
    for directory in os.listdir("../../../microbe_images/"):
        count = 0
        for file in os.listdir(os.path.join("../../../microbe_images/",directory)):
            count += 1
        if count >= 100 and directory not in ["100-over","30-100", "0-30"]:
            print(directory, count)
            os.rename(os.path.join("../../../microbe_images/", directory), os.path.join("../../../microbe_images/100-over", directory))

def delete_EDMS():
    for directory in os.listdir("/media/chasuelt/MICROBES/microbe_images/"):
        for file in os.listdir(os.path.join("/media/chasuelt/MICROBES/microbe_images/", directory)):
            if file[:4] == "EMDS":
                os.remove(os.path.join("/media/chasuelt/MICROBES/microbe_images/", directory, file))


def delete_small_images(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            try:
                with Image.open(filepath) as img:
                    width, height = img.size
                    if width < 96 or height < 64:
                        os.remove(filepath)
                        print(f"Deleted: {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")



total = 0
for directory in os.listdir("/media/chasuelt/MICROBES/microbe_images/"):
    count = 0
    delete_small_images(os.path.join("/media/chasuelt/MICROBES/microbe_images/", directory))
    for file in os.listdir(os.path.join("/media/chasuelt/MICROBES/microbe_images/", directory)):
        count += 1
        total += 1
    print(directory, count)

print("Total: ", total)
