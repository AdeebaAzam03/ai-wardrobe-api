def get_recommendations(weather, wardrobe):
    if weather == "sunny":
        return ["Sunglasses & T-shirt", "Floral Dress", "Linen Pants"]
    elif weather == "rainy":
        return ["Raincoat & Boots", "Waterproof Jacket"]
    else:
        return ["Hoodie", "Jeans", "Basic T-shirt"]
