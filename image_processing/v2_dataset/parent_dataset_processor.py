import os
from PIL import Image

def resize_and_copy(input_dir, output_dir, target_size=(200, 200)):

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # List all files in the input directory
    files = os.listdir(input_dir)

    for file_name in files:
        input_path = os.path.join(input_dir, file_name)
        output_path = os.path.join(output_dir, file_name)
        output_path_v = os.path.join(output_dir, "vertical_" + file_name)
        output_path_h = os.path.join(output_dir, "horizontal_" + file_name)
        print(file_name)
        # Open the image file
        with Image.open(input_path) as img:
            width, height = img.size
            if width < 200 or height < 200:
                print("Too Small")
                continue
            if img.mode == "P" or img.mode == "RGBA":
                print("Wrong Mode")
                continue
            # Resize the image
            img_resized = img.resize(target_size, Image.ANTIALIAS)
            img_vertical = img_resized.transpose(Image.FLIP_TOP_BOTTOM)
            img_horizontal = img_resized.transpose(Image.FLIP_LEFT_RIGHT)

            # Save the resized image
            img_resized.save(output_path)
            img_vertical.save(output_path_v)
            img_horizontal.save(output_path_h)

if __name__ == "__main__":
    input_base = "/media/chasuelt/MICROBES/organized/"
    output_base = "/media/chasuelt/MICROBES/training_dataset/"
    target_size = (200, 200)
    for directory_name in os.listdir(input_base):
        for sub_dirname in os.listdir(os.path.join(input_base, directory_name)):
            try:
                resize_and_copy(os.path.join(input_base, directory_name, sub_dirname), os.path.join(output_base, directory_name), target_size)
            except:
                print("fail")
                continue
