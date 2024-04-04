import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor

data_root = 'https://github.com/ageron/data/raw/main/'
lifesat = pd.read_csv(data_root + 'lifesat/lifesat.csv')
x = lifesat[["GDP per capita (USD)"]].values
y = lifesat[["Life satisfaction"]].values

## Visualize the data
lifesat.plot(kind='scatter', grid=True, x='GDP per capita (USD)', y= 'Life satisfaction')

plt.axis([23_500, 62_500,4,9])
plt.show()

## select a linear model
model = LinearRegression()

## Train the model
model.fit(x,y)

## make a prediction for Cyprus
x_new = [[37_655.2]] ## cyprus GDP per capita in 2020
print(model.predict(x_new))

#~ [[6.30165767]] ## Shows life satisfaction with of GDP 37,655.2


data_root = 'https://github.com/ageron/data/raw/main/'
lifesat = pd.read_csv(data_root + 'lifesat/lifesat.csv')
x = lifesat[["GDP per capita (USD)"]].values
y = lifesat[["Life satisfaction"]].values

## Visualize the data
lifesat.plot(kind='scatter', grid=True, x='GDP per capita (USD)', y= 'Life satisfaction')

plt.axis([23_500, 62_500,4,9])
plt.show()


## select a linear model
model = KNeighborsRegressor()

## Train the model
model.fit(x,y)

## make a prediction for Cyprus
x_new = [[37_655.2]] ## cyprus GDP per capita in 2020
print(model.predict(x_new))
