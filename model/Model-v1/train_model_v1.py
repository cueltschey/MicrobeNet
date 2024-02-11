import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator



def train_model_v1(train_generator):
    model = models.Sequential()

# First Convolutional Layer
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(200, 200, 3)))
    model.add(layers.MaxPooling2D((2, 2)))

# Second Convolutional Layer
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))

# Third Convolutional Layer
    model.add(layers.Conv2D(128, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))

# Fourth Convolutional Layer
    model.add(layers.Conv2D(256, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))

# Fifth Convolutional Layer
    model.add(layers.Conv2D(512, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))

# Flatten Layer
    model.add(layers.Flatten())

# Dropout Layer for Regularization
    model.add(layers.Dropout(0.5))

# First Fully Connected Layer
    model.add(layers.Dense(512, activation='relu'))

# Second Fully Connected Layer
    model.add(layers.Dense(256, activation='relu'))

# Output Layer
    model.add(layers.Dense(600, activation='softmax'))

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    history = model.fit(
        train_generator,
        epochs=10
    )
    model.summary()
# Save the trained model
    model.save('trained_model.h5')

# Evaluate the model
    loss, accuracy = model.evaluate(train_generator)
    print(f'Training accuracy: {accuracy * 100:.2f}%')
    model.save("/media/chasuelt/MICROBES/Model-v1")
    return accuracy, loss

# Define the directory containing your images
train_dir = '/media/chasuelt/MICROBES/training_dataset/'

# Define parameters
batch_size = 204
img_height = 200
img_width = 200
epochs = 10

# Create data generator for training data
train_datagen = ImageDataGenerator(rescale=1./255)

# Load images from the directory and apply data augmentation
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='sparse')

train_model_v1(train_generator)




