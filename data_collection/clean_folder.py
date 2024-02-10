import os

def is_small(image_path):
    print(image_path, os.path.getsize(image_path))
    return os.path.getsize(image_path) <= 22122

def delete_trash(folder_path):
    import os

    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            image_path = os.path.join(folder_path, filename)
            if is_small(image_path):
                os.remove(image_path)
                print(f"Deleted grayscale image: {filename}")



for directory in os.listdir("../../../microbe_images/"):
    delete_trash(os.path.join("../../../microbe_images/", directory))
