import pandas as pd

pd.options.display.max_rows = 999
pd.set_option('display.max_rows',999)
pd.set_option('display.max_columns',999)
pd.set_option('display.width',1000)


#! Dunder methods are methods with __add__method (double underscore methods)

# a = 2+4    ## Here the PVM runs 2.__add__(4) in the background.
# print(a)

#! Index Alignment

#% make sure that the indexes:

#* Are unique (no duplicates)

#* Are common to both series

s1 = pd.Series([10,20,30], index=[1,2,2])
s2 = pd.Series([35,44,53], index=[2,2,4])

# print(s1)
# print(s2)

#! Note that index names 1 and 4 have NaN while index name 2 has four results—every 2 from s1 is matched up with every 2 from s2.
# print(s1+s2)

#~ 1     NaN
#~ 2    55.0
#~ 2    64.0
#~ 2    65.0
#~ 2    74.0
#~ 4     NaN
#~ dtype: float64


#! Broadcasting

#% Following codes will replaces the second series non matching indexes with 0. 

a = s1.add(s2, fill_value=0)

# print(a)

#~ 1    10.0
#~ 2    55.0
#~ 2    64.0
#~ 2    65.0
#~ 2    74.0
#~ 4    53.0
#~ dtype: float64

url = 'https://github.com/mattharrison/datasets/raw/master/data/vehicles.csv.zip'
df = pd.read_csv(url,low_memory=False)      ## when importing file from net, use 'low_memory = False'
city_mpg = df.city08
highway_mpg = df.highway08

b= ((city_mpg + highway_mpg)/2)

# print(b)


c = ((city_mpg.add(highway_mpg).div(2)))
# print(c)

print(s1.add(s1))
