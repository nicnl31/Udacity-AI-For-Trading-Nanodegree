import pandas as pd
import numpy as np


def estimate_volatility(prices, l):
    """Create an exponential moving average model of the volatility of a stock
    price, and return the most recent (last) volatility estimate.

    Parameters
    ----------
    prices : pandas.Series
        A series of adjusted closing prices for a stock.

    l : float
        The 'lambda' parameter of the exponential moving average model. Making
        this value smaller will cause the model to weight older terms less
        relative to more recent terms.

    Returns
    -------
    last_vol : float
        The last element of your exponential moving average volatility model series.

    """
    # Create a daily log return series
    log_returns = np.log(prices/prices.shift(1))

    # Declare n as length of price series, and initialise the numerator and denominator
    n = len(prices)
    numer, denom = 0, 0

    # Iterate in reverse through the log returns to calculate the numerator and iterate
    # through powers of lambda to calculate the denominator
    for i, j in enumerate(reversed(range(1, n))):
        numer += l**i * log_returns[j]**2
        denom += l**i

    # Return the square root of the quotient
    return np.sqrt(numer/denom)


def run(filename='data.txt'):
    """Test run get_most_volatile() with stock prices from a file."""
    prices = pd.read_csv(filename, parse_dates=['date'], index_col='date', squeeze=True)
    print(f"Most recent volatility estimate based on past returns: {estimate_volatility(prices=prices, l=0.7)}")


if __name__ == '__main__':
    run()
