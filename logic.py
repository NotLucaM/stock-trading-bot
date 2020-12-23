import numpy as np
import portfolio_manger

global lookback
lookback = {}
global stop_loss
stop_loss = 0.02

ceiling, floor = 30, 10


def init():
    for ticker in portfolio_manger.available:
        lookback[ticker] = 30


def look():
    active = portfolio_manger.get_active()

    for ticker in active:
        if ticker not in portfolio_manger.available:
            portfolio_manger.available.append(ticker)
            portfolio_manger.purchased[ticker] = 0


def on_market_open(ticker: str):
    # determine the look back length based on volatility
    close = portfolio_manger.get_data(ticker, period='1m')['Close']
    today_volatility = np.std(close[1:31])
    yesterday_volatility = np.std(close[0:30])
    delta_volatility = (today_volatility - yesterday_volatility) / today_volatility
    lookback[ticker] = round(lookback[ticker] * (1 + delta_volatility))

    if lookback[ticker] > ceiling:
        lookback[ticker] = ceiling
    elif lookback[ticker] < floor:
        lookback[ticker] = floor


def on_update(ticker: str):
    high = portfolio_manger.get_data(ticker, period='1m')

    if portfolio_manger.purchased[ticker] == 0 \
            and portfolio_manger.get_price(ticker) >= max(high[:-1]):
        portfolio_manger.buy(ticker, 1)
