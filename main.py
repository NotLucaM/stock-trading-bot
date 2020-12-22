from time import sleep

from portfolio_manger import query_price

for i in range(1, 10000):
    query_price("AAPL")
    sleep(5)