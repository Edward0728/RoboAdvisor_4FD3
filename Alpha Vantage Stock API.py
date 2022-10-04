# Acquire Data from Alpha Vantage Stock API

# API key: AEGJDU540F597MXQ
# https://www.alphavantage.co/documentation/

import requests

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=AEGJDU540F597MXQ'
r = requests.get(url)
data = r.json()

print(data)

# hello edward
