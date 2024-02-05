from PIL import Image
import os


def process_images(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    files = os.listdir(input_dir)
    if "pis" in files[0] and len(files) > 12:
        files = files[:-11]
    if len(files) < 68:
        return

    for file_name in files[:68]:
        input_path = os.path.join(input_dir, file_name)

        # Original image
        original_output_path = os.path.join(output_dir, file_name)
        vertical_flip_output_path = os.path.join(output_dir, f"vertical_flip_{file_name}")
        horizontal_flip_output_path = os.path.join(output_dir, f"horizontal_flip_{file_name}")
        try:
            with Image.open(input_path) as img:
                width, height = img.size
                if width < 96 or height < 64 or img.format != "JPEG":
                    continue
                img.thumbnail((96, 64))
                img.save(original_output_path)
                img = img.transpose(Image.FLIP_TOP_BOTTOM)
                img.save(vertical_flip_output_path)
                img = img.transpose(Image.FLIP_LEFT_RIGHT)
                img.save(horizontal_flip_output_path)
        except:
            print("Error occured with file ", file_name)


if __name__ == "__main__":
    input_base = "/media/chasuelt/MICROBES/microbe_images/"
    output_base = "/media/chasuelt/MICROBES/processed_images/"
    count = 0
    for directory in os.listdir(input_base):
        count += 1
        print(f"Processing genus {directory} index {count} --> {os.path.join(output_base, directory)}")
        process_images(os.path.join(input_base, directory), os.path.join(output_base, directory))
