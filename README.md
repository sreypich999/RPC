# 🌦 Weather Reporter RPC

[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)  
[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue?logo=python)](https://www.python.org/)  
[![Flask 2.x](https://img.shields.io/badge/flask-2.x-lightblue?logo=flask)](https://flask.palletsprojects.com/)  
[![Requests 2.28](https://img.shields.io/badge/requests-2.28.1-orange?logo=python)](https://docs.python-requests.org/)

> A sleek Flask app communicating via XML-RPC to provide current weather and 5-day forecasts using OpenWeatherMap API.

---

## ✨ Features

- **Real-time weather search** by city
- XML-RPC client-server architecture  
- Displays **current weather** and **5-day forecast**  
- Clean, minimalistic Jinja2 templates  
- Modular, scalable code design  

---

## 🗂 Project Structure

```plaintext
RPC/
├── app/
│   ├── __init__.py
│   ├── main.py           # Flask routes & app logic
│   ├── rpc_client.py     # XML-RPC client
│   ├── rpc_server.py     # XML-RPC server
│   ├── services.py       # OpenWeatherMap API calls
│   └── templates/
│       ├── index.html    # Search form
│       ├── weather.html  # Current weather display
│       └── forecast.html # 5-day forecast display
├── run.py                # Flask app runner
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables
└── README.md             # Project documentation
