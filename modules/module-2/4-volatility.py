import pandas as pd
import numpy as np


def get_most_volatile(prices):
    """Return the ticker symbol for the most volatile stock.

    Parameters
    ----------
    prices : pandas.DataFrame
        a pandas.DataFrame object with columns: ['ticker', 'date', 'price']

    Returns
    -------
    ticker : string
        ticker symbol for the most volatile stock
    """

    def volatility(df):
        """
        Helper function to calculate daily volatility.

        :param df: DataFrame of daily prices of stock.

        :return: Volatility.
        """
        periods = len(df.price)
        return np.sqrt(periods) * np.std(df.price)

    tickers = prices.ticker.unique()
    most = 0
    result = None
    for i in tickers:
        current = volatility(prices[prices['ticker'] == i])
        if most <= current:
            most = current
            result = i
        else:
            continue
    return result


def test_run(filename='prices.csv'):
    """Test run get_most_volatile() with stock prices from a file."""
    prices = pd.read_csv(filename, parse_dates=['date'])
    print("Most volatile stock: {}".format(get_most_volatile(prices)))


if __name__ == '__main__':
    test_run()
