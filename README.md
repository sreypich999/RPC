# 🌤️ Weather Reporter RPC

[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)  
[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue?logo=python)](https://www.python.org/)  
[![Flask](https://img.shields.io/badge/flask-2.x-lightblue?logo=flask)](https://flask.palletsprojects.com/)  
[![Requests](https://img.shields.io/badge/requests-2.28.1-orange?logo=python)](https://docs.python-requests.org/)

> A lightweight Flask application interfacing with an XML-RPC server to provide real-time weather updates and 5-day forecasts via OpenWeatherMap.

---

## 🚀 Features

- 🔍 **Search weather by city** with ease  
- 🔗 **XML-RPC client-server communication**  
- 🌡️ Current temperature, humidity, wind speed, and weather description  
- 📅 Detailed 5-day weather forecast  
- 🖥️ Responsive UI with Jinja2 templates  
- 🧱 Modular, clean codebase for easy expansion  

---

## 📂 Project Layout



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




---

## ⚙️ Installation & Setup

**Prerequisites:**  
- Python 3.8+  
- OpenWeatherMap API key

```bash
git clone https://github.com/sreypich999/RPC.git
cd RPC
python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate
pip install -r requirements.txt


