# crypto_chatbot.py
import streamlit as st
import requests

# CoinGecko API
def get_crypto_price(coin_id='bitcoin'):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get(coin_id, {}).get('usd', 'N/A')
    return 'API Error'

# Simple chatbot logic
def crypto_chat_response(user_input):
    user_input = user_input.lower()
    if "price" in user_input and "bitcoin" in user_input:
        price = get_crypto_price('bitcoin')
        return f"Current price of Bitcoin (BTC) is ${price}"
    elif "price" in user_input and "ethereum" in user_input:
        price = get_crypto_price('ethereum')
        return f"Current price of Ethereum (ETH) is ${price}"
    elif "hello" in user_input or "hi" in user_input:
        return "Hello! Ask me about crypto prices like Bitcoin or Ethereum."
    else:
        return "Sorry, I can only give you prices of BTC or ETH for now."

# Streamlit UI
st.title("💬 Crypto Chatbot")
user_query = st.text_input("Ask something about crypto:", "")

if user_query:
    response = crypto_chat_response(user_query)
    st.write(f"🤖 {response}")
