import numpy as np
import pandas as pd

pd.options.display.max_rows = 999
pd.set_option('display.max_rows',999)
pd.set_option('display.max_columns',999)
pd.set_option('display.width',1000)

url = 'https://github.com/mattharrison/datasets/raw/master/data/vehicles.csv.zip'
df = pd.read_csv(url,low_memory=False) 

city_mpg = df.city08
highway_mpg = df.highway08

city_mpg.convert_dtypes()

city_mpg.astype('int16')

city_mpg.astype('int8')

## Using the correct type can save significant amounts of memory.

## If you can use a narrower type, you can cut back on memory usage, giving you memory to process more data.

## use NumPy to inspect limits on integer and float types:

# np.iinfo('int64')
#~ iinfo(min=-9223372036854775808, max=9223372036854775807, dtype=int64)

# np.iinfo('uint8')
#~ iinfo(min=0, max=255, dtype=uint8)

# np.finfo('float16')
#~ finfo(resolution=0.001, min=-6.55040e+04, max=6.55040e+04, dtype=float16)

np.finfo('float64')
#~ info(resolution=1e-15, min=-1.7976931348623157e+308, max=1.7976931348623157e+308, dtype=float64)


#! Memory Usage

## Using .nbytes with object types only shows how much memory the Pandas object is taking.

# city_mpg.nbytes
#~ 329152

# city_mpg.astype('int16').nbytes
#! 82288

## o get the amount of memory that includes the strings, we need to use the .memory_usage method:

make = df.make
make.nbytes
#~ 329152

# make.memory_usage()     ## Difference in output is due to the inclusion of the strings
#~ 329284


#! index  True|False  Optional. Default True. Specifies whether include the index (and its memory usage) or not

# make.memory_usage(index=False)  #@ This output is without checking memory usage by the index
#~ 329152

#! deep True|False Default False   If True the systems finds the actual system-level memory consumption to do a real calculation of the memory usage (at a high computer resource cost) instead of an estimate based on dtypes and number of rows (lower cost).

# make.memory_usage(deep=True)
#! 2277247


#! By converting to a categorical, one can save a lot of memory.

# make.astype ('category').memory_usage(deep=True)
#! 94804

#% String and Category Types

#* The .astype method can also convert numeric series to strings if you pass str into it.

# city_mpg.astype(str)

#~ 0        19
#~ 1         9
#~ 2        23
#~ 3        10
#~ 4        17
#~          ..
#~ 41139    19
#~ 41140    20
#~ 41141    18
#~ 41142    18
#~ 41143    16
#~ Name: city08, Length: 41144, dtype: object

#* To convert to a categorical type, you can pass in 'category' as a type:

# city_mpg.astype('category')

#~ 0        19
#~ 1         9
#~ 2        23
#~ 3        10
#~ 4        17
#~          ..
#~ 41139    19
#~ 41140    20
#~ 41141    18
#~ 41142    18
#~ 41143    16
#~ Name: city08, Length: 41144, dtype: category
#~ Categories (105, int64): [6, 7, 8, 9, ..., 137, 138, 140, 150]

#% Python strings when you have string data. When you convert it to categorical data, pandas no longer uses Python strings for each value but optimizes it, so repeating values are not duplicated.

#! Ordered Categories

#% To create ordered categories, you need to define your own CategoricalDtype:

#! Conversion Methods

values = pd.Series(sorted(set(city_mpg)))

city_type = pd.CategoricalDtype(categories=values, ordered=True)
city_mpg.astype(city_type)

#~ 0        19
#~ 1         9
#~ 2        23
#~ 3        10
#~ 4        17
#~          ..
#~ 41139    19
#~ 41140    20
#~ 41141    18
#~ 41142    18
#~ 41143    16
#~ Name: city08, Length: 41144, dtype: category
#~ Categories (105, int64): [6 < 7 < 8 < 9 ... 137 < 138 < 140 < 150]

#! use the .to_frame method to get a dataframe with a single column:

city_mpg.to_frame()

#~ 	city08
#~ 0	19
#~ 1	9
#~ 2	23
#~ 3	10
#~ 4	17
#~ ...	...
#~ 41139	19
#~ 41140	20
#~ 41141	18
#~ 41142	18
#~ 41143	16
#~ 41144 rows × 1 columns
