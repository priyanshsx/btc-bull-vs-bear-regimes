import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
from scipy import stats
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
# print(df.head(10))

# pulling the bull regime and creating a new dedicated df

df_bull = con.sql("""
    SELECT daily_returns
    FROM btc_regime_updated
    WHERE regime = 'bull'
""").df()['daily_returns']

# pulling the bear regime and creating a new dedicated df

df_bear = con.sql("""
    SELECT daily_returns
    FROM btc_regime_updated 
    WHERE regime = 'bear'
""").df()['daily_returns']

# calculating the t-stat 
t_stat, p_value = stats.ttest_ind(df_bull, df_bear)
print(f"T-statistic: {t_stat: .4f}")
print(f"p_value: {p_value: .4f}")

# checking the direction of the effect
print(f"Bull regime mean: {df_bull.mean(): .4f}")
print(f"Bear regime mean: {df_bear.mean(): .4f}")

## checking if each group (bull and bear) is actually normally distributed because t-test generally makes that assumption 

shapiro_bull = stats.shapiro(df_bull)
shapiro_bear = stats.shapiro(df_bear)

print(f"Bull regime - W-stat: {shapiro_bull.statistic: .4f}, p-value: {shapiro_bull.pvalue: .7f}")
print(f"Bear regime - W-stat: {shapiro_bear.statistic: .4f}, p-value: {shapiro_bear.pvalue: .7f}")