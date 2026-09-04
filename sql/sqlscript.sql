-- creating the btc table 

con.sql("""
CREATE TABLE btc AS SELECT * FROM read_csv_auto('btc_daily.csv')
""")

con.sql("SELECT * FROM btc LIMIT 5").show()