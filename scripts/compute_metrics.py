import numpy as np
from scipy.stats import linregress

# Daily Return
def daily_returns(nav_series):
    return nav_series.pct_change()

# Annualized Return
def annualized_return(returns):
    returns = returns.dropna()
    if len(returns) == 0:
        return np.nan

    return (1 + returns).prod() ** (252 / len(returns)) - 1

# CAGR
def cagr(start_nav, end_nav, years):
    if start_nav <= 0:
        return np.nan

    return (end_nav / start_nav) ** (1 / years) - 1

# Sharpe Ratio
def sharpe_ratio(returns, rf=0.065):

    rf_daily = rf / 252

    excess = returns - rf_daily

    std = returns.std()

    if std == 0:
        return np.nan

    return (excess.mean() / std) * np.sqrt(252)

# Sortino Ratio
def sortino_ratio(returns, rf=0.065):

    rf_daily = (1 + rf) ** (1/252) - 1

    excess = returns - rf_daily

    downside = np.where(excess < 0, excess, 0)

    downside_std = np.sqrt((downside ** 2).mean())

    if downside_std == 0:
        return np.nan

    return (
        (excess.mean() * 252)
        /
        (downside_std * np.sqrt(252))
    )

# Alpha Beta
def alpha_beta(fund_returns, benchmark_returns):

    slope, intercept, r, p, std_err = linregress(
        benchmark_returns,
        fund_returns
    )

    return {
        "alpha_daily": intercept,
        "alpha_annual": intercept * 252,
        "beta": slope,
        "r_squared": r ** 2
    }

# Maximum Drawdown
def max_drawdown(nav_series):

    running_max = nav_series.cummax()

    drawdown = nav_series / running_max - 1

    return drawdown.min()

# Tracking Error
def tracking_error(fund_returns, benchmark_returns):

    active_return = (
        fund_returns -
        benchmark_returns
    )

    return (
        active_return.std()
        * np.sqrt(252)
    )