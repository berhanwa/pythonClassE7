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

url = f""
