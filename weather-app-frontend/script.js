document.getElementById('getWeather').addEventListener('click', function() {
    const city = document.getElementById('city').value;
    const weatherResult = document.getElementById('weatherResult');

    if (city) {
        fetch(`http://localhost:5001/weather?city=${city}`)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok ' + response.statusText);
                }
                return response.json();
            })
            .then(data => {
                // Display the weather data
                weatherResult.innerHTML = `
                    <h2>${data.city}</h2>
                    <p>Temperature: ${data.temperature} °C</p>
                    <p>Description: ${data.description}</p>
                `;
            })
            .catch(error => {
                weatherResult.innerHTML = `<p>There was an error: ${error.message}</p>`;
            });
    } else {
        weatherResult.innerHTML = `<p>Please enter a city name.</p>`;
    }
});
