from time import sleep
from yahoo_fin import stock_info as si
from datetime import datetime
from datetime import timedelta
import time

import portfolio_manger
import logic

logic.init()
while True:
    logic.look()
    for ticker in portfolio_manger.available:
        logic.on_market_open(ticker)

    while True:
        now = datetime.now()
        if portfolio_manger.market_close_h <= now.hour:
            if portfolio_manger.market_close_m <= now.minute:
                break
                print('ended')

        for ticker in portfolio_manger.available:
            logic.on_update(ticker)

    t = datetime.today()
    future = datetime(t.year, t.month, t.day, 6, 30)
    if t.hour >= 2:
        future += timedelta(days=1)
    time.sleep((future - t).total_seconds())
