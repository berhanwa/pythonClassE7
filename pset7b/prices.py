# Based a lot of this program structure from the class file quote.py
import csv
import os
import requests
import sys

# Checked for the appropriate formatting from the command line and specified what it was if the length of input was not long enough
if len(sys.argv) != 2:
    sys.exit("Usage: python quote.py STOCK-SYMBOL")
symbol = sys.argv[1]

# Get API_KEY
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    sys.exit("Missing API_KEY")

# With the API, accessed the stock data as a csv file
url = f"https://www.alphavantage.co/query?apikey={API_KEY}&datatype=csv&function=TIME_SERIES_INTRADAY&interval=5min&symbol={symbol}"
response = requests.get(url)
print(response.text)

# Parsed the reader
reader = csv.DictReader(response.text.splitlines())

# Print most recent price and the next line of the file
row = next(reader)
print(row)
print(f"${row["close"]}")
