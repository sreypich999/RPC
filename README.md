# 🌦️ Weather Reporter RPC

[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-lightblue)](https://flask.palletsprojects.com/)
[![Requests](https://img.shields.io/badge/Requests-2.28.1-orange)](https://docs.python-requests.org/en/latest/)

A Python Flask application that communicates with a custom RPC server to fetch real-time weather information and 5-day weather forecasts using the OpenWeatherMap API. Users can search for weather by city and view current conditions and a 5-day forecast.

---

## ✨ Features

- 🏙️ **City Weather Search**: Enter any city to get current weather and 5-day forecast.
- 🔄 **Client-Server RPC Communication**: Flask acts as the client, sending requests to a Python XML-RPC server.
- 🌦️ **Live Weather Data**: Temperature, humidity, wind speed, descriptions for current and 5-day forecast.
- 📁 **HTML Templates**: Clean and responsive Jinja2 templates for input and results.
- ⚙️ **Modular Design**: Separated concerns for scalability and easy maintenance.

---

## 📸 Screenshots

| Search Page          | Current Weather Result   | 5-Day Forecast           |
|---------------------|-------------------------|--------------------------|
| ![Search](screenshots/search.png) | ![Current](screenshots/current_weather.png) | ![Forecast](screenshots/forecast.png) |

> _Add screenshots to a `screenshots/` folder inside your project._

---

## 🗂️ Project Structure

```plaintext
RPC/
├── app/
│   ├── __init__.py
│   ├── main.py              # Flask routes
│   ├── rpc_client.py        # RPC client connecting to server
│   ├── rpc_server.py        # XML-RPC server providing weather data
│   ├── services.py          # OpenWeatherMap API interactions
│   └── templates/
│       ├── index.html       # City input form
│       ├── weather.html     # Current weather result
│       └── forecast.html    # 5-day forecast result
├── run.py                   # Flask app entry point
├── requirements.txt         # Python dependencies
├── .env                     # API key config (ignored in Git)
└── README.md                # This file
