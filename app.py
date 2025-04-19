from flask import Flask, request, jsonify
from outfit_recommender import get_recommendations

app = Flask(__name__)

@app.route('/')
def home():
    return "AI Wardrobe API Running!"

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    weather = data.get('weather')
    wardrobe = data.get('wardrobe')

    outfits = get_recommendations(weather, wardrobe)
    return jsonify({'outfits': outfits})

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

