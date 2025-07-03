import streamlit as st
import requests

st.set_page_config(page_title="🌤️ Weather Fetcher", page_icon="🌤️")

st.title("🌦️ Live Weather Fetcher")

# 🔐 Load your API key securely from Streamlit secrets
api_key = st.secrets["weather_api_key"]

# 🏙️ Ask user for city input
city = st.text_input("Enter city name:")

if city:
    # 🌐 Prepare the correct WeatherAPI URL
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    try:
        # 📡 Fetch the data
        response = requests.get(url)
        data = response.json()

        # ✅ Check if valid data is returned
        if "current" in data:
            st.subheader(f"📍 Weather in {city.title()}")
            st.write(f"🌡️ Temperature: {data['current']['temp_c']}°C")
            st.write(f"💨 Wind: {data['current']['wind_kph']} kph")
            st.write(f"⛅ Condition: {data['current']['condition']['text']}")
        else:
            st.error("⚠️ Could not find weather info. Try another city.")
    except Exception as e:
        st.error(f"❌ Error fetching data: {e}")
