from tensorflow.keras.models import load_model
import numpy as np
from tensorflow.keras.datasets import fashion_mnist

# 1. Load the trained model
model = load_model("fashion_model.h5")

# 2. Load test dataset
(_, _), (x_test, y_test) = fashion_mnist.load_data()

# 3. Normalize and reshape test data
x_test = x_test / 255.0
x_test = x_test[..., np.newaxis]

# 4. Predict on first 5 samples
predictions = model.predict(x_test[:5])

# 5. Display predictions
for i in range(5):
    predicted_label = np.argmax(predictions[i])
    actual_label = y_test[i]
    print(f"🧠 Prediction: {predicted_label}, 🎯 Actual: {actual_label}")
