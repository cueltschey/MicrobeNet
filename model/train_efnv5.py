import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, models
import keras_cv
import keras_core as keras
import numpy as np


def create_efficientnetv2_model(input_shape, num_classes):
    base_model = keras_cv.models.EfficientNetV2Backbone.from_preset(
    "efficientnetv2_b0"
    )

    # Freeze the pre-trained weights
    base_model.trainable = False

    model = models.Sequential([
        layers.Input(shape=input_shape),
        base_model,
        layers.Flatten(),
        layers.Dense(256, activation='relu'),
        layers.Dropout(0.5),
        layers.Dense(num_classes, activation='softmax')
    ])

    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    return model

def train_cnn_with_efficientnetv2(train_dir, validation_dir, input_shape, num_classes, epochs=10, batch_size=32):
    train_datagen = ImageDataGenerator(rescale=1./255,
                                       shear_range=0.2,
                                       zoom_range=0.2,
                                       horizontal_flip=True)

    test_datagen = ImageDataGenerator(rescale=1./255)

    train_generator = train_datagen.flow_from_directory(train_dir,
                                                        target_size=input_shape[:2],
                                                        batch_size=batch_size,
                                                        class_mode='categorical')

    validation_generator = test_datagen.flow_from_directory(validation_dir,
                                                            target_size=input_shape[:2],
                                                            batch_size=batch_size,
                                                            class_mode='categorical')

    model = create_efficientnetv2_model(input_shape, num_classes)

    model.fit(train_generator,
              steps_per_epoch=train_generator.samples // batch_size,
              epochs=epochs,
              validation_data=validation_generator,
              validation_steps=validation_generator.samples // batch_size)

    return model

# Example usage:
train_dir = '/media/chasuelt/MICROBES/training_dataset/'
validation_dir = '/media/chasuelt/MICROBES/validation_dataset/'
input_shape = (96, 64, 3)  # Adjust based on your image size and channels
num_classes = 170  # Adjust based on the number of categories

trained_model = train_cnn_with_efficientnetv2(train_dir, validation_dir, input_shape, num_classes)
trained_model.save("/media/chasuelt/MICROBES/model_v0")
