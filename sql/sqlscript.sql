-- creating the btc table 

con.sql("""
CREATE TABLE btc AS SELECT * FROM read_csv_auto('btc_daily.csv')
""")

con.sql("SELECT * FROM btc LIMIT 5").show()

-- checking for NULLs
con.sql("SELECT * FROM btc WHERE date is NULL OR close IS NULL OR high IS NULL OR low IS NULL OR
    open IS NULL or vol IS NULL").show()

-- using ma 200 for classification 

con.sql("""
CREATE TABLE btc_regime AS
SELECT 
    date,
    close,
    AVG(close) OVER (ORDER BY date ROWS BETWEEN 199 PRECEDING AND CURRENT ROW) AS ma_200,
    CASE
        WHEN close > AVG(close) OVER (ORDER BY date ROWS BETWEEN 199 PRECEDING AND CURRENT ROW) THEN 'bull'
        ELSE 'bear'
    END AS regime
FROM btc
ORDER BY date
""")

-- checking for NULLs
con.sql("SELECT * FROM btc_regime WHERE date IS NULL OR close IS NULL OR ma_200 IS NULL OR regime IS NULL").show()

-- I was expecting the first 199 entries to show up as NULL, which did not happen. This may be because SQL is taking the average of the current row (since we have in our code ROWS BETWEEN 199 PRECEDING AND CURRENT ROW).
-- Since those are false values and do not amount to 200-Day MA, the first 199 rows will have to be NULLed out. 

