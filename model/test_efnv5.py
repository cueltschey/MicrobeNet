import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def test_cnn_with_efficientnetv2(model, test_dir, input_shape, batch_size=32):
    test_datagen = ImageDataGenerator(rescale=1./255)

    test_generator = test_datagen.flow_from_directory(test_dir,
                                                      target_size=input_shape[:2],
                                                      batch_size=batch_size,
                                                      class_mode='categorical')

    # Evaluate the model on the test set
    evaluation = model.evaluate(test_generator, steps=test_generator.samples // batch_size)

    print(f"Test Loss: {evaluation[0]}, Test Accuracy: {evaluation[1]}")

# Example usage:
test_dir = '/media/chasuelt/MICROBES/testing_dataset/'

# Load the trained model (replace 'path/to/saved_model' with the actual path)
saved_model_path = '/media/chasuelt/MICROBES/model_v0'
trained_model = tf.keras.models.load_model(saved_model_path)
input_shape = (96,64,3)

# Test the model
test_cnn_with_efficientnetv2(trained_model, test_dir, input_shape)
