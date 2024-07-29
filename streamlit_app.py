import streamlit as st
import requests

# Set the backend API endpoint
BACKEND_API_URL = 'http://13.236.135.206:5000'

# Function to fetch coin status
def fetch_coin_status():
    try:
        response = requests.get(f'{BACKEND_API_URL}/coin_status')
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f'Failed to fetch coin status: {response.status_code}')
    except Exception as e:
        st.error(f'Error: {e}')
    return None

# UI setup
st.title('Test Connection to Backend')

if st.button('Fetch Coin Status'):
    coin_status = fetch_coin_status()
    if coin_status:
        st.write(f"Volume: {coin_status['volume']}")
        st.write(f"Current Price: ${coin_status['price']:.2f}")
        st.write(f"Previous Price: ${coin_status['previous_price']:.2f}")
