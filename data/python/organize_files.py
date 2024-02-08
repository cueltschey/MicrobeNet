import os
import json



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


total = 0
for directory in os.listdir("/mnt/c/Users/paige/Desktop/microbe_images/"):
    count = 0
    for file in os.listdir(os.path.join("/mnt/c/Users/paige/Desktop/microbe_images/", directory)):
        count += 1
        total += 1
    print(directory, count)

print("Total: ", total)
