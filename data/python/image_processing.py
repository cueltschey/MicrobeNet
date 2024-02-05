from PIL import Image
import os



def process_images(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    files = os.listdir(input_dir)

    for file_name in files:
        input_path = os.path.join(input_dir, file_name)

        # Original image
        original_output_path = os.path.join(output_dir, file_name)
        resize_image(input_path, original_output_path)

        # Vertically flipped image
        vertical_flip_output_path = os.path.join(output_dir, f"vertical_flip_{file_name}")
        with Image.open(input_path) as img:
            img = img.transpose(Image.FLIP_TOP_BOTTOM)
            img.thumbnail((96, 96))
            img.save(vertical_flip_output_path)

        # Horizontally flipped image
        horizontal_flip_output_path = os.path.join(output_dir, f"horizontal_flip_{file_name}")
        with Image.open(input_path) as img:
            img = img.transpose(Image.FLIP_LEFT_RIGHT)
            img.thumbnail((96, 96))
            img.save(horizontal_flip_output_path)

if __name__ == "__main__":
    input_directory = "input_images"
    output_directory = "output_images"

    # Process the images
    process_images(input_directory, output_directory)
