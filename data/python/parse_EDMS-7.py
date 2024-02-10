import os

names_map = {

        }

for file in os.listdir("/media/chasuelt/MICROBES/EMDS7/"):
    #os.rename(os.path.join("/media/chasuelt/MICROBES/EMDS7/", file), os.path.join("/media/chasuelt/MICROBES/microbe_images/", names[file.split()]))
    print(file.split("-")[1])
