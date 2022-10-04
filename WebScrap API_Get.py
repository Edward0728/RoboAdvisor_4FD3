# use Webscrap API to list mutual funds in certain risk level
# API key is:  L7xmlCPHedkoWw2PThNVMIAaJVuCRyGO
# https://docs.webscrapingapi.com/webscrapingapi/basic-api-requests/get-request

# Get Request
# GET carries request parameter appended in URL string

import requests

API_KEY = 'L7xmlCPHedkoWw2PThNVMIAaJVuCRyGO'
SCRAPER_URL = 'https://api.webscrapingapi.com/v1'

TARGET_URL = 'https://httpbin.org/post'

PARAMS = {
    "api_key":API_KEY,
    "url": TARGET_URL,
}

response = requests.get(SCRAPER_URL, params=PARAMS)

print(response)