
from numpy import percentile
import http.client
import pandas as pd
import time

date = '2022-12-02'  # we could get input for this value
# PART 2
# this step need to be adjusted as file name changes from day to day.

main_df = pd.read_csv(f'./Investment_Data/stocks-market-leaders-export-{date}.csv')
performance_df = pd.read_csv(f'./Investment_Data/stocks-market-leaders-export-{date} (1).csv')

both_df = pd.concat([performance_df, main_df[['Change', '% Change', 'Price Volume','Time']]], axis = 1)
symbol_list = both_df['Symbol'].values.tolist()
#print(len(symbol_list))

conn = http.client.HTTPSConnection("api.webscrapingapi.com")
rating_list = []
find = 'class=\"text\"><span>Current</span><span>'

for i in symbol_list:
    #conn.request("GET", "/v1?api_key=DBlmL7pZFYh6TNy71F8CR75fN0cPeT0y&device=desktop&proxy_type=datacenter&url=https%3A%2F%2Fwww.theglobeandmail.com%2Finvesting%2Fmarkets%2Ffunds%2F"+str(i)+"%2Ffundamentals%2F")
    conn.request("GET", "/v1?api_key=DBlmL7pZFYh6TNy71F8CR75fN0cPeT0y&device=desktop&proxy_type=datacenter&url=https%3A%2F%2Fwww.theglobeandmail.com%2Finvesting%2Fmarkets%2Fstocks%2F"+str(i)+"%2Fresearch%2F")
                                     
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
    rating = data[rating_index-28:rating_index-24].strip()
    print(i, 'rating: ', rating)
    rating_list.append(rating)

#print(risk_list)     
rating_dict = {'Rating': rating_list}      
rating_df = pd.DataFrame(rating_dict) 
all_df = pd.concat([both_df,rating_df], axis = 1)

#create percentile column
percentile_list = []
for i in range(100):
    if i <10:
        percentile_list.append('10%')
    elif i >= 10 and i < 15:
        percentile_list.append('15%')
    elif i >= 15 and i < 30:
        percentile_list.append('30%')
    else:
        percentile_list.append('None')

all_df = all_df.sort_values(by=['YTD %Change'], ascending=False)
all_df['Percentile'] = percentile_list

#create volatility column
volatility_list = []
volatility_list = all_df['52-Week High']/all_df['52-Week Low']-1
all_df['Volatility'] =  volatility_list

    
# saving the dataframe 
all_df.to_csv(f'./Investment_Data/stocks_{date}.csv') 


