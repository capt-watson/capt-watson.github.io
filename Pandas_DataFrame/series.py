import pandas as pd

# series = {
#         'index':[0 , 1, 2, 3],
#         'data':[145 , 142, 38, 13],
#         'name':'songs '
#         }


# def get(series, idx):
#     value_idx = series['index'].index(idx) ## Search val in series dic at given index
#     return series['data'][value_idx]

# x = get(series,1)   ## Get the value in data colum at index 1

# print(x)

# % Index Abstraction

#! Here index need not be integers but it can also be strings

# songs = {
#     "index": ["Betty", "John", "George", "Veronica"],
#     "data": [145, 142, 38, 13],
#     "name": "Counts",
# }

# def get(series, idx):
#     value_idx = series["index"].index(idx)  ## Search val in series dic at given index
#     return series["data"][value_idx]


# Y = get(songs, "George")

# print(Y)



# '''
# The index is a core feature of pandas’data structures given the library’s past in analysis of
# financial data or time-series data. Many of the operations performed on a Series operate directly
# on the index or by index lookup.
# '''

#! Pandas Series

# import pandas as pd

# songs2 = pd.Series([145,142,38,13], name='counts')

# print(songs2)

## Generic name for an index is an 'axis'.

## The values of the index i.e. o,1,2,3 are called 'axis labels'.

## The data i.e. are called 'values' of the series.

## Two dimensional structure of pandas i.e. 'DataFrame' has two axis, one for rows and
## another for columns.

## dtype: int64 means and data type and int64 means 64 bit integer.

## To get the best speed, the value should be of same type.

#% 'name' is given (optional) to the index column. Here its is given as 'count'.

#! 'count' method counts the number of values in the given series.

# x = songs2.index
# print(x)


songs3 = pd.Series([145,142,38,13], name='counts', index = ["Betty", "John", "George", "Veronica"])

# print(songs3)

# print(songs3.index)

## The actual data (or values) for a series does not have to be numeric or homogeneous.

## We can insert Python objects into a series as shown below:

# class Foo:
#     pass

# ringo = pd.Series(['Richard ', 'Starkey ', 13, Foo()], name='ringo ')

# print(ringo)

# #! The NaN value

# import numpy as np

# nan_series = pd.Series([2, np.nan], index=['0no', 'Clapton'])

# print(nan_series)

# a = nan_series.count()

# print(a)

#% note here that the type of this series is float64, not int64!

##The type is a float because float64 supports NaN, which int64 does not.
## When pandas sees numeric data (2) as well as the np.nan, it coerced the 2 to a float value


## In this case, it indicates that the count of items in the series is one, one for the
## value of 2 at index location Ono, ignoring the NaN value at index location Clapton

## You can inspect the number of entries (including missing values) with the .size property

# b = nan_series.size

# print(b)

#! Note: If you load data from a CSV file, an empty value for an otherwise numeric column will become
#! NaN. Later, methods such as .fillna and .dropna will explain how to deal with NaN.


#% The pandas Series object mentioned above behaves similarly to a NumPy array given below. Both types respond to index operations:


#! Mean - The average value, Median - The mid point value, Mode - The most common value

# numpy_ser = np.array([145,142,38,13])

# print(songs3.iloc[1])

# print(numpy_ser[1])

# print(songs3.mean ())

# print(numpy_ser.mean ())

# print(songs3.median())

# mask = songs3 > songs3.median()     ## boolean array

# print(mask)

## Here the answer is :

## Betty        True
## John         True
## George      False
## Veronica    False

## Explanation: Since the songs3.median() is 90.0, Betty & John (145,142) have higher values than George & Veronica (38,13) and hence the answer for the first 2 values are TRUE whereas for rest it is FALSE.

#% NumPy also has filtering by boolean arrays, but lacks the .median method on an array. Instead, NumPy provides a median function in the NumPy namespace as given below. Here the output will be in the form of array.

# mask1 = numpy_ser[numpy_ser > np.median(numpy_ser )]
# print(mask1)
# #~ [145 142]

#% Categorical Data

#* When you load data, you can indicate that the data is categorical. Beneficial only if data limited to few values.

s = pd.Series(['m','l', 'xs','s', 'xl'], dtype='category')

print(s)

#~ 0     m
#~ 1     l
#~ 2    xs
#~ 3     s
#~ 4    xl
#~ dtype: category
#~ Categories (5, object): ['l', 'm', 's', 'xl', 'xs']

#! By default, categories don’t have an ordering.

print(s.cat.ordered)
#~ False

#! To convert a non-categorical series to an ordered category, create a type with the CategoricalDtype constructor and the appropriate parameters. Pass this type into the .astype method:

s2 = pd.Series (['m', 'l', 'xs ', 's', 'xl '])
size_type = pd.api.types.CategoricalDtype(categories =['s','m','l'], ordered=True)

s3 = s2.astype(size_type)

print(s3)

#~ 0      m
#~ 1      l
#~ 2    NaN
#~ 3      s
#~ 4    NaN
#~ dtype: category
#~ Categories (3, object): ['s' < 'm' < 'l']

print(s3 > 's')

#~ 0     True
#~ 1     True
#~ 2    False
#~ 3    False
#~ 4    False
#~ dtype: bool

#! One can also add ordering information to categorical data. One just need to make sure that we specify all of the members of the category or pandas will throw a ValueError:

a = s.cat.reorder_categories(['xs','s','m','l','xl'], ordered=True)

print(a)

#~ 0     m
#~ 1     l
#~ 2    xs
#~ 3     s
#~ 4    xl
#~ dtype: category
#~ Categories (5, object): ['xs' < 's' < 'm' < 'l' < 'xl']

#* Summary

#!      Method                                    Description
#% Method Description                           #% Create a series from data (sequence, dictionary, .
#% pd.Series(data=None, index=None,             #% or scalar)
#% dtype=None, name=None, copy=False)
#% s.index                                      #% Access index of series.
#% s.astype(dtype, errors='raise')              #% Cast a series to dtype. To ignore errors(and return          original object) use errors='ignore'.
#% s[boolean_array]                             #% Return values from s where boolean_array is True.
#% s.cat.ordered                                #% Determine if a categorical series is ordered.
#% s.cat.reorder_categories( new_categories, ordered=False) 
#% Add categories (potentially ordered) to the series. #% Add categories (potentially ordered) to the series new_categories must include all categories.

#* Page 23