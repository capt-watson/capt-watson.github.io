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

make = df.make

#! Prepping the Data and Renaming the Index

#% Use of .rename method to change the index labels. One can pass in a dictionary to map the previous index label to the new label:

city2 = city_mpg.rename(make.to_dict())  ##to_dict() method is used to convert a DataFrame into a dictionary of series

city2


#~ Alfa Romeo    19
#~ Ferrari        9
#~ Dodge         23
#~ Dodge         10
#~ Subaru        17
#~               ..
#~ Subaru        19
#~ Subaru        20
#~ Subaru        18
#~ Subaru        18
#~ Subaru        16
#~ Name: city08, Length: 41144, dtype: int64

#% To view the index you can access the .index attribute:

# city2.index

#~ Index(['Alfa Romeo', 'Ferrari', 'Dodge', 'Dodge', 'Subaru', 'Subaru', 'Subaru', 'Toyota', 'Toyota', 'Toyota',       ...       'Saab', 'Saturn', 'Saturn', 'Saturn', 'Saturn', 'Subaru', 'Subaru', 'Subaru', 'Subaru', 'Subaru'], dtype='object', length=41144)

#* examples of renaming index of a series

# s = pd.Series([145,142,38,13], index=['Veronica', 'Suzy', 'Bob', 'Veronica'])


# s.rename(index={0:'Emily'})


#~ Emily        Dave
#~ 1            Suzy
#~ 2             Bob
#~ 3        Veronica
#~ dtype: object

# def to_str(val):
#     return f'idx-{val}'

# s.rename(to_str)


#~ idx-0        Dave
#~ idx-1        Suzy
#~ idx-2         Bob
#~ idx-3    Veronica
#~ dtype: object

## following will replace the entire index of 's' with new index values from 's2'

# s2 = pd.Series(['a','b','c','d'])
# s.rename(index=s2)


## If only one value provided without specifying index number, then none of the index values will be modified. Only .name attribute will be updated.

# s.rename(index='Emily')

#~ 0        Dave
#~ 1        Suzy
#~ 2         Bob
#~ 3    Veronica
#~ Name: Emily, dtype: object



# city2= city_mpg.rename(make)

## If you pass a scalar value (a single string) into .rename, the index will stay the same, but the .name attribute of the series will update as shown below:

city2.rename('First')

#~ Alfa Romeo    19
#~ Ferrari        9
#~ Dodge         23
#~ Dodge         10
#~ Subaru        17
#~               ..
#~ Subaru        19
#~ Subaru        20
#~ Subaru        18
#~ Subaru        18
#~ Subaru        16
#~ Name: First, Length: 41144, dtype: int64

#! Resetting the Index

## If you want to set the index to monotonic increasing, and therefore unique integers starting at zero, you can use the .reset_index method.

## By default, this method will return a dataframe, moving the current index into a new column:

# city2.reset_index()

#~ 	index	city08
#~ 0	Alfa Romeo	19
#~ 1	Ferrari	9
#~ 2	Dodge	23
#~ 3	Dodge	10
#~ 4	Subaru	17
#~ ...	...	...
#~ 41139	Subaru	19
#~ 41140	Subaru	20
#~ 41141	Subaru	18
#~ 41142	Subaru	18
#~ 41143	Subaru	16
#~ 41144 rows × 2 columns

#% To drop the current index and return a Series, use the drop=True parameter:

# city2.reset_index(drop=True)

#* examples of resetting index of a series

# s.reset_index()

#~      index	 0
#~ 0	Dave	145
#~ 1	Suzy	142
#~ 2	Bob	     38
#~ 3	Veronica 13


## Renaming of the axis label as 'First'

# s.rename_axis('First').reset_index()

#~      First	 0
#~ 0	Dave	145
#~ 1	Suzy	142
#~ 2	Bob	38
#~ 3	Veronica	13


## Will drop the current axis

# s.reset_index(drop = True)

#~ 0    145
#~ 1    142
#~ 2     38
#~ 3     13
#~ dtype: int64

#% One can sort the values and the index with .sort_values and .sort_index respectively.


# city2.sort_values()

#~ Lamborghini      6
#~ Lamborghini      6
#~ Lamborghini      6
#~ Lamborghini      6
#~ Lamborghini      6
#~               ... 
#~ Tesla          138
#~ Tesla          140
#~ Hyundai        150
#~ Hyundai        150
#~ Hyundai        150
#~ Name: city08, Length: 41144, dtype: int64


# city2.sort_index()

#~ AM General    13
#~ AM General    18
#~ AM General    13
#~ AM General    16
#~ AM General    13
#~               ..
#~ smart         33
#~ smart         31
#~ smart         31
#~ smart         33
#~ smart         34
#~ Name: city08, Length: 41144, dtype: int64

#! The .loc Attribute

#% .loc attribute deals with index labels. It allows you to pull out the pieces of the series.
#% .loc can also be called 'locate method'

## Will return a series as there are more than one 'Subaru' labels in the series.

# city2.loc['Subaru'] 


# city2.loc['Fisker']

#~ 20


## Following will return the index with its value.
# city2.loc[['Fisker']]

#~ Fisker    20
#~ Name: city08, dtype: int64


## Following will return the indexes with multiple values
# city2.loc[['Fisker', 'Lamborghini']]

#~ Fisker         20
#~ Lamborghini     8
#~ Lamborghini     8
#~ Lamborghini     8

#* examples of .loc on a series

# s.loc[['Veronica']]

#~ Veronica    13
#~ dtype: int64


# s.loc[['Veronica','Bob']]

#~ Veronica    145
#~ Veronica     13
#~ Bob          38


#% Need to use .sort before .loc to slice with string values else will result in KeyError:

# city2.sort_index().loc['Ferrari':'Lamborghini']

#~ Ferrari        10
#~ Ferrari        13
#~ Ferrari        13
#~ Ferrari         9
#~ Ferrari        10
#~                ..
#~ Lamborghini    12
#~ Lamborghini     9
#~ Lamborghini     8
#~ Lamborghini    13
#~ Lamborghini     8
#~ Name: city08, Length: 11210, dtype: int64

#* Exercise

s = pd.Series([145,140,38,13],index=['Veronica', 'Suzy', 'Bob', 'Veronica'])

s[~s.index.duplicated(keep='first')].loc['Veronica':'Bob']

#~ Veronica    145
#~ Suzy        140
#~ Bob          38
#~ dtype: int64

city2.sort_index().loc['F':'J']  ## Slices upto J but not including J.

#~ Federal Coach    15
#~ Federal Coach    13
#~ Federal Coach    13
#~ Federal Coach    14
#~ Federal Coach    13
#~                  ..
#~ Isuzu            15
#~ Isuzu            15
#~ Isuzu            15
#~ Isuzu            27
#~ Isuzu            18
#~ Name: city08, Length: 9040, dtype: int64

city2.loc[pd.Index(['Dodge'])]

#~ Dodge    23
#~ Dodge    10
#~ Dodge    12
#~ Dodge    11
#~ Dodge    11
#~          ..
#~ Dodge    18
#~ Dodge    17
#~ Dodge    14
#~ Dodge    14
#~ Dodge    11
#~ Name: city08, Length: 2583, dtype: int64

mask = city2 > 50
mask                ## Will return values where the city mileage is above 50 or False since the mask doesn't return anything for value found to be True.

#~ Alfa Romeo    False
#~ Ferrari       False
#~ Dodge         False
#~ Dodge         False
#~ Subaru        False
#~               ...  
#~ Subaru        False
#~ Subaru        False
#~ Subaru        False
#~ Subaru        False
#~ Subaru        False
#~ Name: city08, Length: 41144, dtype: bool

city2.loc[mask]

#~ Nissan              81
#~ Toyota              81
#~ Toyota              81
#~ Ford                74
#~ Nissan              84
#~ Tesla              140
#~ Tesla              115
#~ Tesla              104
#~ Tesla               98
#~ Toyota              55
#~ Name: city08, dtype: int64

#* Exercise

## Given below are the prices of household commodities as was observed a year ago. Prices have increased 10% since then. Find out only those items where the prices have gone beyond $3.


cost = pd.Series([1.00, 2.25, 3.99, 0.99, 2.79],index = ['Gum', 'Cookie', 'Melon', 'Roll','Carrots'])
inflation = 1.10
cost.mul(inflation).loc[lambda x : x > 3]

#~ Melon      4.389
#~ Carrots    3.069
#~ dtype: float64

#! The .iloc Attribute

city2.iloc[0]       ## First value

city2.iloc[-1]      ## Last Value

#% When indexed with a list of positions, iloc will return a series object.

city2.iloc[[0, 1, -1]]  ## Will return first, second and last value


city2.iloc[0:5]         ## Will return first to 4th position values.

#~ Alfa Romeo    19
#~ Ferrari        9
#~ Dodge         23
#~ Dodge         10
#~ Subaru        17
#~ Name: city08, dtype: int64

city2.iloc[-8:]  ## Will return the last eight positions.

mask = city2 > 50
city2.iloc[mask.to_numpy()]   ## Convert the mask to numpy for mask to work with .iloc

city2.iloc[list(mask)]        ## Or use mask within list[] for it work with .iloc



#! Heads and Tails:

#% Heads & Tails methods are useful in pulling out values at the start or end of the series.
#% Useful for checking chunks of data for missing values etc.

city2.head(3)   ## Will extract first 3 lines of the series data.

#~ Alfa Romeo    19
#~ Ferrari        9
#~ Dodge         23
#~ Name: city08, dtype: int64

city2.tail(3)   ## Will extract last 3 lines of the series data.
#~ Subaru    18
#~ Subaru    18
#~ Subaru    16
#~ Name: city08, dtype: int64


#! Sampling

#% Sampling extracts specified number of lines randomly from the series.

city2.sample(6, random_state=42)  ## random_state parameter is used for controlling the randomness of the sample. No.42 is a number commonly used in science fictions.

#~ Volvo         16
#~ Mitsubishi    19
#~ Buick         27
#~ Jeep          15
#~ Land Rover    13
#~ Saab          17
#~ Name: city08, dtype: int64

#! Filtering index values

#% Filter method will filter index labels by:

#% exact match
#% substring
#% regular expression

#% Filter is controlled with 'items', 'like' and 'regex' parameters.

# city2.filter(items=['Ford', 'Subaru'])  ## Will produce valueError as the index has duplicate labels.

city2.filter(like='rd')   ## Use of 'like' parameter to filer the index

#~ Ford    18
#~ Ford    16
#~ Ford    17
#~ Ford    17
#~ Ford    15
#~         ..
#~ Ford    26
#~Ford    19
#~ Ford    21
#~ Ford    18
#~ Ford    19
#~ Name: city08, Length: 3371, dtype: int64

city2.filter(regex='(Ford)|(Subaru)')  ## Use of 'regex' parameter to filter index

#~ Subaru    17
#~ Subaru    21
#~ Subaru    22
#~ Ford      18
#~ Ford      16
#~           ..
#~ Subaru    19
#~ Subaru    20
#~ Subaru    18
#~ Subaru    18
#~ Subaru    16
#~ Name: city08, Length: 4256, dtype: int64


#! Reindexing

#% Reindex method allows one to extract values by index label.
#% Reindex method does not work with duplicate labels in the index.

# city2.reindex(['Lamborghini', 'Jaguar'])

#~ ValueError: cannot reindex on an axis with duplicate labels

city_mpg.reindex([0,0,20,200000])   ## Although reindex method does not work with duplicate labels, but if one repeats the same index label multiple times, it will repeat that index.

#~ 0         19.0
#~ 0         19.0
#~ 20        14.0
#~ 200000     NaN
#~ Name: city08, dtype: float64

s1 = pd.Series([10,20,30],index=['a','b','c'])
s2 = pd.Series([15,25,35],index=['b','c','d'])

s2.reindex(s1.index)    ## passing entire s1 index as parameter for s2 reindex

#~ a     NaN
#~ b    15.0
#~ c    25.0
#~ dtype: float64

