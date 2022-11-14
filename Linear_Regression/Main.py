import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn import linear_model

#   x = [12, 20, 25, 36, 40, 50]
#   y = [21, 40, 9, 18, 60, 61]
#   plt.scatter(x, y)
#   plt.show()

theta = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
x = np.array([6, 7, 8, 9, 10]).reshape(-1, 1)

y_hat = np.dot(np.transpose(theta), x)

X = 5 * np.random.rand(10, 1)
y = np.random.randn(10, 1) + 10 + 7 * X

np.c_[np.array([12, 20, 25, 36, 40, 50]), np.array([21, 40, 9, 18, 60, 61])]

#   X.shape

X_c = np.c_[np.ones((10, 1)), X]
#   X_c[:5]

theta_best = np.linalg.inv(np.transpose(X_c).dot(X_c)).dot(X_c.T).dot(y)
#   theta_best

X_new = np.array([[10], [40]]) # Two random points
X_new_c = np.c_[np.ones((2, 1)), X_new] # Complete version of the feature vector
y_pred = X_new_c.dot(theta_best)

plt.plot(X_new, y_pred, "g-", label="Predictions")
plt.plot(X, y, "b.")
plt.axis([0, 60, 0, 60])
plt.show()

model = linear_model.LinearRegression()
model.fit(X, y)
print(model.intercept_)
print(model.coef_)
#   print(model.predict(X_new))
Predict_for_p5 = int(model.intercept_) + int(model.coef_)*50
print(Predict_for_p5)
Predict_for_60 = int(model.intercept_) + int(model.coef_)*60
print(Predict_for_60)
