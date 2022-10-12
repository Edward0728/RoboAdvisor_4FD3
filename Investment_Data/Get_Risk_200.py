import http.client
import pandas as pd

main_df = pd.read_csv(r'C:/Users/forfu/Downloads/funds-market-leaders-export-2022-10-10.csv')
performance_df = pd.read_csv(r'C:/Users/forfu/Downloads/funds-market-leaders-export-2022-10-10 (6).csv')

both_df = pd.concat([performance_df, main_df[['Change', '% Change', 'Assets Under Management','Time']]], axis = 1)
#all_df.to_csv('C:/Users/forfu/Downloads/both_funds.csv')
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
    #print(type(data))
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
# dictionary of lists  
risk_dict = {'risk': risk_list}      
risk_df = pd.DataFrame(risk_dict) 
all_df = pd.concat([both_df,risk_df], axis = 1)
    
# saving the dataframe 
all_df.to_csv('C:/Users/forfu/Downloads/all_funds_data_2.csv') 


