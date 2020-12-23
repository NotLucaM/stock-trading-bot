from yahoo_fin import stock_info as si

import alpaca_trade_api as tradeapi
import yfinance as yf

import KEYS

global api
api = tradeapi.REST(KEYS.TRADE_KEY_ID, KEYS.TRADE_API_SECRET_KEY, base_url="https://paper-api.alpaca.markets")
global buying_power

global available
available = []  # stocks to look at
global purchased  # stocks bought and how much is bought
purchased = {}
market_open_h = 6
market_open_m = 30
market_close_h = 13
market_close_m = 30

yf.pdr_override()


def buy(ticker: str, quantity: int):
    # if purchased[ticker] == 0 and buying_power > (quantity * get_price(ticker)):
    #     api.submit_order(symbol=ticker, qty=quantity, side='buy', type='market', time_in_force='day')
    #     purchased[ticker] = quantity
    print("buying " + str(quantity) + " " + ticker)


def sell(ticker: str, quantity: int):
    # if purchased[ticker] < quantity:
    #     quantity = purchased[ticker]
    # api.submit_order(symbol=ticker, qty=quantity, side='sell', type='market', time_in_force='day')
    # purchased[ticker] -= quantity
    print("selling " + str(quantity) + " " + ticker)


def get_active():
    active = si.get_day_most_active()

    return active['Symbol']


def get_data(ticker: str, period='1d', interval='1m'):
    ticker = yf.Ticker(ticker)
    history = ticker.history(period=period, interval=interval)
    del history['Dividends']
    del history['Stock Splits']
    # data = history.iloc[0].to_dict()
    # data['Gain'] = (data['Close'] - data['Open']) / data['Open']
    # print(data)
    #
    # del data['Dividends']
    # del data['Stock Splits']

    return history


def get_price(ticker: str):
    return si.get_live_price(ticker)


def get_performance(ticker: str):
    ticker = yf.Ticker(ticker)
    return ticker.recommendations()
