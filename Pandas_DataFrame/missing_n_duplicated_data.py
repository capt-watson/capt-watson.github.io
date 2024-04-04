import pandas as pd
from shiv_parvati import shiv_parvati

url= 'https://github.com/mattharrison/datasets/raw/master/data/siena2018-pres.csv'

df = pd.read_csv(url, index_col=0)

pres =shiv_parvati(df)

## isna() method will indicate whether values are missing or not.
pres.isna()

## following code will show which rows have missing values.
# pres[pres.Integrity.isna()]

## Get the counts of the columns with missing values.
pres.isna().sum()

pres.isna().mean()

#^ Duplicates

pres.drop_duplicates()

## Because none of the above rows are complete copies, the above call does nothing.


## By default, it removes duplicate rows based on duplicate values found in all columns.

#! To remove duplicates rows with duplicate values found only in specific column(s), use subset

#% To keep only the first president from each party, do the following

pres.drop_duplicates(subset= 'Party')

#% To remove duplicates and keep last only last president from each party, use 'last'.

pres.drop_duplicates(subset= 'Party', keep = 'last')

#% To remove all duplicates, use keep = False

pres.drop_duplicates(subset= 'Party', keep = False)


pres.assign(first_in_party_seq = lambda df_ : df_.Party != df.Party.shift(1)).loc[lambda df_ : df_.first_in_party_seq]

## In the above code, pres.assign(first_in_party_seq = lambda df_ : df_.Party != df.Party.shift(1)) creates a column that indicates whether it is not the same as the next value or in other words, if it is the first entry in a sequence.