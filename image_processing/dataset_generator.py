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
                print("copying: ", file_path, "to ", output_directory)
                shutil.copy2(file_path, output_directory)
