from flask import Flask, request, jsonify
from outfit_recommender import get_recommendations
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # 🔥 Allows Flutter web access

@app.route('/')
def home():
    return "AI Wardrobe API Running!"

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    weather = data.get('weather')
    wardrobe = data.get('wardrobe')
    preferences = data.get('preferences')  # 🔥 use this in AI logic

    outfits = get_recommendations(weather, wardrobe, preferences)
    return jsonify({'outfits': outfits})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # ✅ Required for Render
    app.run(host='0.0.0.0', port=port)
