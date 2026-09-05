import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
import statsmodels as sm
import duckdb 

con = duckdb.connect('/home/priyansh/Documents/d/btc bull vs bear regimes/data/raw/main.duckdb')

df = con.sql("""
    SELECT regime, 
    AVG(daily_returns) AS avg_daily_return,
    STDDEV(daily_returns) AS volatility
    FROM btc_regime_updated 
    WHERE regime IS NOT NULL 
    GROUP BY regime 
    """).df()
print(df.head(10))