import streamlit as st
import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ========== CONFIG ==========
API_KEY = "your_actual_api_key_here"   # Replace with your OpenWeatherMap API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# ========== STREAMLIT UI ==========
st.title("🌍 Real-Time Weather Dashboard")
st.write("Fetching live weather data using OpenWeatherMap API")

# User city selection
cities = st.multiselect(
    "Select Cities:",
    ["London", "New York", "Tokyo", "Delhi", "Sydney", "Paris", "Moscow"],
    default=["London", "Delhi", "New York"]
)

if st.button("Fetch Weather Data"):
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
            st.warning(f"⚠️ Error fetching data for {city}: {data.get('message')}")

    if weather_data:
        df = pd.DataFrame(weather_data)
        st.subheader("📊 Weather Data")
        st.dataframe(df)

        sns.set_style("whitegrid")

        # --- Temperature Chart ---
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.barplot(x="City", y="Temperature (°C)", data=df, palette="coolwarm", ax=ax)
        ax.set_title("Temperature by City")
        st.pyplot(fig)

        # --- Humidity Chart ---
        fig, ax = plt.subplots(figsize=(8, 4))
        sns.lineplot(x="City", y="Humidity (%)", data=df, marker="o", ax=ax, color="blue")
        ax.set_title("Humidity by City")
        st.pyplot(fig)

        # --- Weather Conditions Pie Chart ---
        fig, ax = plt.subplots(figsize=(6, 6))
        df["Weather"].value_counts().plot.pie(
            autopct="%1.1f%%", colors=sns.color_palette("pastel"), ax=ax
        )
        ax.set_ylabel("")
        ax.set_title("Weather Condition Distribution")
        st.pyplot(fig)
    else:
        st.error("⚠️ No data fetched. Please check your API key or try again later.")
