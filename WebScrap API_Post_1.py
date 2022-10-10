# use Webscrap API to list mutual funds in certain risk level
# API key is:  L7xmlCPHedkoWw2PThNVMIAaJVuCRyGO
# https://docs.webscrapingapi.com/webscrapingapi/basic-api-requests/post-and-put-requests

# Post Request
# POST carries request parameter in message body

import requests

API_KEY = 'L7xmlCPHedkoWw2PThNVMIAaJVuCRyGO'
SCRAPER_URL = 'https://api.webscrapingapi.com/v1'

TARGET_URL = 'https://httpbin.org/post'

PARAMS = {
    "api_key":API_KEY,
    "url": TARGET_URL,
}

HEADERS = {
    'WSA-Content-Type':'application/json',
    'WSA-Accept':'application/json'
}

DATA = {
    "query":"\\n mutation {\\n createCartItem(\\n \\n menuItemId: \\\ '105097698\\\'\\n …\\n \)} \""
}

response = requests.post(SCRAPER_URL, data=DATA, params=PARAMS, headers=HEADERS)

print(response.text)