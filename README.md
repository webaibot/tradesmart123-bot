# TradeSmart Bot

![TradeSmart Bot](https://img.shields.io/badge/TradeSmart-Bot-blue)

TradeSmart Bot is an intelligent trading analysis assistant designed to offer comprehensive insights and analysis for stock market enthusiasts.

## Features
- 📈 Built-in technical indicators: RSI, MACD, moving averages
- 🔍 Pattern recognition for common trading patterns
- 📊 Portfolio tracking and performance metrics
- ⚖️ Risk calculator for trade evaluation

## Project Structure
```
TradeSmart Bot/
├── app.py
├── config.py
├── bot/
│   ├── __init__.py
│   ├── routes.py
│   ├── engine.py
│   ├── models.py
│   ├── knowledge.py
│   ├── responses.py
│   └── utils.py
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── app.js
├── templates/
│   └── index.html
├── tests/
│   ├── __init__.py
│   └── test_engine.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .gitignore
└── .env.example
```

## Setup & Run Instructions
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `python app.py`
4. Open your browser and go to `http://localhost:3000` to chat with TradeSmart Bot.

## Docker Instructions
1. Build the Docker image: `docker build -t tradesmart-bot .`
2. Run the container: `docker run -p 3000:3000 tradesmart-bot`

## Architecture Overview
TradeSmart Bot is built using Flask for the server-side logic, with all intelligence coded in Python. The bot uses state machines and decision trees to handle user interactions and provide trading insights.

## License
This project is licensed under the MIT License.