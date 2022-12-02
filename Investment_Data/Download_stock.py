from numpy import percentile
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
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
time.sleep(10)

Download_Performance = browser.find_element_by_xpath('//button[normalize-space()="Download"]')
Download_Performance.click()
time.sleep(10)
browser.implicitly_wait(8)

browser.close()
