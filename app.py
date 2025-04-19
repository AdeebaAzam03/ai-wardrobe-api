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

if __name__ == '__main__':
    app.run(debug=True, port=5050)
