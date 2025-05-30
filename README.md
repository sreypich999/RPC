# 🌦️ Weather Reporter RPC

[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-lightblue)](https://flask.palletsprojects.com/)
[![Requests](https://img.shields.io/badge/Requests-2.28.1-orange)](https://docs.python-requests.org/en/latest/)

A Python Flask application that communicates with a custom RPC server to fetch real-time weather information using the OpenWeatherMap API. Users can search for weather by city and view current and forecast conditions.

---

## ✨ Features

- 🏙️ **City Weather Search**: Enter any city and get current weather conditions.
- 🔄 **Client-Server RPC Communication**: Flask acts as the client, sending requests to a Python XML-RPC server.
- 🌦️ **Live Weather Data**: Temperature, humidity, wind speed, and descriptions from OpenWeatherMap.
- 📁 **HTML Templates**: Built-in Flask templating (Jinja2) for displaying results.
- ⚙️ **Modular Structure**: Organized code for scalability and readability.

---

## 📸 Screenshots

| Search Page | Weather Result |
|-------------|----------------|
| ![Search](screenshots/search.png) | ![Weather](screenshots/weather.png) |

> _Add screenshots to a `screenshots/` folder in your project directory._

---

## 🗂️ Project Structure

```plaintext
RPC/
├── app/
│   ├── __init__.py
│   ├── main.py              # Flask routes
│   ├── rpc_client.py        # RPC client to connect to server
│   ├── rpc_server.py        # XML-RPC server code
│   ├── services.py          # Weather fetching logic
│   └── templates/
│       ├── index.html       # Input form for city
│       └── weather.html     # Weather display page
├── run.py                   # Flask app entrypoint
├── requirements.txt         # Dependencies
├── .env                     # API key config (not committed)
└── README.md
