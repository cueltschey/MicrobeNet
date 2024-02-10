import os
import shutil


training_names = os.listdir("/media/chasuelt/MICROBES/training_dataset/")
validation_names = list()

for name in os.listdir("/media/chasuelt/MICROBES/validation_dataset/"):
    if name not in training_names:
        shutil.rmtree(os.path.join("/media/chasuelt/MICROBES/validation_dataset/", name))
    validation_names.append(name)

difference = [name for name in training_names if name not in validation_names]
print(difference)
