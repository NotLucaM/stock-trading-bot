import threading
from collections import Counter
import datetime
from time import sleep
from yahoo_fin import stock_info as si

import alpaca_trade_api as tradeapi
import yfinance as yf
from pandas_datareader import data as pdr

import KEYS

global api
api = tradeapi.REST(KEYS.TRADE_KEY_ID, KEYS.TRADE_API_SECRET_KEY, base_url="https://paper-api.alpaca.markets")
global buying_power

global available
available = []  # stocks to look at
global purchased  # stocks bought and how much is bought
purchased = {}
global security
security = ''

yf.pdr_override()


def buy(ticker: str, quantity: int):
    if purchased[ticker] == 0 and buying_power > (quantity * get_price(ticker)):
        api.submit_order(symbol=ticker, qty=quantity, side='buy', type='market', time_in_force='day')
        purchased[ticker] = quantity


def sell(ticker: str, quantity: int):
    if purchased[ticker] < quantity:
        quantity = purchased[ticker]
    api.submit_order(symbol=ticker, qty=quantity, side='sell', type='market', time_in_force='day')
    purchased[ticker] -= quantity


def get_data(ticker: str, period='1d'):
    ticker = yf.Ticker(ticker)
    history = ticker.history(period=period, interval='1m')
    data = history.iloc[0].to_dict()
    data['Gain'] = (data['Close'] - data['Open']) / data['Open']

    del data['Dividends']
    del data['Stock Splits']

    print(data)


def get_price(ticker: str):
    return si.get_live_price(ticker)


def get_performance(ticker: str):
    ticker = yf.Ticker(ticker)
    print(ticker.recommendations())
