from datetime import *
# date_int = (int(x) for x in '2017-01-01'.split('-'))
# print(type(date(int(x) for x in '2017-01-01'.split('-'))))
#print(type(date(date_int[1],date_int[2], date_int[3])))

stock_name = 'ENB.TO '
start_date = '2016-01-01'
end_date = '2022-11-18'
start_date_nse = datetime.strptime(start_date.replace('-', ''), '%Y%m%d')
end_date_nse = datetime.strptime(end_date.replace('-', ''), '%Y%m%d')

print(start_date_nse, end_date_nse)