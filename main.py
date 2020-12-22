from time import sleep

import portfolio_manger

for i in range(1, 10000):
    portfolio_manger.get_data("AAPL")
    sleep(5)