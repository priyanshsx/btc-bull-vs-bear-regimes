-- creating the btc table 

con.sql("""
CREATE TABLE btc AS SELECT * FROM read_csv_auto('btc_daily.csv')
""")

con.sql("SELECT * FROM btc LIMIT 5").show()

-- checking for NULLs
con.sql("SELECT * FROM btc WHERE date is NULL OR close IS NULL OR high IS NULL OR low IS NULL OR
    open IS NULL or vol IS NULL").show()