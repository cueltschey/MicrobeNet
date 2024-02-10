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

        # Open the image file
        with Image.open(input_path) as img:
            # Resize the image
            img_resized = img.resize(target_size, Image.ANTIALIAS)

            # Save the resized image
            img_resized.save(output_path)

if __name__ == "__main__":
    # Input directory containing original images
    input_dir = "/media/chasuelt/MICROBES/microbe_images"

    # Output directory to store resized images
    output_dir = "/path/to/resized_images"

    # Target size for resized images
    target_size = (200, 200)

    # Resize and copy images
    resize_and_copy(input_dir, output_dir, target_size)
