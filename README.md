# 🌦️ Weather Reporter RPC

[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)  
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)  
[![Flask](https://img.shields.io/badge/Flask-2.x-lightblue)](https://flask.palletsprojects.com/)  
[![Requests](https://img.shields.io/badge/Requests-2.28.1-orange)](https://docs.python-requests.org/en/latest/)

A Python Flask application that communicates with a custom RPC server to fetch real-time weather information and 5-day weather forecasts using the OpenWeatherMap API. Users can search for weather by city and view current conditions and a detailed 5-day forecast.

---

## ✨ Features

- 🏙️ **City Weather Search**: Get current weather and 5-day forecast by entering any city.
- 🔄 **Client-Server RPC Communication**: Flask acts as the client sending requests to a Python XML-RPC server.
- 🌦️ **Live Weather Data**: View temperature, humidity, wind speed, and weather descriptions.
- 📁 **Responsive HTML Templates**: Clean and user-friendly interfaces.
- ⚙️ **Modular & Scalable**: Clear separation of concerns for maintainability and expansion.

---

## 🗂️ Project Structure

```plaintext
our file directory 
weather-reporter/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── rpc_server.py
│   ├── rpc_client.py
│   ├── services.py
│   ├── auth.py
│   ├── config.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── logging_config.py
│   │   └── security.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── css/
│           └── style.css
├── run.py
├── ngrok/
│   └── start_ngrok.sh
├── .env
├── requirements.txt
└── README.md
