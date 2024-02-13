import os
from PIL import Image


stats_dir = "/mnt/c/Users/paige/Desktop/old_microbe_images/"
total_viable = 0
total_percent = 0
total = 0
for dirname in os.listdir(stats_dir):
    viable_images_count = 0
    count = 0
    for filename in os.listdir(os.path.join(stats_dir, dirname)):
        count += 1
        file = os.path.join(stats_dir, dirname, filename)
        with Image.open(file) as img:
            width, height = img.size
            if width >= 200 and height >= 200:
                viable_images_count += 1
    viable_percent = (viable_images_count / count) * 100
    total += count
    total_percent += viable_percent
    total_viable += viable_images_count
    print(f"{dirname}: Viable({viable_images_count}) {viable_percent}%\n")

total_percent /= len(os.listdir(stats_dir))
print(f"\n\nTotal: Viable:{total_viable} {total_percent}% Total:{total}\n\n")

