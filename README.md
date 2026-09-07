# BTC: Bull vs Bear Classification for the Past 2 Years Using Technicals

## Overview 
This project classifies each day of BTC trading over the past 2 and a half years into a "Bull" or "Bear" regime using a single, widely-used technical indicator: the 200-day moving average. The classifications are as follows: 

- Bull: price above the 200-day MA 
- Bear: price below the 200-day MA

It then tests whether this simple classification actually corresponds to a measurable difference in BTC' daily return behavior, or whether the labels are effectively meaningless noise. 


## Research Question
Does BTC's daily return behavior differ meaningfully between Bull and Bear regimes, as defined by a simple 200-day moving average crossover? 

Specifically: 

- Is the average daily return significantly different between Bull and Bear days? 
- Is that difference statistically distinguishable from noise? 
- Does volatility also differ meaningfully between the two regimes, or only returns? 

## Data
- **Source:** Yahoo Finance (via the yfinance Python library)
- **Time period:** 01-01-2023 - 31-08-2026
- **Granularity:** Daily OHLCV 
- **Size:** 
- **Access method:** Public API

## Tools & Methods
- **Database:** DuckDB (SQL) for storage, cleaning, and aggregation
- **Language:** Python (pandas, numpy, matplotlib/plotly, scipy.stats, statsmodels)
- **Key techniques used:** window functions, GROUP BY aggregation, OLS regression

## Pipeline

1. Ingestion: Daily BTC_USD OHLCV data was pulled via the yfinance Python library and exported to CSV. The export included yfinance's characteristic multi-row header (ticker/metadata rows), requiring skip=3 and manually assigned column names when loading into DuckDB. 
2. Cleaning: Verified no null values existed in the raw price/volume columns using an explicit WHERE...IS NULL check. 
3. Transformation: Built a 200-day rolling moving average using a SQL window function (AVG(close) OVER (ORDER BY date ROWS BETWEEN 199 AND PRECEDING AND CURRENT ROW)). Used ROW_NUMBER() to explicitly force NULL for the first 199 rows, since DuckDB's window frame silently computes a smaller, expanding average during the "warm-up" period rather than returning NULL by default. Each day was then subsequently labeled 'bull' or 'bear' via CASE WHEN close > ma_200. Daily returns were computed using LAG(): (close - LAG(close)) / LAG(close)
4. EDA: Aggregated average daily return and volatility (standard deviation of daily return) per regime using GROUP BY regime in SQL, after excluding the 199 warm-up rows with WHERE regime IS NOT NULL. 
5. Statistical analysis: Ran an independent 2-sample t-test in Python using the scipy.stats library comparing daily returns between Bull and Bear regimes. Followed up with a Shapiro-Wilk normality test on each group to check the t-test's underlying assumptions, given known fat-tailed behavior in financial return data. 
6. Visualization: Built a two-panel bar chart in matplotlib comparing average daily return and volatility side-by-side across the two regimes. 

## Key Findings

1. Daily returns differ significantly between bull and bear regimes (t-stat: 3.3028, p-value: 0.0010). If there were truly no difference between daily returns of Bull and Bear regimes, there would only be a 0.1% chance of observing a difference this large by random chance. 
2. Bull-regime days averaged a +0.31% daily return, vs -0.18% for bear-regime days. 
3. Both regimes significantly deviate from a normal distribution (Shapiro-Wilk p < 0.001 for both groups). This is an expected feature of financial returns data. Given the large sample size in each group and how far the t-test's p-value sits below the 0.05 threshold, this violation is unlikely to overturn the core finding. 
4. Volatility was nearly identical between the two regimes (bull: 0.0245; bear: 0.0241). This small difference was not formally tested for significance. This is a notable contrast to the common assumption that bear markets are meaningfully more volatile than bull markets; in this dataset, the regimes differ clearly in return direction, but not obviously in volatility. 


## Visualization
Please refer to the figures folder. 

## Limitations & Caveats
This is my second end-to-end data analysis project, built to extend what I learned from my first (TradFi Real Yields vs NASDAQ) into a regime-based framing rather than a single-day comparison. 

- Single indicator, single threshold: Regime classification relies entirely on one technical indicator (200-day MA) with a simple below/above rule. Real regime detection in practice often combines multiple indicators or uses more sophisticated methods. I chose the simplest, most standard approach as I wanted to get my hands dirty. 
- Volatility difference wasn't formally tested: I reported the volatility gap between regimes descriptively but didn't run a formal test to check whether its statistically meaningful or just noise. 
- Non-normal residuals in the t-test: Both regimes failed the Shapiro-wilk normality test. I judged this unlikely to overturn the result given the very small p-value and large sample size, but I haven't run a non-parametric alternative to formally confirm that judgement. 
- Single asset, one MA window: Only BTC was tested, using a 200-day window. I didn't check whether the result holds using a 50-day MA instead, or whether it holds for other crypto assets. 
- (approx.) 3.6 years sample window: This captures one or two BTC market cycles at most, not a long, multi-cycle history. 
## What I'd Do Next

- Learn about non-parametric tests and test a non-parametric alternative to confirm the t-test result holds up without relying on the normality assumption.
- Formally test the volatility difference using the Levene's test
- Compare 50-day vs 200-day MA classifications to see how sensitive the bull/bear split are to that choice 
- Extend to other assets (both crypto and stocks)

## How to Reproduce

# 1. Clone the repo
git clone [your-repo-link]
cd [repo-folder-name]

# 2. Install dependencies
pip install duckdb pandas numpy matplotlib scipy statsmodels yfinance

# 3. Pull raw data (or use the CSV already in raw_data/, if included)
python3 src/pull_data.py

# 4. Load into DuckDB and build the regime classification table
python3 src/build_regime_table.py

# 5. Run the statistical analysis and generate the chart
python3 src/analysis.py

## Project Structure
```
project-folder/
├── raw_data/              # original BTC-USD CSV from yfinance
├── db/                    # btc_regime.duckdb — the working database
├── sql/                   # saved .sql scripts (table creation, regime classification)
├── src/                   # Python scripts (data pull, transformation, analysis)
├── figures/                # btc_regime_comparison.png and other charts
├── README.md
```

---
*Author: Priyansh Saxena | https://www.linkedin.com/in/priyansh-saxena/ | 7th September, 2026*