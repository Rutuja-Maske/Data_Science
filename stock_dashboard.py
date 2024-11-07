import requests
import streamlit as st
from datetime import datetime
import time

# Alpha Vantage API configuration
API_KEY = "YI7VO8EOIFBWQ83F"  # Replace with your actual API key
STOCK_SYMBOL = "AAPL"  # Replace with the desired stock symbol

# Function to fetch live stock data from Alpha Vantage
def fetch_stock_data():
    url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": STOCK_SYMBOL,
        "interval": "1min",
        "apikey": API_KEY
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Streamlit Dashboard
st.title("Live Stock Market Dashboard")
st.write("Fetching live stock data...")

# Create a container to display live data
live_data_container = st.empty()

# Display header for stock data
st.subheader("Stock Data Overview")

# Placeholders for stock data
time_display = st.empty()
open_display = st.empty()
high_display = st.empty()
low_display = st.empty()
close_display = st.empty()
volume_display = st.empty()

# Main loop to fetch and display stock data
while True:
    stock_data = fetch_stock_data()
    
    if stock_data and "Time Series (1min)" in stock_data:
        try:
            # Extract the most recent time data
            time_series = stock_data['Time Series (1min)']
            latest_time = next(iter(time_series))  # Get the latest available time entry
            latest_data = time_series[latest_time]

            # Extract stock data from the latest available time
            open_price = latest_data['1. open']
            high_price = latest_data['2. high']
            low_price = latest_data['3. low']
            close_price = latest_data['4. close']
            volume = latest_data['5. volume']

            # Convert time to readable format
            display_time = datetime.strptime(latest_time, '%Y-%m-%d %H:%M:%S')

            # Update the displayed data in the dashboard
            time_display.write(f"**Time**: {display_time}")
            open_display.write(f"**Open**: {open_price}")
            high_display.write(f"**High**: {high_price}")
            low_display.write(f"**Low**: {low_price}")
            close_display.write(f"**Close**: {close_price}")
            volume_display.write(f"**Volume**: {volume}")
        
        except KeyError as e:
            live_data_container.write(f"Error: Missing key {e}")
    else:
        live_data_container.write("Error: Missing key 'Time Series (1min)' or data fetch failed.")

    # Wait for 60 seconds before the next update
    time.sleep(60)
