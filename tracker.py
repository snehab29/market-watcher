import yfinance as yf                                    # yfinace's a library to fetch data from yahoo finance, it knows how to get stock details from yahoo.
import smtplib

ticker_symbol = "AAPL"                                   # ticker_symbol is a variable storing the code for a stock/fund. and AAPL is the Apple's stock symbol.

ticker = yf.Ticker(ticker_symbol)                        # yf.Ticker() asks yfinance to crrate an object for this ticker. and ticker a variable that now represents the stock, and you can ask it for prices, historical data, etc.

current_price = ticker.history(period="1d")['Close'][-1]   # ticker.history(period="1d") → fetches the stock’s price history for the last 1 day. ['Close'] → looks only at the “closing price” column. [-1] → grabs the most recent closing price (last item in the list). current_price → stores that number so we can use it later.

print(f"the current price of {ticker_symbol} is ${current_price:.2f}")   #print() → shows text/output in the terminal. f"..." → f-string, lets us insert variables inside a string. {ticker_symbol} → inserts the ticker (e.g., AAPL). {current_price:.2f} → inserts the price rounded to 2 decimal places.

target_price = float(input("Enter your target price: "))        #float(...) → converts the typed string into a number (so you can compare prices).

if current_price <= target_price:
    print(f"Alert! {ticker_symbol} has dropped to ${current_price:.2f}")
    
    sender_email = "snehabajaj2903@gmail.com"
    sender_password = "lqrwmocyifhwratu"
    receiver_email = "snehabajaj2903@gmail.com"
    
    subject = f"{ticker_symbol} Alert!"
    body = f"{ticker_symbol} has dropped to ${current_price:.2f}"
    message = f"Subject: {subject}\n\n{body}"
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, message)
    server.quit()
    
else:
    print(f"No alert. {ticker_symbol} is at ${current_price:.2f}")     #.2f → tells Python: f → floating-point number (decimal) .2 → round it to 2 decimal places
    

    
        