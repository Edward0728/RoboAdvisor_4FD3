from numpy import percentile
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

import http.client
import pandas as pd
import time

browser = webdriver.Chrome(ChromeDriverManager().install())
usernameStr = 'yaoh17@mcmaster.ca'
passwordStr = 'Edward4FD3!'
date = '2022-11-12'  # we could get input for this value

browser.get('https://sec.theglobeandmail.com/user/login?intcmp=site-header')

browser.implicitly_wait(60)

username = browser.find_element_by_id('inputEmail')
username.send_keys(usernameStr)
password = browser.find_element_by_id('inputPassword')
password.send_keys(passwordStr)

browser.implicitly_wait(8)
SignInButton = browser.find_element_by_xpath('//button[normalize-space()="Log in"]')
SignInButton.click()
browser.implicitly_wait(60)

InvestingButton = browser.find_element_by_partial_link_text('INVESTING')
InvestingButton.click()
browser.implicitly_wait(8)

MARKETSButton = browser.find_element_by_partial_link_text('MARKETS')
MARKETSButton.click()
browser.implicitly_wait(8)

MutualFundsButton = browser.find_element_by_partial_link_text('STOCKS')
MutualFundsButton.click()
browser.implicitly_wait(8)

FulllistButton =  browser.find_element_by_partial_link_text('Full list')
FulllistButton.click()
browser.implicitly_wait(60)

Download_Main = browser.find_element_by_xpath('//button[normalize-space()="Download"]')
Download_Main.click()
time.sleep(10)

x = browser.find_element_by_id('dataTableDropdownSelect')
drop = Select(x)

drop.select_by_value('{"fields":"symbol,symbolName,lastPrice,percentChangeYtd,percentChange1m,percentChange3m,percentChange1y,highPrice1y,lowPrice1y"}')
browser.implicitly_wait(80)

Download_Performance = browser.find_element_by_xpath('//button[normalize-space()="Download"]')
Download_Performance.click()
time.sleep(10)
browser.implicitly_wait(8)

browser.close()

# PART 2
# this step need to be adjusted as file name changes from day to day.

#main_df = pd.read_csv(f'C:/Users/forfu/Downloads/funds-market-leaders-export-{date}.csv')
#performance_df = pd.read_csv(f'C:/Users/forfu/Downloads/funds-market-leaders-export-{date} (1).csv')
main_df = pd.read_csv(f'./Investment_Data/stocks-market-leaders-export-{date}.csv')
performance_df = pd.read_csv(f'./Investment_Data/stocks-market-leaders-export-{date}(1).csv')

both_df = pd.concat([performance_df[0:-1], main_df[['Change', '% Change', 'Price Volume','Time']][0:-1]], axis = 1)
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
    print(rating)
    rating_list.append(rating)

#print(risk_list)     
rating_dict = {'Rating': rating_list}      
rating_df = pd.DataFrame(rating_dict) 
all_df = pd.concat([both_df,rating_df], axis = 1)

#create size column
# size_list = []
# for i in all_df['Assets Under Management']:
#     #print(type(i))
#     #print(type(int(i[0:-1].replace(',',''))))
#     size = int(i[0:-1].replace(',',''))
#     if size >= 10000:
#         size_list.append('large')
#     elif size < 10000 and size >= 7500 :
#         size_list.append('medium')
#     else:
#         size_list.append('small')
# all_df['Size']= size_list

#create percentile column
percentile_list = []
for i in range(100):
    if i <=10:
        percentile_list.append('10%')
    elif i > 10 and i <= 15:
        percentile_list.append('15%')
    elif i > 15 and i <= 30:
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


