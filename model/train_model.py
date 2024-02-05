import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

def create_cnn_model(input_shape, num_classes):
    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=input_shape))
    model.add(MaxPooling2D((2, 2)))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2, 2)))
    model.add(Conv2D(128, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2, 2)))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dense(num_classes, activation='softmax'))
    
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    
    return model

def train_cnn(train_dir, validation_dir, input_shape, num_classes, epochs=10, batch_size=32):
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

    model = create_cnn_model(input_shape, num_classes)

    model.fit(train_generator,
              steps_per_epoch=train_generator.samples // batch_size,
              epochs=epochs,
              validation_data=validation_generator,
              validation_steps=validation_generator.samples // batch_size)

# Example usage:
train_dir = '/path/to/train_data'
validation_dir = '/path/to/validation_data'
input_shape = (96, 96, 3)  # Set the desired image size
num_classes = 10  # Adjust based on the number of categories

train_cnn(train_dir, validation_dir, input_shape, num_classes)
