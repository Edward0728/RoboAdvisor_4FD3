# Package Plan
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from datetime import *

# generate the multi-step forecasts
def multi_step_forecasts(stock_ticker,n_past, n_future):

    model = load_model('LSTM_3.h5')
    # 1. Acquire Stock Data Using API
    stock_name = stock_ticker
    start_date = '2016-01-01'
    current_time = datetime.now()
    end_date = current_time.strftime('%Y-%m-%d')
    print(end_date)
    stock_data = yf.download(f'{stock_name}', start= start_date, end=end_date)
    current_price = stock_data['Close'][-1]
    print(current_price)
    #stock_data.head()

    # 2. Visualize Historical Stock Price
    plt.figure(figsize=(15, 8))
    plt.title(f'{stock_name} Stock Prices History')
    plt.plot(stock_data['Close'])
    plt.xlabel('Date')
    plt.ylabel('Prices ($)')
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
    return_rate = (df_all_time['Forecast'][-1] - current_price)/current_price
    #df_all_time.to_csv('prediction_60.csv')
    print(df_all_time['Forecast'][-1])

    return return_rate


date = '2022-12-01'  # we could get input for this value
stock_df = pd.read_csv(f'./Investment_Data/Stock_List.csv')
stock_list = stock_df['Symbol'].tolist()
stock_pred = []

for i in stock_list:
    stock_ticker = i[:-2]+'.TO'
    x = multi_step_forecasts(stock_ticker, 0, 60)
    print(stock_ticker,'return% in 60 days at ', x)
    stock_pred.append(x)

stock_df['Prediction_60'] =stock_pred
stock_df.to_csv('prediction_60.csv')

