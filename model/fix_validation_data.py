import os
import shutil


training_names = os.listdir("/media/chasuelt/MICROBES/training_dataset/")

for name in os.listdir("/media/chasuelt/MICROBES/validation_dataset/"):
    if name not in training_names:
        shutil.rmtree(os.path.join("/media/chasuelt/MICROBES/validation_dataset/", name))
