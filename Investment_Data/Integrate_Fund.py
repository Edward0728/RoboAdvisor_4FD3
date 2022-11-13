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
date = '2022-10-25'  # we could get input for this value

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

MutualFundsButton = browser.find_element_by_partial_link_text('MUTUAL FUNDS')
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
browser.implicitly_wait(60)

Download_Performance = browser.find_element_by_xpath('//button[normalize-space()="Download"]')
Download_Performance.click()
time.sleep(10)
browser.implicitly_wait(8)

browser.close()

# PART 2
# this step need to be adjusted as file name changes from day to day.

#main_df = pd.read_csv(f'C:/Users/forfu/Downloads/funds-market-leaders-export-{date}.csv')
#performance_df = pd.read_csv(f'C:/Users/forfu/Downloads/funds-market-leaders-export-{date} (1).csv')
main_df = pd.read_csv(f'./Investment_Data/funds-market-leaders-export-{date}.csv')
performance_df = pd.read_csv(f'./Investment_Data/funds-market-leaders-export-{date} (1).csv')

both_df = pd.concat([performance_df, main_df[['Change', '% Change', 'Assets Under Management','Time']]], axis = 1)
symbol_list = both_df['Symbol'].values.tolist()
#print(len(symbol_list))

conn = http.client.HTTPSConnection("api.webscrapingapi.com")
risk_list = []
find = '<span class="black glyphicon glyphicon-chevron-up">'

for i in symbol_list[0:-151]:
    #conn.request("GET", "/v1?api_key=DBlmL7pZFYh6TNy71F8CR75fN0cPeT0y&device=desktop&proxy_type=datacenter&url=https%3A%2F%2Fwww.theglobeandmail.com%2Finvesting%2Fmarkets%2Ffunds%2F"+str(i)+"%2Ffundamentals%2F")
    conn.request("GET", "/v1?api_key=iE03XeiH0a2FPOaRz2EffEfFVhI7tOmb&device=desktop&proxy_type=datacenter&url=https%3A%2F%2Fwww.theglobeandmail.com%2Finvesting%2Fmarkets%2Ffunds%2F"+str(i)+"%2Ffundamentals%2F")
    
    #conn.request("GET", "/v1?url=https%3A%2F%2Fwww.theglobeandmail.com%2Finvesting%2Fmarkets%2Ffunds%2FTDB2766.CF%2Ffundamentals%2F&api_key=DBlmL7pZFYh6TNy71F8CR75fN0cPeT0y&device=desktop&proxy_type=datacenter")
    #time.sleep(3)
    res = conn.getresponse()
    #time.sleep(3)
    data = str(res.read())
    try:
        risk_index = data.index(find)
    except:
        risk_list.append('None')
        print('None')
        continue
    index_1 = data[risk_index-60:risk_index].index('>')
    index_2 = data[risk_index-60:risk_index].index('<')
    #print(index_1, index_2)
    risk = data[risk_index-60:risk_index][index_1+1:index_2].strip()
    print(risk)
    risk_list.append(risk)

#print(risk_list)     
risk_dict = {'risk': risk_list}      
risk_df = pd.DataFrame(risk_dict) 
all_df = pd.concat([both_df,risk_df], axis = 1)

#create size column
size_list = []
for i in all_df['Assets Under Management']:
    #print(type(i))
    #print(type(int(i[0:-1].replace(',',''))))
    size = int(i[0:-1].replace(',',''))
    if size >= 10000:
        size_list.append('large')
    elif size < 10000 and size >= 7500 :
        size_list.append('medium')
    else:
        size_list.append('small')
all_df['Size']= size_list

#create percentile column
percentile_list = []
for i in range(200):
    if i <20:
        percentile_list.append('10%')
    elif i >= 20 and i < 30:
        percentile_list.append('15%')
    elif i >= 30 and i < 60:
        percentile_list.append('30%')
    else:
        percentile_list.append('None')

all_df = all_df.sort_values(by=['YTD %Change'], ascending=False)
all_df['Percentile'] = percentile_list

#create volatility column
volatility_list = []
volatility_list = all_df['52-Week High']/all_df['52-Week Low']-1
all_df = all_df['Volatility'] =  volatility_list

    
# saving the dataframe 
all_df.to_csv(f'./Investment_Data/funds_{date}.csv') 


