import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import fashion_mnist

# 1. Load data
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

# 2. Normalize
x_train = x_train / 255.0
x_test = x_test / 255.0

# 3. Expand dims for CNN input
x_train = x_train[..., tf.newaxis]
x_test = x_test[..., tf.newaxis]

# 4. Define model
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')  # 10 categories
])

# 5. Compile and train
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

# 6. Save model
model.save("fashion_model.h5")
print("✅ Model saved as fashion_model.h5")
