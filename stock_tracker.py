import matplotlib
matplotlib.use("TkAgg")

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Choose your stock and date range
ticker = "AAPL"  # Change to any stock symbol (e.g., TSLA, MSFT)
start_date = "2024-01-01"
end_date = "2024-12-31"

# Step 2: Download stock data
data = yf.download(ticker, start=start_date, end=end_date)
data["30MA"] = data["Close"].rolling(window=30).mean()
print(data[["Close", "30MA"]].head(40))
print(data.head())  # prints first 5 rows of the stock data


# Step 3: Plot the closing prices
plt.figure(figsize=(10, 5))
plt.plot(data["Close"], label=f"{ticker} Close Price")
plt.plot(data["30MA"], label="30-Day Moving Avg")
plt.title(f"{ticker} Stock Price ({start_date} to {end_date})")
plt.xlabel("Date")
plt.ylabel("Price ($)")
plt.legend()
plt.grid(True)
plt.show()

