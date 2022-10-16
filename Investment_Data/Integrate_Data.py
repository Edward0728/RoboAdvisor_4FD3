from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

import http.client
import pandas as pd

browser = webdriver.Chrome(ChromeDriverManager().install())
usernameStr = 'yaoh17@mcmaster.ca'
passwordStr = 'Edward4FD3!'

browser.get('https://sec.theglobeandmail.com/user/login?intcmp=site-header')

browser.implicitly_wait(8)

username = browser.find_element_by_id('inputEmail')
username.send_keys(usernameStr)
password = browser.find_element_by_id('inputPassword')
password.send_keys(passwordStr)

browser.implicitly_wait(8)
SignInButton = browser.find_element_by_xpath('//button[normalize-space()="Log in"]')
SignInButton.click()
browser.implicitly_wait(88)

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
browser.implicitly_wait(8)

Download_Main = browser.find_element_by_xpath('//button[normalize-space()="Download"]')
Download_Main.click()

x = browser.find_element_by_id('dataTableDropdownSelect')
drop = Select(x)

drop.select_by_value('{"fields":"symbol,symbolName,lastPrice,percentChangeYtd,percentChange1m,percentChange3m,percentChange1y,highPrice1y,lowPrice1y"}')
browser.implicitly_wait(8)

Download_Performance = browser.find_element_by_xpath('//button[normalize-space()="Download"]')
Download_Performance.click()
browser.implicitly_wait(10)

browser.close()

# PART 2
# this step need to be adjusted as file name changes from day to day.
main_df = pd.read_csv(r'C:/Users/forfu/Downloads/funds-market-leaders-export-2022-10-10.csv')
performance_df = pd.read_csv(r'C:/Users/forfu/Downloads/funds-market-leaders-export-2022-10-10 (6).csv')

both_df = pd.concat([performance_df, main_df[['Change', '% Change', 'Assets Under Management','Time']]], axis = 1)
symbol_list = both_df['Symbol'].values.tolist()
#print(len(symbol_list))

conn = http.client.HTTPSConnection("api.webscrapingapi.com")
risk_list = []
find = '<span class="black glyphicon glyphicon-chevron-up">'

for i in symbol_list[0:-1]:
    conn.request("GET", "/v1?url=https%3A%2F%2Fwww.theglobeandmail.com%2Finvesting%2Fmarkets%2Ffunds%2F"+str(i)+"%2Ffundamentals%2F&api_key=DBlmL7pZFYh6TNy71F8CR75fN0cPeT0y&device=desktop&proxy_type=datacenter")
    #conn.request("GET", "/v1?url=https%3A%2F%2Fwww.theglobeandmail.com%2Finvesting%2Fmarkets%2Ffunds%2FTDB2766.CF%2Ffundamentals%2F&api_key=DBlmL7pZFYh6TNy71F8CR75fN0cPeT0y&device=desktop&proxy_type=datacenter")
    res = conn.getresponse()
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
    
# saving the dataframe 
all_df.to_csv('C:/Users/forfu/Downloads/all_funds_data_2.csv') 


