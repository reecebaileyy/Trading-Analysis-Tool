import datetime as dt
import pandas as pd
import yfinance as yf

print(dt.datetime.today() - dt.timedelta(360))

stocks = ["AAPL", "MSFT", "AMZN", "GOOG", "META", "TSLA"]
start = dt.datetime.today() - dt.timedelta(360)
end = dt.datetime.today()
cl_price = pd.DataFrame() # empty dataframe which will be filled with closing prices of each stock
ohlcv_data = {}
 
# looping over tickers and creating a dataframe with close prices
for ticker in stocks:
    cl_price[ticker] = yf.download(ticker, start, end)["Adj Close"]

for ticker in stocks:
    ohlcv_data[ticker] = yf.download(ticker, start, end)


    