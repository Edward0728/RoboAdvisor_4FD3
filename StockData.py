# https://twelvedata.com/docs#profile
import requests


# url = 'https://api.twelvedata.com/earnings?symbol=AAPL&apikey=13142851cdfe4856bd76e5297106e00b'
# r = requests.get(url)
# data = r.json()
#   print(data)


def stockinfo_request(symbol):
    stock = symbol
    url = 'https://api.twelvedata.com/earnings?symbol=AAPL&apikey=13142851cdfe4856bd76e5297106e00b'
    r = requests.get(url)
    data = r.json()
    return data


print(stockinfo_request("AAPL"))