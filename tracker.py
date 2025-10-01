import os
import requests
from dotenv import load_dotenv
import smtplib
import yfinance as yf


ticker_symbol = "AAPL"
ticker = yf.Ticker(ticker_symbol)
# current_price = ticker.history(period="1d")['Close'][-1]  # Not used, using Finnhub API instead


load_dotenv()
API_KEY = os.getenv("FINNHUB_API_KEY")

url = f"https://finnhub.io/api/v1/quote?symbol={ticker_symbol}&token={API_KEY}"
response = requests.get(url)
data = response.json()

current_price = data['c']


print(f"The current price of {ticker_symbol} is ${current_price:.2f}")
target_price = float(input("Enter your target price: "))

if current_price <= target_price:
    print(f"Alert! {ticker_symbol} has dropped to ${current_price:.2f}")

    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_PASSWORD")
    receiver_email = os.getenv("RECEIVER_EMAIL")

    subject = f"{ticker_symbol} Alert!"
    body = f"{ticker_symbol} has dropped to ${current_price:.2f}"
    message = f"Subject: {subject}\n\n{body}"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, message)
    server.quit()
else:
    print(f"No alert. {ticker_symbol} is at ${current_price:.2f}")
