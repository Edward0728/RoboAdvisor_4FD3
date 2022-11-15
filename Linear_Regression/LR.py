import math
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn import linear_model

X = np.array([12, 20, 25, 36, 40, 50]).reshape(-1, 1)
#   y = [21, 40, 9, 18, 60, 61]
y = np.array([21, 40, 9, 18, 60, 61]).reshape(-1, 1)

model = linear_model.LinearRegression()
model.fit(X, y)
print("Model.intercept_:", model.intercept_)
print("Model.coef_:", model.coef_)

y_pred = model.predict(X)
first_pred = X[0][0] * model.coef_[0] + model.intercept_
print("first_pred:", first_pred)
print("y_pred[5]", y_pred[5])

#   model.intercept_


y_actual = [21, 40, 9, 18, 60, 61]
y_predicted = y_pred
MSE = np.square(np.subtract(y_actual, y_predicted)).mean()
print("Mean Square Error:\n", MSE)

X_beyond = np.array(range(1, 60))
X_beyond = X_beyond.reshape(-1, 1)
y_beyond_pred = model.predict(X_beyond)
print("y_beyond_pred", y_beyond_pred)

plt.scatter(X, y)
plt.plot(X, y_pred, 'r')
plt.show()
