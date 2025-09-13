import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ========== CONFIG ==========
API_KEY = "b54bf5607f1bdbaf1a2a60128dae162c"   # Replace this
cities = ["London", "New York", "Tokyo", "Delhi", "Sydney", "Paris", "Moscow"]
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# ========== FETCH DATA ==========
weather_data = []

for city in cities:
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        weather_data.append({
            "City": city,
            "Temperature (°C)": data["main"]["temp"],
            "Humidity (%)": data["main"]["humidity"],
            "Pressure (hPa)": data["main"]["pressure"],
            "Weather": data["weather"][0]["description"].capitalize()
        })
    else:
        print(f"Error fetching data for {city}: {data.get('message')}")

# Convert to DataFrame
df = pd.DataFrame(weather_data)

if df.empty:
    print("\n⚠️ No data fetched. Check your API key or API request limits.")
else:
    print("\nWeather Data:\n", df)

    # ========== VISUALIZATION ==========
    sns.set_style("whitegrid")
    plt.figure(figsize=(12, 6))

    # Barplot - Temperature
    plt.subplot(1, 2, 1)
    sns.barplot(x="City", y="Temperature (°C)", data=df, palette="coolwarm")
    plt.title("City-wise Temperature")
    plt.xticks(rotation=30)

    # Lineplot - Humidity
    plt.subplot(1, 2, 2)
    sns.lineplot(x="City", y="Humidity (%)", data=df, marker="o", color="blue")
    plt.title("City-wise Humidity")
    plt.xticks(rotation=30)

    plt.tight_layout()
    plt.savefig("weather_dashboard.png")
    plt.show()



