from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

pyha_url = 'https://raw.githubusercontent.com/Mini-project-Team-Theta/team_theta/refs/heads/main/final/pyha_df.csv'
pyha_df = pd.read_csv(pyha_url)


x = pyha_df[['Year']]
y = pyha_df[['Snow depth mean [cm]']]
degree = 2
poly = PolynomialFeatures(degree=degree)
X_poly = poly.fit_transform(pyha_df[['Year']])

model = LinearRegression()
model.fit(X_poly,y)

future_years = np.array(range(2025,2035)).reshape(-1, 1) # predict 2025-2035
future_years_poly = poly.transform(future_years)

future_predictions = model.predict(future_years_poly)

plt.scatter(x, y, color="blue")
plt.plot(future_years, future_predictions, color="red")
plt.legend()
plt.show()

future_df = pd.DataFrame({'Year':future_years.flatten(),'Predicted value':future_predictions.flatten()})
print(future_predictions)
print(future_df)