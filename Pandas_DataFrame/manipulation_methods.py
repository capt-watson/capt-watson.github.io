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

#* Most of the methods we discuss here manipulate the series values but preserve the index.

#! .apply and .where

#^ Code smells are usually not bugs; they are not technically incorrect and do not prevent the program from functioning. Instead, they indicate weaknesses in design that may slow down development or increase the risk of bugs or failures in the future.

#^ .apply method typically operates on each individual value in the series, the function is called once for every value. If you have one million values in a series, it will be called one million times and hence slows down python code execution.

make = df.make

make

make.value_counts()

top_5 = make.value_counts().index[:5]

def generalize_top5(val):
    if val in top_5:
        return val
    return 'other'

make.apply(generalize_top5)

#~ 0        other
#~ 1        other
#~ 2        Dodge
#~ 3        Dodge
#~ 4        other
#~          ...  
#~ 41139    other
#~ 41140    other
#~ 41141    other
#~ 41142    other
#~ 41143    other
#~ Name: make, Length: 41144, dtype: object

#^ In the above example, generalize_top5 is called once for every value which slows down dev.

#% A faster, more idiomatic manner of doing this is using .where method.

## %%timeit
# make.apply(generalize_top5)
#~ 23.3 ms ± 3.31 ms per loop (mean ± std. dev. of 7 runs , 10 loops each)

# %%timeit
# make.where(make.isin(top_5), other = 'Other')
#~ 4.49 ms ± 1.94 ms per loop (mean ± std. dev. of 7 runs , 100 loops each)

#& In the above .where method, wherever the condition is False it keeps the original values; if it is True it replaces the value with the other parameter.

# make.mask(~make.isin(top_5), other='other')

#* In the above code, ~ performs an inversion of the boolean array, switching all true values to false and vice versa.

#! If Else with Pandas

vc = make.value_counts()
top_5 = vc.index[:5]
top_10 = vc.index[:10]

# def generalize(val):
#     if val in top_5:
#         return val
#     elif val in top_10:
#         return 'Top 10'
#     else:
#         return 'Other'

# make.apply(generalize)

#^ To replicate this in pandas, one needs to chain calls to .where:

(make.where(make.isin(top_5), 'Top 10').where(make.isin(top_10), 'Other'))

#~ 0        Other
#~ 1        Other
#~ 2        Dodge
#~ 3        Dodge
#~ 4        Other
#~          ...  
#~ 41139    Other
#~ 41140    Other
#~ 41141    Other
#~ 41142    Other
#~ 41143    Other
#~ Name: make, Length: 41144, dtype: object

#! Missing Data

#* machine learning algorithms do not work if there is missing data.

cyl = df.cylinders

# (cyl.isna().sum())  ## Returns the sum of missing values in the cylinder column.

#~ 206

#% To find out the indexes where the values are missing in cyl column:

missing = cyl.isna()

make.loc[missing]  ## This returns list of indexes where the values are missing


#! Filling In Missing Data

cyl[cyl.isna()]

cyl.fillna(0).loc[7136:7141]    ## fillna(0) replaces all NaN values with '0'

#! Interpolating Data

## Interpolation means replacing a new data into another data.

#% Another option for replacing missing data is the .interpolate method. This comes in handy if the data is ordered (as time series data often is) and there are holes in the data.

# temp = pd.Series([32,40,None, 42, 39, 32])

# temp

#~ 0    32.0
#~ 1    40.0
#~ 2     NaN
#~ 3    42.0
#~ 4    39.0
#~ 5    32.0
#~ dtype: float64



# temp.interpolate()

#~ 0    32.0
#~ 1    40.0
#~ 2    41.0
#~ 3    42.0
#~ 4    39.0
#~ 5    32.0
#~ dtype: float64


#! Clipping Data

#% For outliers in one's data, one might want to use the .clip method.

city_mpg.loc[:446].clip(lower=city_mpg.quantile(0.05),upper=city_mpg.quantile(.95))


#! Sorting Values

#% The .sort_values method will sort the values in ascending order and also rearrange the index accordingly:

city_mpg.sort_values()

#~ 7901       6
#~ 34557      6
#~ 37161      6
#~ 21060      6
#~ 35887      6
#~        ... 
#~ 34563    138
#~ 34564    140
#~ 32599    150
#~ 31256    150
#~ 33423    150
#~ Name: city08, Length: 41144, dtype: int64



#% Because of index alignment, you can still do math operations on a sorted series:

(city_mpg.sort_values() + highway_mpg)/2
#~ 0        22.0
#~ 1        11.5
#~ 2        28.0
#~ 3        11.0
#~ 4        20.0
#~          ... 
#~ 41139    22.5
#~ 41140    24.0
#~ 41141    21.0
#~ 41142    21.0
#~ 41143    18.5
#~ Length: 41144, dtype: float64

#! Sorting the Index

#% To sort the index of a series, one can use the .sort_index method. First we unsort the index by sorting the values and then sort the index.

city_mpg.sort_values().sort_index()

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
#~ Name: city08, Length: 41144, dtype: int64


#! Dropping Duplicates

#% The .drop_duplicates method will remove values that appear more than once. You can determine whether to keep the first or last duplicate value found using the keep parameter. If you set it to 'last' it will use the last value. The default value is 'first'. If set it to False it will remove any duplicated values (including the initial value). This call keeps the original index. Notice that there are only 105 results (down from 41144) now that duplicates are removed:

city_mpg.drop_duplicates()

#! Ranking Data

#% The .rank method will return a series that keeps the original index but uses the ranks of values from the original series. One can control how ranking occurs with the method parameter. By default, if two values are same, their rank will be average of the positions they take. One can specify 'min' to put equal values in the same rank, and 'dense' to not skip any positions:

city_mpg.rank()
#~ 0        27060.5
#~ 1          235.5
#~ 2        35830.0
#~ 3          607.5
#~ 4        19484.0
#~           ...   
#~ 41139    27060.5
#~ 41140    29719.5
#~ 41141    23528.0
#~ 41142    23528.0
#~ 41143    15479.0
#~ Name: city08, Length: 41144, dtype: float64


city_mpg.rank(method='min')

#~ 0        25555.0
#~ 1          136.0
#~ 2        35119.0
#~ 3          336.0
#~ 4        17467.0
#~           ...   
#~ 41139    25555.0
#~ 41140    28567.0
#~ 41141    21502.0
#~ 41142    21502.0
#~ 41143    13492.0
#~ Name: city08, Length: 41144, dtype: float64


city_mpg.rank(method='dense')

#~ 0        14.0
#~ 1         4.0
#~ 2        18.0
#~ 3         5.0
#~ 4        12.0
#~          ... 
#~ 41139    14.0
#~ 41140    15.0
#~ 41141    13.0
#~ 41142    13.0
#~ 41143    11.0
#~ Name: city08, Length: 41144, dtype: float64


#! Replacing Data

#% The .replace method allows one to map values to new values. There are many ways to specify how to replace the values. One can specify a whole string to replace a string or use a dictionary to map old values to new values.

make.replace('Subaru ', 'スバル')

#* make.replace('old word', ; 'new word')

df = pd.Series([40, 20, 30, 15, 10], index= [0, 1, 2, 3, 4])


# df.replace(to_replace=[40,10], value=[42,9.8])  ## First method

# #~ 0    42.0
# #~ 1    20.0
# #~ 2    30.0
# #~ 3    15.0
# #~ 4     9.8
# #~ dtype: float64



# df.replace(to_replace={40:42, 10:9.8})          ## second method

# #~ 0    42.0
# #~ 1    20.0
# #~ 2    30.0
# #~ 3    15.0
# #~ 4     9.8
# #~ dtype: float64

df = pd.Series(['Dave', 'Suzy', 'Adam', 'Sandy'], index= [0,1,2,3])


df.replace(to_replace='Suzy', value='Suzanne')   ## First method

#~ 0       Dave
#~ 1    Suzanne
#~ 2       Adam
#~ 3      Sandy
#~ dtype: object


df.replace(to_replace={'Suzy':'Suzanne'})       ## Second Method

#~ 0       Dave
#~ 1    Suzanne
#~ 2        Adam
#~ 3      Sandy
#~ dtype: object


df.replace(to_replace='z.*', value='zanne', regex=True)  ## Third method

#~ 0       Dave
#~ 1    Suzanne
#~ 2       Adam
#~ 3      Sandy
#~ dtype: object


#! Binning Data

#% Using the cut function, one can create bins of equal width:

# pd.cut(city_mpg, 10)

#~ 0        (5.856, 20.4]
#~ 1        (5.856, 20.4]
#~ 2         (20.4, 34.8]
#~ 3        (5.856, 20.4]
#~ 4        (5.856, 20.4]
#~              ...      
#~ 41139    (5.856, 20.4]
#~ 41140    (5.856, 20.4]
#~ 41141    (5.856, 20.4]
#~ 41142    (5.856, 20.4]
#~ 41143    (5.856, 20.4]
#~ Name: city08, Length: 41144, dtype: category
#~ Categories (10, interval[float64, right]): [(5.856, 20.4] < (20.4, 34.8] < (34.8, 49.2] < #~ (49.2, 63.6] ... (92.4, 106.8] < (106.8, 121.2] < (121.2, 135.6] < (135.6, 150.0]]

#% If you have specific sizes for bin edges, you can specify those. In the following example five bins are created (so you need to provide six edges):

# pd.cut(city_mpg, [0,10,20,40,70,150])

#~ 0        (10, 20]
#~ 1         (0, 10]
#~ 2        (20, 40]
#~ 3         (0, 10]
#~ 4        (10, 20]
#~            ...   
#~ 41139    (10, 20]
#~ 41140    (10, 20]
#~ 41141    (10, 20]
#~ 41142    (10, 20]
#~ 41143    (10, 20]
#~ Name: city08, Length: 41144, dtype: category
#~ Categories (5, interval[int64, right]): [(0, 10] < (10, 20] < (20, 40] < (40, 70] < (70, 150]]

#% Note the bins have a half-open interval. They do not have the start value but do include the end value. If the city_mpg series had values with 0 or values above 150, they would be missing after binning the series.


#% One can bin data with quantiles instead. If you wanted 10 bins that had approximately the same number of entries in each bin (rather that each bin width being the same), use the qcut function:

# pd.qcut(city_mpg, 10)

#~ 0         (18.0, 20.0]
#~ 1        (5.999, 13.0]
#~ 2         (21.0, 24.0]
#~ 3        (5.999, 13.0]
#~ 4         (16.0, 17.0]
#~              ...      
#~ 41139     (18.0, 20.0]
#~ 41140     (18.0, 20.0]
#~ 41141     (17.0, 18.0]
#~ 41142     (17.0, 18.0]
#~ 41143     (15.0, 16.0]
#~ Name: city08, Length: 41144, dtype: category
#~ Categories (10, interval[float64, right]): [(5.999, 13.0] < (13.0, 14.0] < (14.0, 15.0] < #~ (15.0, 16.0] ... (18.0, 20.0] < (20.0, 21.0] < (21.0, 24.0] < (24.0, 150.0]]

#% Both of these functions allow you to set the labels to use instead of the categorical intervals they generate:

# pd.qcut(city_mpg, 10, labels=list(range(1,11)))

#~ 0        7
#~ 1        1
#~ 2        9
#~ 3        1
#~ 4        5
#~         ..
#~ 41139    7
#~ 41140    7
#~ 41141    6
#~ 41142    6
#~ 41143    4
#~ Name: city08, Length: 41144, dtype: category
#~ Categories (10, int64): [1 < 2 < 3 < 4 ... 7 < 8 < 9 < 10]