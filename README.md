# BTC: Bull vs Bear Classification for the Past 2 Years Using Technicals

## Overview 


## Research Question


## Data
- **Source:** 
- **Time period:** 
- **Granularity:** 
- **Size:** 
- **Access method:** 

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
*Author: Priyansh Saxena | https://www.linkedin.com/in/priyansh-saxena/ | 3rd September, 2026*