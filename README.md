# API-Integration-and-Visualization

# 🌦️ Weather Data Visualization Dashboard  

## 📌 Project Overview  
This project fetches **real-time weather data** using the [OpenWeatherMap API](https://openweathermap.org/) and provides two modes:  
1. A **Python script (`weather_data.py`)** that generates static visualizations.  
2. An **interactive Streamlit dashboard (`dashboard.py`)** where users can select multiple cities and view weather insights dynamically.  

The goal is to analyze and visualize weather parameters such as **temperature, humidity, and condition distribution** across cities.  

---

## ⚙️ Features  
- Fetches **live weather data** from OpenWeatherMap.  
- Displays results in a structured **Pandas DataFrame**.  
- Visualizes weather data with **Matplotlib** and **Seaborn**:  
  - 🌡️ Temperature bar chart  
  - 💧 Humidity line chart  
  - ☁️ Weather condition distribution pie chart  
- Handles errors (invalid API key, missing data).  
- Saves static plots as `weather_dashboard.png`.  
- Interactive dashboard built with **Streamlit**.  

---

## 🛠️ Tech Stack  
- **Python 3**  
- **Libraries**:  
  - `requests` → Fetching API data  
  - `pandas` → Data processing  
  - `matplotlib`, `seaborn` → Data visualization  
  - `streamlit` → Interactive dashboard  

---

## 📂 Project Structure  
