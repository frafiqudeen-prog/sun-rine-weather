# SkyCast Weather Forecast App

A professional responsive weather forecast application built with:

- HTML
- CSS
- JavaScript
- Python Flask
- OpenWeatherMap API

## Features

- Search weather by city
- Current temperature
- Feels-like temperature
- Humidity
- Wind speed
- Weather icons
- 5-day forecast cards
- Responsive design for mobile, tablet and desktop
- Error handling
- Clean frontend/backend separation

## Installation

### 1. Open the project folder

```bash
cd weather_forecast_app
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your API key

Open `app.py` and replace:

```python
API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"
```

with your OpenWeatherMap API key.

### 5. Run the application

```bash
python app.py
```

### 6. Open in browser

```text
http://127.0.0.1:5000
```

## Project Structure

```text
weather_forecast_app/
│
├── app.py
├── requirements.txt
├── .env.example
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js
```

## API

This project uses OpenWeatherMap:

- Current Weather API
- 5-day / 3-hour Forecast API
