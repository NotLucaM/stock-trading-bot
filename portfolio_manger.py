import threading
from collections import Counter
from datetime import datetime

import alpaca_trade_api as tradeapi
import yfinance as yf

global api = tradeapi.REST()

def buy(ticker: str, quantity: int):
    tradeapi