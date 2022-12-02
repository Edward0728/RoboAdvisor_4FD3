import http.client

conn = http.client.HTTPSConnection("api.webscrapingapi.com")

conn.request("GET", "/v1?url=https%3A%2F%2Fwww.theglobeandmail.com%2Finvesting%2Fmarkets%2Ffunds%2FRBF460.CF%2Ffundamentals%2F&api_key=L7xmlCPHedkoWw2PThNVMIAaJVuCRyGO&device=desktop&proxy_type=datacenter")

res = conn.getresponse()
data = res.read()

#print(data.decode("utf-8"))

Html_file= open("C:/Users/forfu/source/repos/Edward0728/RoboAdvisor_4FD3/Investment_Data/RBF460-CF.html","w")
Html_file.write(str(data))
Html_file.close()