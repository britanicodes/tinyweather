from flask import Flask, jsonify, request # type: ignore
import requests # type: ignore
from flask_cors import CORS # type: ignore

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify(message="Welcome to my Flask app!")

@app.route('/hello')
def hello():
    return jsonify(message="HELLOOOOO!")

@app.route('/weather', methods=['GET'])
def get_weather():
    api_key = process.env.REACT_APP_API_KEY;
    city = request.args.get('city')
    if not city:
        print("No city parameter provided")  # Add this line
        return jsonify({"error": "City parameter is required"}), 400

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    print("Response status code:", response.status_code)  # Add this line
    
    if response.status_code != 200:
        print("City not found or API error")  # Add this line
        return jsonify({"error": "City not found"}), 404

    data = response.json()
    weather_info = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"]
    }
    return jsonify(weather_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)

