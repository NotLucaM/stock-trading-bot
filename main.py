from time import sleep
from yahoo_fin import stock_info as si

import portfolio_manger

for i in range(1, 10000):
    # print(portfolio_manger.get_data("AAPL"))

    print(si.get_stats("AAPL"))
    sleep(60)
