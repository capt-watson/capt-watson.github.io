import pandas as pd
from tweak_jb import tweak_jb
pd.set_option('future.no_silent_downcasting', True)

url = 'https://github.com/mattharrison/datasets/raw/master/data/2020-jetbrains-python-survey.csv'

jb = pd.read_csv(url, dtype='unicode')

jb2 = tweak_jb(jb)

## Following code will create a new column and store size values into it.
jb2.groupby('country_live', observed=True).age.transform('size')


## Following codes will create a new column called 'country_responses' at the end of the dataframe and store aggregations values into it. Total numbers of given age group people from the given country.
jb2.assign(country_responses = jb2.groupby('country_live', observed=True).age.transform('size'))

#^ Filtering parts of Group

## Following codes will return total number of respondents from the given country.
jb2.country_live.value_counts()

## Following codes will return a median value for the value counts column.
jb2.country_live.value_counts().median()

## Here the median is 60.5

jb2.groupby('country_live', observed=True).filter(lambda g: g.country_live.size >= 60.5)

