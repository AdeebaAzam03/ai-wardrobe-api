from tensorflow.keras.models import load_model
import numpy as np

# Load once globally
model = load_model("fashion_model.h5")

# Labels for Fashion-MNIST
labels = ['T-shirt', 'Trouser', 'Pullover', 'Dress', 'Coat',
          'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

def get_recommendations(weather, wardrobe):
    # This is just a demo logic
    output = []

    for item in wardrobe:
        item_name = item.get('name', '').lower()

        if 'shirt' in item_name and 'sun' in weather:
            output.append("T-shirt and jeans for sunny day")

    # You can modify this later to use model.predict()
    return output

def get_recommendations(weather, wardrobe):
    basic_outfit = []
    accessories = []

    wardrobe_items = [item['name'].lower() for item in wardrobe]

    # Add main clothing logic based on weather (already existing)

    # Accessories logic
    if 'shoes' not in wardrobe_items:
        accessories.append({
            'item': 'Stylish Shoes',
            'link': 'https://www.amazon.in/s?k=stylish+shoes'
        })

    if 'watch' not in wardrobe_items:
        accessories.append({
            'item': 'Smart Watch',
            'link': 'https://www.amazon.in/s?k=smart+watch'
        })

    # Return both outfits and accessories
    return {
        'outfits': basic_outfit,
        'accessories': accessories
    }
