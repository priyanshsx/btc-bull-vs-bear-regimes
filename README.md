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


## Key Findings

1. Upon investigation, we found a p-value of 0.0010. This implies that if there were truly no difference between the daily returns in bull and bear regimes for the calculated sample, there were a 0.1% chance we would observe a difference this large purely by chance. 
2. The t-statistic, upon running on both the independent samples was found to be 3.3028. 


## Visualization


## Limitations & Caveats


## What I'd Do Next


## How to Reproduce


## Project Structure
```
project-folder/
├── data/                  # raw and/or processed data (or note if excluded from repo)
├── notebooks/             # exploratory analysis
├── scripts/               # reusable/production code (data pull, cleaning, etc.)
├── outputs/               # charts, exported results
├── README.md
```

---
*Author: Priyansh Saxena | https://www.linkedin.com/in/priyansh-saxena/ | 7th September, 2026*