from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome(ChromeDriverManager().install())
usernameStr = 'yaoh17@mcmaster.ca'
passwordStr = '**********'

browser.get('https://sec.theglobeandmail.com/user/login?intcmp=site-header')

browser.implicitly_wait(5)
# fill in username and hit the next button
username = browser.find_element_by_id('inputEmail')
username.send_keys(usernameStr)
password = browser.find_element_by_id('inputPassword')
password.send_keys(passwordStr)

browser.implicitly_wait(5)
SignInButton = browser.find_element_by_xpath('//button[normalize-space()="Log in"]')
SignInButton.click()
browser.implicitly_wait(5)

#InvestingButton = browser.find_element_by_xpath('//button[normalize-space()="INVESTING"]')
InvestingButton = browser.find_element_by_partial_link_text('INVESTING')
InvestingButton.click()
browser.implicitly_wait(5)

MARKETSButton = browser.find_element_by_partial_link_text('MARKETS')
MARKETSButton.click()
browser.implicitly_wait(5)

MutualFundsButton = browser.find_element_by_partial_link_text('MUTUAL FUNDS')
MutualFundsButton.click()
browser.implicitly_wait(8)

FulllistButton =  browser.find_element_by_partial_link_text('Full list')
FulllistButton.click()
browser.implicitly_wait(5)

Download_Main = browser.find_element_by_xpath('//button[normalize-space()="Download"]')
Download_Main.click()
  
# Find id of option
x = browser.find_element_by_id('dataTableDropdownSelect')
drop = Select(x)
  
# Select by value
drop.select_by_value('{"fields":"symbol,symbolName,lastPrice,percentChangeYtd,percentChange1m,percentChange3m,percentChange1y,highPrice1y,lowPrice1y"}')
browser.implicitly_wait(8)

Download_Performance = browser.find_element_by_xpath('//button[normalize-space()="Download"]')
Download_Performance.click()
browser.implicitly_wait(10)

browser.close()