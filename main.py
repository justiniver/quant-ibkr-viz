import matplotlib.pyplot as plt
import pandas as pd
from ib_insync import *

# connect to IBKR (TWS must be running and API enabled)
ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)

# create contract for AAPL stock
contract = Stock('AAPL', 'SMART', 'USD')

bars = ib.reqHistoricalData(
    contract,
    endDateTime='',
    durationStr='1 M',
    barSizeSetting='1 day',
    whatToShow='TRADES',
    useRTH=True,
    formatDate=1
)

# convert data to pandas DataFrame
df = util.df(bars)

# plot the closing prices
plt.figure(figsize=(10, 5))
plt.plot(df['date'], df['close'], label='AAPL Closing Price')
plt.title('AAPL - Last Month')
plt.xlabel('Date')
plt.ylabel('Price ($)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

ib.disconnect()
