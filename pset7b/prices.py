import csv
import os
import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Usage: python quote.py STOCK-SYMBOL")
symbol = sys.argv[1]

# Get API_KEY
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    sys.exit("Missing API_KEY")

url = f"https://www.alphavantage.co/query?apikey={TVAWRB3X4K3B6Y0G}&datatype=csv&function=TIME_SERIES_INTRADAY&interval=5min&symbol={symbol}"
response = requests.get(url)
print(response.txt)

reader = csv.DictReader(response.text.splitlines())

row = next(reader)
print(row)
print(f"${row["close"]}")
