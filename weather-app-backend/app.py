from flask import Flask, jsonify, request
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/weather', methods=['GET'])
def get_weather():
    api_key = '4eb72ab8a81eb83af1a742aad2d21b22'  # Replace with your OpenWeatherMap API key
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

