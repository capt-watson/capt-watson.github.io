import pandas as pd
from shiv_parvati import shiv_parvati

url= 'https://github.com/mattharrison/datasets/raw/master/data/siena2018-pres.csv'

df = pd.read_csv(url, index_col=0)

pres =shiv_parvati(df)


#% Sort by a single column name
# pres.sort_values(by='Party')

#% sort by multiple columns names as well as specifying whether each column should be sorted in ascending or descending order.

## In the code below, ascending=[True, False] specifies that the first column 'Party' should be sorted in ascending order and the second column 'Average rank' should be sorted in descending order
# pres.sort_values(by=['Party', 'Average_rank'], ascending=[True, False])


## Split the Presidents names in the President column
# pres.President.str.split()

# pres.President.str.split().apply(lambda val: val[-1])


## key function should be vectorized i.e it should expect a series and returns a series with the same shape as the input.

## Sort the presidents columns using the presidents last names using key function.
## First lambda will split the strings and second lambda will extract the last name from the president column.
pres.sort_values(by='President',key= lambda a: a.str.split().apply(lambda val: val[-1]))


#% Sorting the column order

## Will sort the columns alphabetically.
pres.sort_index(axis='columns')

## set_index() will change the index values to those from the column president.
pres.set_index('President').sort_index()


## will change the index values to those from the column party, sort its values and then filter only values between 'Democratic' and 'Republican'.

pres.set_index('Party').sort_index().loc['Democratic':'Republican']

