# Acquire Data from Alpha Vantage Stock API

# API key: AEGJDU540F597MXQ
# https://www.alphavantage.co/documentation/

import requests

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=TOU-T&interval=5min&apikey=MFCI9CTBFDHTPF7Y'
r = requests.get(url)
data = r.json()

print(data)

# hello edward
