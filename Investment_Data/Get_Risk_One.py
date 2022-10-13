import http.client

conn = http.client.HTTPSConnection("api.webscrapingapi.com")

conn.request("GET", "/v1?url=https%3A%2F%2Fwww.theglobeandmail.com%2Finvesting%2Fmarkets%2Ffunds%2FTDB306.CF%2Ffundamentals%2F&api_key=DBlmL7pZFYh6TNy71F8CR75fN0cPeT0y&device=desktop&proxy_type=datacenter")

res = conn.getresponse()
data = str(res.read())
print(type(data))

find = '<span class="black glyphicon glyphicon-chevron-up">'
risk_index = data.index(find)
index_1 = data[risk_index-60:risk_index].index('>')
index_2 = data[risk_index-60:risk_index].index('<')
print(index_1, index_2)
print(data[risk_index-60:risk_index][index_1+1:index_2].strip())


