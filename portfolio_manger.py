from yahoo_fin import stock_info as si

import alpaca_trade_api as tradeapi
import yfinance as yf

import KEYS

global api
api = tradeapi.REST(KEYS.TRADE_KEY_ID, KEYS.TRADE_API_SECRET_KEY, base_url="https://paper-api.alpaca.markets")
global buying_power
buying_power = 100000

global available
available = ['GOOGL', 'AMZN']  # stocks to look at
global purchased  # stocks bought and how much is bought
purchased = {}
market_open_h = 6
market_open_m = 0
market_close_h = 13
market_close_m = 0

yf.pdr_override()


def buy(ticker: str, quantity: int):
    global buying_power
    if purchased[ticker] == 0 and buying_power > (quantity * get_price(ticker)):
        api.submit_order(symbol=ticker, qty=quantity, side='buy', type='market', time_in_force='day')
        purchased[ticker] = quantity
        buying_power -= quantity * get_price(ticker)
    print("buying " + str(quantity) + " " + ticker)


def sell(ticker: str, quantity: int):
    global buying_power
    if purchased[ticker] < quantity:
        quantity = purchased[ticker]
    api.submit_order(symbol=ticker, qty=quantity, side='sell', type='market', time_in_force='day')
    purchased[ticker] -= quantity
    buying_power += get_price(ticker) * quantity
    print("selling " + str(quantity) + " " + ticker)


def get_active():
    active = si.get_day_most_active()

    return active['Symbol']


def get_data(ticker: str, period='1d', interval='1m'):
    ticker = yf.Ticker(ticker)
    history = ticker.history(period=period, interval=interval)
    if len(history) == 0:
        global available
        available.remove(ticker.ticker)
        return True
    del history['Dividends']
    del history['Stock Splits']

    return history


def get_price(ticker: str):
    try:
        return si.get_live_price(ticker)
    except AssertionError:
        return True


def get_performance(ticker: str):
    ticker = yf.Ticker(ticker)
    return ticker.recommendations()
