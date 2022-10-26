import json
import pandas as pd
# Change the CSV file address to your CSV file path
#mutualFund_CSV = pd.read_csv (r'/Users/qinyang/PycharmProjects/RoboAdvisor/Investment_Data/all_funds_data.csv')
mutualFund_CSV = pd.read_csv (r'C:/Users/forfu/source/repos/Edward0728/RoboAdvisor_4FD3/Investment_Data/all_funds_data.csv')
size_list = []
print(type((mutualFund_CSV['Assets Under Management'][0][0:-1].replace(',', ''))))

for i in mutualFund_CSV['Assets Under Management']:
    #print(type(i))
    #print(type(int(i[0:-1].replace(',',''))))
    size = int(i[0:-1].replace(',',''))
    if size >= 10000:
        size_list.append('Large')
    elif size < 10000 and size >= 7500 :
        size_list.append('Medium')
    else:
        size_list.append('Small')
mutualFund_CSV['Size']= size_list

#create percentile column
percentile_list = []
for i in range(200):
    if i <=20:
        percentile_list.append('10%')
    elif i > 20 and i <= 30:
        percentile_list.append('15%')
    elif i > 30 and i <= 60:
        percentile_list.append('30%')
    else:
        percentile_list.append('None')

mutualFund_CSV = mutualFund_CSV.sort_values(by=['YTD %Change'], ascending=False)
mutualFund_CSV['Percentile'] = percentile_list

#create volatility column
volatility_list = []

volatility_list = mutualFund_CSV['52-Week High']/mutualFund_CSV['52-Week Low']-1

mutualFund_CSV['Volatility'] =  volatility_list


# saving the dataframe 
mutualFund_CSV.to_csv(f'./Investment_Data/funds_volatility.csv') 