import pandas as pd
from shiv_parvati import shiv_parvati

url= 'https://github.com/mattharrison/datasets/raw/master/data/siena2018-pres.csv'

df = pd.read_csv(url, index_col=0)

pres =shiv_parvati(df)

#^ Renaming of an Index

## Use rename() method to update the index values.

def new_name(val):
    names = val.split()
    return ' '.join([f'{names[0][0]}.',*names[1:]])

## The string format method will extract the first word and then then the first letter of the first word and will add '.' dot after the truncated string. This string format method will then add all the remaining words from the name string starting from the 1st index value. Here the space ' ' is used as separator between two consecutive words

pres.set_index('President').rename(new_name)

#^ Resetting the index

## will add row index number to the new index names. President names will no longer be the index.
pres.set_index('President').reset_index()

#^ Dataframe Indexing, filtering & Querying

## Filtering out all presidents with average rank below 10
lt10 = pres.Average_rank < 10

pres[lt10]

## Checking if they are Republican:
pres[lt10 & (pres.Party == 'Republican')]


## query() method allows you to call methods, include variables and combine conditional expressions inside a string.

#! Always ensure to put parenthesis around multiple conditions in index operations if you inline them.

pres[(pres.Average_rank <10) & (pres.Party == 'Republican')]


## Using query() method to obtain the above results. In query() method, we do not need to worry about precedence and parenthesis.
pres.query('Average_rank < 10 and Party == "Republican"')


## To refer to a variable inside of the string, use  @ symbol before the variable name.
lt10 = pres.Average_rank < 10
pres.query('@lt10 and Party == "Republican"')


#^ indexing by Position using iloc[]

## Print only the row at 1st index position
pres.iloc[[1]]

## Print only the rows at 0th, 5th and 10th index positions
pres.iloc[[0, 5, 10]]

## Print only the rows between 0th, 11th index positions with a step of 5.
pres.iloc[0:11:5]


#% We can pass functions into the index operations.

## Following operations will give same results:
pres.iloc[[0, 5, 10]]

pres.iloc[lambda df: [0,5,10]]


## Following operations will pull out the second column (index position 1). Because we are using a scalar for the column indexer, it will return a series.
pres.iloc[[0, 5, 10], 1]   ## syntax : [[rows, columns]]

#~ 6     John Quincy Adams
#~ 11        James K. Polk
#~ Name: President, dtype: object
#~ 1     George Washington


## Following operations will return a dataframe.
pres.iloc[[0,5,10], [1]]

#~ President
#~ 1	George Washington
#~ 6	John Quincy Adams
#~ 11	James K. Polk


## Following operations will return all the rows for columns at index positions 1 and 2.
pres.iloc[:,[1,2] ]

#! Or

pres.iloc[:, 1:3]

#^ Indexing by Name

#$ .iloc follows half-open interval(includes the first index but not the last)
#$ .loc follows the closed interval(includes both the first index and the end index)

pres = pres.set_index('Seq')

## following operations will throw an error as the index is not an integer index due to the presence of entry 22/24 in the seq column which is the index column.

# pres.loc[1:5]

## Following operations will not throw an error as we are searching the index using the strings.
pres.loc['1':'5']

## Following operations will set 'Party' column as Index and return rows with 'Whig' as Index.
pres.set_index('Party').loc['Whig']

## Following operations will return a series if we only use scalar value (i.e. not as a list)
pres.set_index('Party').loc['Federalist']

#~ President                         John Adams
#~ Background                                 3
#~ Imagination                               13
#~ Integrity                                  4
#~ Intelligence                               4
#~ Luck                                      24
#~ Willing_to_take_risks                     14
#~ Ability_to_compromise                     31
#~ Executive_ability                         21
#~ Leadership_ability                        21
#~ Communication_ability                     13
#~ Overall_ability                            8
#~ Party_leadership                          28
#~ Relations_with_Congress                   17
#~ Court_appointments                         4
#~ Handling_of_economy                       13
#~ Executive_appointments                    15
#~ Domestic_accomplishments                  19
#~ Foreign_policy_accomplishments            13
#~ Avoid_crucial_mistakes                    16
#~ Experts'_view                             10
#~ Overall                                   14
#~ Average_rank                              13
#~ Quartile                                 2nd
#~ Name: Federalist, dtype: object


## Following operations will return a dataframe if we enter values as as a list
pres.set_index('Party').loc[['Federalist']]


#^ Slicing with string indexes.

#* Must Remember:

#! Sort the indexes before slicing it.
#! One can slice with partial values.

pres.set_index('Party').sort_index().loc['Democratic':'Independent']

## Following operations will slice the index from name beginning with letter 'C' and ending with name 'Thomas Jefferson'. Also it will slice the index from the party to Integrity.
pres.set_index('President').sort_index().loc['C': 'Thomas jefferson', 'Party':'Integrity']


## Following operations will return an error as we can not use partial strings on categorical indexes.
pres.set_index('President').sort_index().loc['D':'J']


## Following operations will convert Party from category type to string type and then change Party column to Index.
pres.assign(Party = pres.Party.astype(str)).set_index('Party').sort_index().loc['D':'J']


## Following operations will set 'President' column as index, sort it then sort the columns axis and then slice the index rows from 'C' to 'T' and columns from 'B' to 'D'.
pres.set_index('President').sort_index().sort_index(axis = 'columns').loc['C':'Thomas Jefferson', 'B':'D']

#^ Filtering with Functions & .loc

## Following operations will slice first three columns and filter out all rows having Average_rank less than 10.
#$ Advantage of passing a function into .loc is that the function will receive the current state of the dataframe.
pres.loc[pres.Average_rank < 10, lambda df_ : df_.columns[:3]]


#~ President	Party	Background
#~ Seq			
#~ 1	George Washington	Independent	7
#~ 3	Thomas Jefferson	Democratic-Republican	2
#~ 4	James Madison	Democratic-Republican	4
#~ 5	James Monroe	Democratic-Republican	9
#~ 16	Abraham Lincoln	Republican	28
#~ 26	Theodore Roosevelt	Republican	5
#~ 32	Franklin D. Roosevelt	Democratic	6
#~ 33	Harry S. Truman	Democratic	31
#~ 34	Dwight D. Eisenhower	Republican	11

#^ .query vs .loc

## If you do lot of chaining (recommended), .query has the advantage of working on the intermediate dataframe. On the flipside, .query doesn't support column selection, but .loc does.

