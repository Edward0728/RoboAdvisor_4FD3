# Package Plan
import math
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from datetime import *

# generate the multi-step forecasts
def multi_step_forecasts(model, close_prices, x, y, n_past, n_future):

    x_past = x[-n_past - 1:, :, :][:1]  # last observed input sequence
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

    return df_past.join(df_future, how='outer')

#print(data)
model = load_model('LSTM_3.h5')

# 1. Acquire Stock Data Using API
stock_name = 'SU.TO '
start_date = '2016-01-01'
end_date = '2022-11-18'
stock_data = yf.download(f'{stock_name}', start= start_date, end=end_date)
stock_data.head()

# 2. Visualize Historical Stock Price
plt.figure(figsize=(15, 8))
plt.title(f'{stock_name} Stock Prices History')
plt.plot(stock_data['Close'])
plt.xlabel('Date')
plt.ylabel('Prices ($)')
# plt.show()

# 3. Prepare Training Data Set
close_prices = stock_data['Close']
#print('close_prices type: ', type(close_prices))
values = close_prices.values

# Use the Scikit-Learn MinMaxScaler to normalize all our stock data ranging from 0 to 1.
# We also reshape our normalized data into a two-dimensional array.
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(values.reshape(-1, 1))

window_size = 100

# 4. Prepare Test Data Set
test_data = scaled_data

# create feature data (x_test) and label data (y_test)from our test set
x_test = []
y_test = scaled_data
for i in range(window_size, len(test_data)):
  x_test.append(test_data[i-window_size:i, 0])

# Reshape again the x_test and y_test into a three-dimensional array
x_test = np.array(x_test)
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

# 7. Evaluate Model with RMSE
# predictions = model.predict(x_test)

# forecast the next 30 days
df1 = multi_step_forecasts(model, close_prices, x_test, y_test,n_past=0, n_future=60)
df1.plot(title=stock_name)

# forecast the last 20 days and the next 30 days
# df2 = multi_step_forecasts(model, close_prices, x_test, y_test, n_past=10, n_future=100)
# df2.plot(title=stock_name)
