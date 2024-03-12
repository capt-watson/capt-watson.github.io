import numpy as np
import pandas as pd




pd.options.display.max_rows = 999
pd.set_option('display.max_rows',999)
pd.set_option('display.max_columns',999)
pd.set_option('display.width',1000)

#! Aggregations

#% Aggregation method is ,mean is used to calculate mean value of a series.

url = 'https://github.com/mattharrison/datasets/raw/master/data/vehicles.csv.zip'
df = pd.read_csv(url,low_memory=False)      ## when importing file from net, use 'low_memory = False'
city_mpg = df.city08
highway_mpg = df.highway08

# print(city_mpg.mean())

#~ 18.369045304297103

# print(city_mpg.is_unique)
#~ False

# print(city_mpg.is_monotonic_increasing)
#~ False

# city_mpg.quantile()
#~ 17.0

# city_mpg.quantile(.9)
#~ 24.0

# city_mpg.quantile([.1, .5, .9])
#~ 0.1    13.0
#~ 0.5    17.0
#~ 0.9    24.0

#! Count and Mean of an Attribute

# city_mpg.gt(20).sum()       ## here 'gt()' method returns greater than given value. sum() method returns total of those values meeting criteria.
10272

city_mpg.gt(20).mul(100).mean()
## here 'mul' means to multiply and mean is avg in statistics

def sec_to_last(s):
    return s.iloc[-2]

# city_mpg.agg(['mean',np.var, max, sec_to_last])

data = np.array(['g','e','e','k','s'])

c = pd.Series(data)
# print(c)

data = np.array(['g','e','e','k','s','f', 'o','r','g','e','e','k','s'])
d = pd.Series(data, index=[10,11,12,13,14,15,16,17,18,19,20,21,22])

print(d[16])

#% The head() method returns a specified number of rows, string from the top.

#% The head() method returns the first 5 rows if a number is not specified.


#! pd.loc[] uses the provided index to extract the desired data row by row.

#! pd.iloc[] uses the built-in index to extract the desired data row by row.

