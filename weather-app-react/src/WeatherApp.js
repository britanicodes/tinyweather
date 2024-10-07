// src/WeatherApp.js
import React, { useState } from 'react';
import './style.css'; // Import your CSS file

const WeatherApp = () => {
    const [city, setCity] = useState('');
    const [weatherData, setWeatherData] = useState(null);

    const fetchWeatherData = async () => {
        const response = await fetch(`http://ec2-3-89-158-143.compute-1.amazonaws.com:5001/weather?city=${city}`);
        const data = await response.json();
        setWeatherData(data);
    };

    return (
        <div>
            <h1>Weather App</h1>
            <input 
                type="text" 
                value={city} 
                onChange={(e) => setCity(e.target.value)} 
                placeholder="Enter city" 
            />
            <button onClick={fetchWeatherData}>Get Weather</button>
            {weatherData && (
                <div>
                    <h2>Currently in {weatherData.city}:</h2>
                    <p>{weatherData.forecast}</p>
                    <p>Temperature: {weatherData.temperature} °C</p>
                    <p>Description: {weatherData.description}</p>
                </div>
            )}
        </div>
    );
};

export default WeatherApp;
