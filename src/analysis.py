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

# plotting charts 

fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# avg daily return by regime
ax[0].bar(df['regime'], df['avg_daily_return'], color=['green' if r == 'bull' else 'red' for r in df['regime']])
ax[0].set_title('Average Daily Return by Regime')
ax[0].set_ylabel('Average Daily Return')
ax[0].axhline(0, color='gray', linewidth=0.8)

# volatility by regime 
ax[1].bar(df['regime'], df['volatility'], color=['green' if r == 'bull' else 'red' for r in df['regime']])
ax[1].set_title('Volatility (stdev of daily returns) by regime')
ax[1].set_ylabel('Standard Deviation')

plt.suptitle('BTC: Bull vs. Bear Regime Comparison (200-day) MA')
plt.tight_layout()
plt.savefig('/home/priyansh/Documents/d/btc bull vs bear regimes/figures/btc_regime_comparison.png', dpi=300)
plt.show()