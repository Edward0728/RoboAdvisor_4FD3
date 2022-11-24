from numpy import percentile
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

import http.client
import pandas as pd
import time

date = '2022-11-12'

main_df = pd.read_csv(f'./Investment_Data/stocks-market-leaders-export-{date}.csv')
performance_df = pd.read_csv(f'./Investment_Data/stocks-market-leaders-export-{date}(1).csv')

both_df = pd.concat([performance_df[0:5], main_df[['Change', '% Change', 'Price Volume','Time']][0:5]], axis = 1)
symbol_list = both_df['Symbol'].values.tolist()

conn = http.client.HTTPSConnection("api.webscrapingapi.com")
rating_list = []
find = 'class=\"text\"><span>Current</span><span>'


for i in symbol_list:
    #conn.request("GET", "/v1?api_key=DBlmL7pZFYh6TNy71F8CR75fN0cPeT0y&device=desktop&proxy_type=datacenter&url=https%3A%2F%2Fwww.theglobeandmail.com%2Finvesting%2Fmarkets%2Ffunds%2F"+str(i)+"%2Ffundamentals%2F")
    conn.request("GET", "/v1?api_key=iE03XeiH0a2FPOaRz2EffEfFVhI7tOmb&device=desktop&proxy_type=datacenter&url=https%3A%2F%2Fwww.theglobeandmail.com%2Finvesting%2Fmarkets%2Fstocks%2F"+str(i)+"%2Fresearch%2F")
    
    #conn.request("GET", "/v1?url=https%3A%2F%2Fwww.theglobeandmail.com%2Finvesting%2Fmarkets%2Ffunds%2FTDB2766.CF%2Ffundamentals%2F&api_key=DBlmL7pZFYh6TNy71F8CR75fN0cPeT0y&device=desktop&proxy_type=datacenter")
    #time.sleep(3)
    res = conn.getresponse()
    #time.sleep(3)
    data = str(res.read())
    try:
        rating_index = data.index(find)
    except:
        rating_list.append('None')
        print('None')
        continue
    # index_1 = data[rating_index-24:rating_index].index('>')
    # index_2 = data[rating_index-27:rating_index].index('<')
    #print(index_1, index_2)
    rating = float(data[rating_index-28:rating_index-24].strip())
    print(rating)
    rating_list.append(rating)

#print(risk_list)     
rating_dict = {'Rating': rating_list}      
rating_df = pd.DataFrame(rating_dict) 
print(rating_df)
all_df = pd.concat([both_df,rating_df], axis = 1)
print(all_df)

percentile_list = []
for i in range(5):
    if i <=1:
        percentile_list.append('20%')
    elif i > 1 and i <= 2:
        percentile_list.append('40%')
    elif i > 2 and i <= 3:
        percentile_list.append('60%')
    else:
        percentile_list.append('None')

all_df = all_df.sort_values(by=['YTD %Change'], ascending=False)
all_df['Percentile'] = percentile_list

print(all_df)
print(type(c) for c in all_df.columns)

#create volatility column
volatility_list = []
volatility_list = all_df['52-Week High']/all_df['52-Week Low']-1
all_df['Volatility'] =  volatility_list

print(all_df)
print(type(c) for c in all_df.columns)
    
# saving the dataframe 
all_df.to_csv(f'./Investment_Data/test_stocks_{date}.csv') 