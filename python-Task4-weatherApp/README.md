# Python Basic Weather App (OIBSIP - Task 4)

A command-line real-time weather application created by **Apeksha Suhas Phapale** as part of the Oasis Infobyte Internship Program.

## Features
- Fetches live weather data for any user-specified city or ZIP code
- Parses JSON responses using Python `requests` and the Open-Meteo free weather API
- Displays current temperature in both Celsius (°C) and Fahrenheit (°F), humidity percentage, weather description, and wind speed
- Handles empty inputs, unknown cities, HTTP/API errors, and network timeouts gracefully

## How to Run
1. Install dependencies:
   ```bash
   pip install requests
