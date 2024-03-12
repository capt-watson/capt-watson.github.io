import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame, Series

pd.options.display.max_rows = 999
pd.set_option('display.max_rows', 999)
pd.set_option('display.max_columns', 999)
pd.set_option('display.width', 1000)

url = 'https://github.com/mattharrison/datasets/raw/master/data/vehicles.csv.zip'
df = pd.read_csv(url)
city_mpg = df.city08
highway_mpg = df.highway08

print(city_mpg)

a = len(dir(city_mpg))

print(a)

#~ 421

#! The built-in dir function will list the attributes of an object. This shows that there are over 400 attributes on a series.
