# fetching btc 2-year data from yfinance 

import yfinance as yf

btc = yf.download('BTC-USD', start='2023-01-01', end='2026-08-31')
btc.to_csv('/home/priyansh/Documents/d/btc bull vs bear regimes/data/raw/btc_daily.csv')
