import yfinance as yf
#choose a stock(e.g.,Apple)
ticker = "AAPL"
#Get the Data
data = yf.Ticker(ticker)
#print the current price
print(f"The current price of {ticker} is: {data.info['currentPrice']}")
