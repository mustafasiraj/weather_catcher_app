import streamlit as st
import requests

st.set_page_config(page_title="🌤️ Weather Fetcher", page_icon="🌤️")

st.title("🌦️ Live Weather Fetcher")

api_key = st.secrets["weather_api_key"]

# Ask user for a city
city = st.text_input("Enter city name:", "")

if city:
    # Use WeatherAPI's free demo endpoint
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}={city}"
    
    # Make the GET request
    response = requests.get(url)
    data = response.json()

    # Check and print weather info
    if "current" in data:
        st.subheader(f"📍 Weather in {city.title()}")
        st.write(f"🌡️ Temperature: {data['current']['temp_c']}°C")
        st.write(f"💨 Wind: {data['current']['wind_kph']} kph")
        st.write(f"⛅ Condition: {data['current']['condition']['text']}")
    else:
        st.error("⚠️ Could not find weather info. Try another city.")
