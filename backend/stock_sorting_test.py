import os
import pandas as pd
# Package Plan
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
from datetime import *

# generate the multi-step forecasts
def multi_step_forecasts(stock_ticker,n_past = 0, n_future = 60):

    model = load_model('LSTM_3.h5')
    # 1. Acquire Stock Data Using API
    stock_name = stock_ticker
    start_date = '2016-01-01'
    current_time = datetime.now()
    end_date = current_time.strftime('%Y-%m-%d')
    stock_data = yf.download(f'{stock_name}', start= start_date, end=end_date)
    current_price = stock_data['Close'][-1]
    print('Current price:', current_price)
    #stock_data.head()

    # 2. Visualize Historical Stock Price
    # plt.figure(figsize=(15, 8))
    # plt.title(f'{stock_name} Stock Prices History')
    # plt.plot(stock_data['Close'])
    # plt.xlabel('Date')
    # plt.ylabel('Prices ($)')
    # plt.show()

    # 3. Prepare Training Data Set
    close_prices = stock_data['Close']
    values = close_prices.values

    # Use the Scikit-Learn MinMaxScaler to normalize all our stock data ranging from 0 to 1.
    # We also reshape our normalized data into a two-dimensional array.
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(values.reshape(-1, 1))
    window_size = 100

    # 4. Prepare historical Data Set used for prediction
    history_data = scaled_data

    # create feature data (x_into_model) and label data (y_test)from our test set
    x_into_model = []
    y = history_data
    for i in range(window_size, len(history_data)):
        x_into_model.append(history_data[i-window_size:i, 0])

    # Reshape again the x_into_model and y_test into a three-dimensional array
    x_into_model = np.array(x_into_model)
    x_into_model = np.reshape(x_into_model, (x_into_model.shape[0], x_into_model.shape[1], 1))

    x_past = x_into_model[-n_past - 1:, :, :][:1]  # last observed input sequence
    y_past = y[-n_past - 1]             # last observed target value
    y_future = []                        # predicted target values

    for i in range(n_past + n_future):

        # feed the last forecast back to the model as an input
        x_past = np.append(x_past[:, 1:, :], y_past.reshape(1, 1, 1), axis=1)

        # generate the next forecast
        y_past = model.predict(x_past)

        # save the forecast
        y_future.append(y_past.flatten()[0])

    # transform the forecasts back to the original scale
    y_future = scaler.inverse_transform(np.array(y_future).reshape(-1, 1)).flatten()

    # add the forecasts to the data frame

    df_past = pd.DataFrame(
        data=close_prices
    )

    df_future = pd.DataFrame(
        index=pd.bdate_range(start=close_prices.index[- n_past - 1] + pd.Timedelta(days=1), periods=n_past + n_future),
        columns=['Forecast'],
        data=y_future
    )

    df_all_time = df_past.join(df_future, how='outer')
    print('Price in 60 days: ', df_all_time['Forecast'][-1] )
    return_rate = (df_all_time['Forecast'][-1] - current_price)/current_price
    #df_all_time.to_csv('prediction_60.csv')
    print(stock_ticker, 'return rate in 60 days: ', return_rate)

    return return_rate


def stock_solution(rating_stock):
#def final_solution(rating_stock,size_stock,rank_stock,volatility_stock):
    solution_rate = []
    solution=[]
    print(rating_stock)
    for i in rating_stock:
        stock_ticker = i[:-2]+'.TO'
        print(stock_ticker)
        x = multi_step_forecasts(stock_ticker.strip())
        solution_rate.append((i,x))
        def rate(stock):
            return stock[1]      
        solution_rate.sort(key = rate, reverse=True)
        print(solution_rate)
    for i in solution_rate:
        solution.append(i[0])
    #print('stock solution: ', solution)
    if len(solution) >= 10:
        return solution[0:10]
    elif len(solution) > 0 and len(solution) < 10:
        return solution
    else:
        return(['no', 'stock', 'found'])    

dirname = os.path.dirname(__file__)
# Change the CSV file address to your CSV file path
#mutualFund_CSV = pd.read_csv (r'/Users/qinyang/PycharmProjects/RoboAdvisor/Investment_Data/all_funds_data.csv')

sortingStock = pd.read_csv('./Investment_Data/stock_sorting_test.csv')['Symbol'].tolist()
print('sortingStock: ', sortingStock)

result = stock_solution(sortingStock)
print(result)