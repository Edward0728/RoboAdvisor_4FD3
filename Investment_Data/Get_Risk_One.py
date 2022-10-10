import requests
import datetime


#from beautifulsoup4 import BeautifulSoup

import http.client

conn = http.client.HTTPSConnection("api.webscrapingapi.com")

conn.request("GET", "/v1?url=https%3A%2F%2Fwww.theglobeandmail.com%2Finvesting%2Fmarkets%2Ffunds%2FTDB306.CF%2Ffundamentals%2F&api_key=DBlmL7pZFYh6TNy71F8CR75fN0cPeT0y&device=desktop&proxy_type=datacenter")

res = conn.getresponse()
data = str(res.read())
print(type(data))
#print(data.decode("utf-8"))

# Html_file= open("C:/Users/forfu/source/repos/Edward0728/RoboAdvisor_4FD3/Investment_Data/RBF460-CF.html","w")
# Html_file.write(str(data))
# Html_file.close()
#now =datetime.datetime.now()

find = '<span class="black glyphicon glyphicon-chevron-up">'
risk_index = data.index(find)
index_1 = data[risk_index-60:risk_index].index('>')
index_2 = data[risk_index-60:risk_index].index('<')
print(index_1, index_2)
print(data[risk_index-60:risk_index][index_1+1:index_2].strip())

#url = 'http://www.basketball-reference.com/boxscores/index.cgi?lid=header_dateoutput&month={0}&day=17&year={2}'.format(cmonth,cday,cyear)
#response = requests.get(url)
# html = response.content
# print(html)

