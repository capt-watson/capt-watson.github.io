import pandas as pd

url = 'https://github.com//mattharrison/datasets/raw/master/data/alta-noaa-1980-2019.csv'

alta_df = pd.read_csv(url)

dates = pd.to_datetime(alta_df.DATE)

snow = alta_df.SNOW.rename(dates)


#~ 1980-01-01    2.0
#~ 1980-01-02    3.0
#~ 1980-01-03    1.0
#~ 1980-01-04    0.0
#~ 1980-01-05    0.0
#~              ... 
#~ 2019-09-03    0.0
#~ 2019-09-04    0.0
#~ 2019-09-05    0.0
#~ 2019-09-06    0.0
#~ 2019-09-07    0.0
#~ Name: SNOW, Length: 14160, dtype: float64

## The above data shows the amount of snow fell each day at the ski resort.

#! Finding if any missing data in the snow column.

# snow.isna().any()

#~ True

## Here True means that there is/are some data missing.

# snow[snow.isna()]

1#~ 985-07-30   NaN
1#~ 985-09-12   NaN
1#~ 985-09-19   NaN
1#~ 986-02-07   NaN
1#~ 986-06-26   NaN
1#~ 986-06-27   NaN
1#~ 986-06-28   NaN
1#~ 986-06-29   NaN
1#~ 986-06-30   NaN
1#~ 986-11-22   NaN
1#~ 986-11-30   NaN
1#~ 986-12-09   NaN

## The above code fetches indexes where data is missing.


# snow.loc['1985-09':'1985-09-20']

1#~ 985-09-01    0.0
1#~ 985-09-02    0.0
1#~ 985-09-03    0.0
1#~ 985-09-04    0.0
1#~ 985-09-05    0.0
1#~ 985-09-06    0.0
1#~ 985-09-07    0.0
1#~ 985-09-08    0.0
1#~ 985-09-09    0.0
1#~ 985-09-10    0.0
1#~ 985-09-11    0.0
1#~ 985-09-12    NaN
1#~ 985-09-13    0.0
1#~ 985-09-14    0.0
1#~ 985-09-15    0.0
1#~ 985-09-16    0.0
1#~ 985-09-17    0.0
1#~ 985-09-18    0.0
1#~ 985-09-19    NaN
1#~ 985-09-20    0.0
#~ ame: SNOW, dtype: float64

## The above data shows if data is missing or it is 0


#! Filling in missing data

# snow.loc['1985-09':'1985-09-20'].fillna(0)

#~ 1985-09-01    0.0
#~ 1985-09-02    0.0
#~ 1985-09-03    0.0
#~ 1985-09-04    0.0
#~ 1985-09-05    0.0
#~ 1985-09-06    0.0
#~ 1985-09-07    0.0
#~ 1985-09-08    0.0
#~ 1985-09-09    0.0
#~ 1985-09-10    0.0
#~ 1985-09-11    0.0
#~ 1985-09-12    0.0
#~ 1985-09-13    0.0
#~ 1985-09-14    0.0
#~ 1985-09-15    0.0
#~ 1985-09-16    0.0
#~ 1985-09-17    0.0
#~ 1985-09-18    0.0
#~ 1985-09-19    0.0
#~ 1985-09-20    0.0
#~ Name: SNOW, dtype: float64

## The above code will fill the missing data fields with 0.

# snow.loc['1987-12-30': '1988-01-10']

#~ 1987-12-30    6.0
#~ 1987-12-31    5.0
#~ 1988-01-01    NaN
#~ 1988-01-02    0.0
#~ 1988-01-03    0.0
#~ 1988-01-04    NaN
#~ 1988-01-05    2.0
#~ 1988-01-06    6.0
#~ 1988-01-07    4.0
#~ 1988-01-08    9.0
#~ 1988-01-09    5.0
#~ 1988-01-10    2.0
#~ Name: SNOW, dtype: float64

# snow.loc['1987-12-30': '1988-01-10'].ffill()

#~ 987-12-30    6.0
#~ 987-12-31    5.0
#~ 988-01-01    5.0
#~ 988-01-02    0.0
#~ 988-01-03    0.0
#~ 988-01-04    0.0
#~ 988-01-05    2.0
#~ 988-01-06    6.0
#~ 988-01-07    4.0
#~ 988-01-08    9.0
#~ 988-01-09    5.0
#~ 988-01-10    2.0
#~ ame: SNOW, dtype: float64

## ffill() method is called forward fill and bfill() methods is known as backward fill. Here the data value from the previous days is used for filling up the next day's missing data.

# snow.loc['1987-12-30': '1988-01-10'].bfill()

#~ 1987-12-30    6.0
#~ 1987-12-31    5.0
#~ 1988-01-01    0.0
#~ 1988-01-02    0.0
#~ 1988-01-03    0.0
#~ 1988-01-04    2.0
#~ 1988-01-05    2.0
#~ 1988-01-06    6.0
#~ 1988-01-07    4.0
#~ 1988-01-08    9.0
#~ 1988-01-09    5.0
#~ 1988-01-10    2.0
#~ Name: SNOW, dtype: float64

## Here the data value from the next day is used for filling up the previous day's missing data.

#! Interpolation

#@ Let’s interpolate the missing values using the Linear method. Note that Linear method ignore the index and treat the values as equally spaced.

# df = pd.DataFrame({"A":[12, 4, 5, None, 1], 
#                    "B":[None, 2, 54, 3, None], 
#                    "C":[20, 16, None, 3, 8], 
#                    "D":[14, 3, None, None, 6]})

# df.interpolate(limit_direction='both')


#^ axis = 0 means column by column, axis = 1 means row by row

# snow.loc['1987-12-30': '1988-01-10'].interpolate()


# winter = (snow.index.quarter == 1) | (snow.index.quarter == 4)

# snow.where(~(winter & snow.isna()), snow.interpolate()).where(~(~winter & snow.isna()),0)

#~ 1980-01-01    2.0
#~ 1980-01-02    3.0
#~ 1980-01-03    1.0
#~ 1980-01-04    0.0
#~ 1980-01-05    0.0
#~              ... 
#~ 2019-09-03    0.0
#~ 2019-09-04    0.0
#~ 2019-09-05    0.0
#~ 2019-09-06    0.0
#~ 2019-09-07    0.0
#~ Name: SNOW, Length: 14160, dtype: float64


## The first code line specifies the winter and summer period.

## First part of Second code line applies the interpolate method where it is winter i.e. it is quarter 1 or quarter 4 and yet the snowfall is missing. Second part of second code line applies the isna() method and leaves the snowfall as 0.

#% As .where() method keeps the first value where it is true. Now to reverse that condition, we use ~ to inverse that condition. Now .where() method will not keep the first value where the given condition is true but will replace it with the second value.

# snow.where(~(winter & snow.isna()), snow.interpolate()).where(~(~winter & snow.isna()),0).loc[['1985-09-19', '1988-01-01']]

#^ The above code interpolates the value for NaN during the winter months and in summer months, if the value is NaN, then it replaces it with 0.

#! Dropping missing values

# snow.loc['1987-12-30':'1988-01-10'].dropna()

#~ 1987-12-30    6.0
#~ 1987-12-31    5.0
#~ 1988-01-02    0.0
#~ 1988-01-03    0.0
#~ 1988-01-05    2.0
#~ 1988-01-06    6.0
#~ 1988-01-07    4.0
#~ 1988-01-08    9.0
#~ 1988-01-09    5.0
#~ 1988-01-10    2.0
#~ Name: SNOW, dtype: float64

## The above code drops all the missing values from the series.

#! Shifting Data

#^ forward Shift example

# snow.shift(1)

#~ 1980-01-01    NaN
#~ 1980-01-02    2.0
#~ 1980-01-03    3.0
#~ 1980-01-04    1.0
#~ 1980-01-05    0.0
#~              ... 
#~ 2019-09-03    0.0
#~ 2019-09-04    0.0
#~ 2019-09-05    0.0
#~ 2019-09-06    0.0
#~ 2019-09-07    0.0

## Here forward shift pushes the entire series values down by 1 row.


#^ backward shift example.

# snow.shift(-1)

#~ 1980-01-01    3.0
#~ 1980-01-02    1.0
#~ 1980-01-03    0.0
#~ 1980-01-04    0.0
#~ 1980-01-05    1.0
#~              ... 
#~ 2019-09-03    0.0
#~ 2019-09-04    0.0
#~ 2019-09-05    0.0
#~ 2019-09-06    0.0
#~ 2019-09-07    NaN
#~ Name: SNOW, Length: 14160, dtype: float64

## Here backward shift pushes the entire series values up by 1 row.

#! Rolling Average

# snow.add(snow.shift(1)).add(snow.shift(2)).add(snow.shift(3)).add(snow.shift(4)).div(5)

#~ 1980-01-01    NaN
#~ 1980-01-02    NaN
#~ 1980-01-03    NaN
#~ 1980-01-04    NaN
#~ 1980-01-05    1.2
#~              ... 
#~ 2019-09-03    0.0
#~ 2019-09-04    0.0
#~ 2019-09-05    0.0
#~ 2019-09-06    0.0
#~ 2019-09-07    0.0

# snow.rolling(5).mean()

#~ 1980-01-01    NaN
#~ 1980-01-02    NaN
#~ 1980-01-03    NaN
#~ 1980-01-04    NaN
#~ 1980-01-05    1.2
#~              ... 
#~ 2019-09-03    0.0
#~ 2019-09-04    0.0
#~ 2019-09-05    0.0
#~ 2019-09-06    0.0
#~ 2019-09-07    0.0
#~ Name: SNOW, Length: 14160, dtype: float64

#% The above code uses rolling() method to shift all the lines below and apply mean() method to get the average of the values. The value which was at the index 0 has been shifted down by 5 places and replaced by the average of all the 5 values.

#! Resampling

# snow.resample('ME').max()

#~ 1980-01-31    20.0
#~ 1980-02-29    25.0
#~ 1980-03-31    16.0
#~ 1980-04-30    10.0
#~ 1980-05-31     9.0
#~               ... 
#~ 2019-05-31     5.1
#~ 2019-06-30     0.0
#~ 2019-07-31     0.0
#~ 2019-08-31     0.0
#~ 2019-09-30     0.0
#~ Freq: ME, Name: SNOW, Length: 477, dtype: float64

#^ Note: 'ME' means month end. Resample aggregates values at different. At high levels, we group date entries by some interval(Yearly, Monthly, weekly, etc) and then aggregate values at that interval.

# snow.resample('2ME').max()

#~ 1980-01-31    20.0
#~ 1980-03-31    25.0
#~ 1980-05-31    10.0
#~ 1980-07-31     1.0
#~ 1980-09-30     0.0
#~               ... 
#~ 2019-01-31    19.0
#~ 2019-03-31    20.7
#~ 2019-05-31    18.0
#~ 2019-07-31     0.0
#~ 2019-09-30     0.0
#~ Freq: 2ME, Name: SNOW, Length: 239, dtype: float64

## 2ME means two month.

# snow.resample('YE-MAY').max()

#~ 1980-05-31    25.0
#~ 1981-05-31    26.0
#~ 1982-05-31    34.0
#~ 1983-05-31    38.0
#~ 1984-05-31    25.0
#~ 1985-05-31    22.0
#~ 1986-05-31    34.0
#~ 1987-05-31    16.0
#~ 1988-05-31    23.0
#~ 1989-05-31    30.0
#~ 1990-05-31    32.0
#~ 1991-05-31    28.0
#~ 1992-05-31    22.0
#~ 1993-05-31    30

## YE-MAY means year end may

#! Gathering Aggregate Values (But Keeping Index)

# snow.div(snow.resample('ME').transform('sum')).mul(100).fillna(0)

#~ 1980-01-01    1.388889
#~ 1980-01-02    2.083333
#~ 1980-01-03    0.694444
#~ 1980-01-04    0.000000
#~ 1980-01-05    0.000000
#~                 ...   
#~ 2019-09-03    0.000000
#~ 2019-09-04    0.000000
#~ 2019-09-05    0.000000
#~ 2019-09-06    0.000000
#~ 2019-09-07    0.000000
#~ Name: SNOW, Length: 14160, dtype: float64

#^ The offset alias 'ME' aggregates at the monthly level. The transform method puts the result into the original index.

# season2017 = snow.loc['2016-10':'2017-05']

# season2017.resample('ME').sum().div(season2017.sum()).mul(100)

#~ 2016-10-31     2.153969
#~ 2016-11-30     9.772637
#~ 2016-12-31    15.715995
#~ 2017-01-31    25.468688
#~ 2017-02-28    21.041085
#~ 2017-03-31     9.274033
#~ 2017-04-30    14.738732
#~ 2017-05-31     1.834862
#~ Freq: ME, Name: SNOW, dtype: float64

#! Groupby Operations

def season(idx):
    year = idx.year
    month = idx.month
    return year.where((month<10), year+1)

snow.groupby(season(snow.index)).sum()



# snow.resample('YE-SEP').sum()

#~ 1980-09-30    457.5
#~ 1981-09-30    503.0
#~ 1982-09-30    842.5
#~ 1983-09-30    807.5
#~ 1984-09-30    816.0
#~ 1985-09-30    536.0
#~ 1986-09-30    740.8
#~ 1987-09-30    243.1
#~ 1988-09-30    314.5
#~ 1989-09-30    429.5

#! Cumulative Operations

# snow.loc['2016-10':'2017-09'].cumsum()

#~ 2016-10-01      0.0
#~ 2016-10-02      0.0
#~ 2016-10-03      4.9
#~ 2016-10-04      4.9
#~ 2016-10-05      5.5
#~               ...  
#~ 2017-09-26    524.0
#~ 2017-09-27    524.0
#~ 2017-09-28    524.0
#~ 2017-09-29    524.0
#~ 2017-09-30    524.0
#~ Name: SNOW, Length: 364, dtype: float64


#% To do this calculation for every year, use .resample with .transform and .cumsum:

# snow.resample('YE-SEP').transform('cumsum')

#~ 1980-01-01      2.0
#~ 1980-01-02      5.0
#~ 1980-01-03      6.0
#~ 1980-01-04      6.0
#~ 1980-01-05      6.0
#~               ...  
#~ 2019-09-03    504.5
#~ 2019-09-04    504.5
#~ 2019-09-05    504.5
#~ 2019-09-06    504.5
#~ 2019-09-07    504.5
#~ Name: SNOW, Length: 14160, dtype: float64

