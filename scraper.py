import portfolio_manger as portfolio


def run():

    for ticker in portfolio.available:
        portfolio.get_data(ticker)
