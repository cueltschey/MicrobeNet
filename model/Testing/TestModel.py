import tensorflow as tf
import numpy as np
import cv2
import os

class ModelTester:
    def __init__(self, model_path):
        self.model = tf.keras.models.load_model(model_path)
        self.input_shape = self.model.input_shape[1:3]

    def preprocess_image(self, image_path):
        img = cv2.imread(image_path)
        img = cv2.resize(img, self.input_shape)
        img = img / 255.0  # Normalize pixel values to [0, 1]
        img = np.expand_dims(img, axis=0)  # Add batch dimension
        return img

    def test_image(self, image_path):
        preprocessed_img = self.preprocess_image(image_path)
        prediction = self.model.predict(preprocessed_img)
        return prediction

    def get_classifications_from_directory(self, training_dir):
        classifications = []
        for root, dirs, files in os.walk(training_dir):
            for d in dirs:
                classifications.append(d)
        classifications.sort()  # Sort the list alphabetically
        return classifications


if __name__ == "__main__":
    model_path = "/home/chasuelt/Desktop/Trained_Models/MicrobeNetV2/MicrobeNetV2P.h5"
    image_path = "/media/chasuelt/MICROBES/organized/colonial/"
    training_dir = "/media/chasuelt/MICROBES/v1-datasets/training_dataset/"
    
    correct = 0
    count = 0
    local_stats = list()
    tester = ModelTester(model_path)
    categories = tester.get_classifications_from_directory(training_dir)
    for dirname in os.listdir(image_path):
        local_correct = 0
        for image_name in os.listdir(os.path.join(image_path, dirname)):
            prediction = tester.test_image(os.path.join(image_path, dirname, image_name))
            count += 1
            print("Prediction:", categories[np.argmax(prediction)])
            if categories[np.argmax(prediction)] == "colonial":
                correct += 1
                local_correct += 1
        local_stats.append(local_correct / len(os.listdir(os.path.join(image_path, dirname))))
        print(f"\n\n\n{local_stats}\n\n\n")
    print(f"Accuracy: {correct / count}")
