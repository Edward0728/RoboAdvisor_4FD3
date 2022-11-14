import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn import linear_model

honey = pd.read_csv('/Users/qinyang/PycharmProjects/Linear_Regression/honeyproduction.csv')
honey.head()

honey.info()
honey['year'].value_counts()

production_per_year = honey.groupby('year').totalprod.mean().reset_index()

X = production_per_year['year']
X = X.values.reshape(-1, 1)

y = production_per_year['totalprod']

model = linear_model.LinearRegression()
model.fit(X, y)
print("Model.coef_:", model.coef_)
print("Model.intercept_:", model.intercept_)

y_pred = model.predict(X)
first_pred = X[0][0] * model.coef_[0] + model.intercept_
print("first_pred:", first_pred)
print("y_pred[0]", y_pred[0])

#   model.intercept_

X_beyond = np.array(range(2013, 2021))
X_beyond = X_beyond.reshape(-1, 1)
y_beyond_pred = model.predict(X_beyond)
print(y_beyond_pred)

plt.scatter(X, y)
plt.plot(X, y_pred, 'r')
plt.xlabel('Year')
plt.ylabel('Honey Production')
plt.show()
