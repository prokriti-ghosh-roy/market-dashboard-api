import yfinance as yf
# #ask the user for astock symbol
# ticker_symbol = input("Enter a stock symbol (e.g., TSLA, MSFT, GOOGL): ")
# #Get the Data
# data = yf.Ticker(ticker_symbol)
# #print the result
# print(f"Current price of{ticker_symbol.upper()} is: {data.info['currentPrice']}")
print("_ _ _Market Dashboard API_ _ _")
print("Type 'exit' to stop the program")
while True:
  #ask the user for a stock symbol
  user_input = input("\nEnter a stock symbol (e.g., TSLA, BTC-USD): ")
  #check if the user wants to quit
  if user_input.lower() == 'exit':
    print("closing dashboard. Goodbye!")
    break

  try:
    #get the data
    data = yf.Ticker(user_input)
    price = data.info['currentPrice']
    currency = data.info['currency']
    print(f"The current price of {user_input.upper()} is: {price} {currency}")
  except Exception:
    print("Could not find that symbol. Please try again (e.g., AAPL.)")

