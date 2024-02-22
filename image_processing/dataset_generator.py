import os
import shutil

def unpack_dataset(input_dir, output_dir):
    # Ensure output directory exists, create if not
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Traverse the input directory
    for root, _, files in os.walk(input_dir):
        for file in files:
            # Get the full path of the file
            file_path = os.path.join(root, file)
            if ".git" in file_path:
                continue
            # Copy the file to the output directory
            if not os.path.isdir(file_path):
                print("copying: ", file_path, "to ", output_dir)
                shutil.copy2(file_path, output_dir)

def resize_and_copy(input_dir, output_dir, target_size=(200, 200)):

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # List all files in the input directory
    files = os.listdir(input_dir)

    if len(files) < 200:
        print("driectory is too small: ", input_dir)
        return

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


outdir = "/home/chasuelt/dataset"
indir = "/home/chasuelt/original_images"

for directory in os.listdir(indir):
    resize_and_copy(os.path.join(indir, directory), os.path.join(outdir, directory))
