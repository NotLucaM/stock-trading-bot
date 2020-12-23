from time import sleep
from yahoo_fin import stock_info as si

import portfolio_manger
from logic import look

for i in range(1, 10000):
    # print(portfolio_manger.get_data("AAPL"))

    look()
    sleep(60)
