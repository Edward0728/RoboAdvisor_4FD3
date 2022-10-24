# https://twelvedata.com/docs#profile
# twelvedata API key: 13142851cdfe4856bd76e5297106e00b
# Alphavantage API key: AEGJDU540F597MXQ

import requests

def stockinfo_request(symbol):
    stock = symbol

#    url ="https://api.twelvedata.com/earnings?symbol=" + stock + "&apikey=13142851cdfe4856bd76e5297106e00b"
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY' \
          '&symbol=' + stock + '&apikey=AEGJDU540F597MXQ'
#    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=TLSA&interval=5min&apikey=demo'

    r = requests.get(url)
    data = r.json()
    return data
