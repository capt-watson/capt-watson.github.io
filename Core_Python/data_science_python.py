#! Data Frame - It is an object that is useful in representing data in the form of
#! rows and columns.

#& Data Frames are generally created from .csv( Comma separated values) files, Excel
#& Spreadsheet file, Python dictionaries, list of tuples or list of dictionaries.

#% Python package 'pandas' is useful for data analysis and manipulation.

#~ 'xlrd' is a package that is useful to retrieve data from Excel files.

import pandas as pd


## df = pd.read_excel("C:/Users/shekh/Projects/Python_Tutorials/Core_Python/empdata.xlsx","Sheet1")

# df = pd.read_csv('C:/Users/shekh/Projects/Python_Tutorials/Core_Python/empdata.csv')

# df

## To get the index information for this df
# df.index

#~    empid               ename      sal         doj
#~ 0   1001      Veronica Cruiz  95050.0  14-02-2008
#~ 1   1002        Ariana White  45845.0  21-05-2012
#~ 2   1003         Grace Smith  64215.0  24-08-2018
#~ 3   1004         Everly John  58785.0  05-04-2010
#~ 4   1005  Valentina Eastwood  26589.5  13-09-2021
#~ 5   1006        Allison Rode  63485.5  24-07-2011

#! Knowing number of rows and columns

# df.shape
#~ (6, 4)

#% Retrieve only rows or columns, we can read that number from tuple as:

# r,c = df.shape
# print(r)
#~ 6

#! Retrieving rows from data frame
#% The method head() gives the first 5 rows and method tail() returns the last 5 rows:

# df.head()
#~    empid               ename      sal         doj
#~ 0   1001      Veronica Cruiz  95050.0  14-02-2008
#~ 1   1002        Ariana White  45845.0  21-05-2012
#~ 2   1003         Grace Smith  64215.0  24-08-2018
#~ 3   1004         Everly John  58785.0  05-04-2010
#~ 4   1005  Valentina Eastwood  26589.5  13-09-2021

# df.tail()
#~    empid               ename      sal         doj
#~ 1   1002        Ariana White  45845.0  21-05-2012
#~ 2   1003         Grace Smith  64215.0  24-08-2018
#~ 3   1004         Everly John  58785.0  05-04-2010
#~ 4   1005  Valentina Eastwood  26589.5  13-09-2021
#~ 5   1006        Allison Rode  63485.5  24-07-2011

#% To read only the first 2 rows, use head(2):

# df.head(2)
#~    empid           ename      sal         doj
#~ 0   1001  Veronica Cruiz  95050.0  14-02-2008
#~ 1   1002    Ariana White  45845.0  21-05-2012

# df.tail(2) 
#~   empid               ename      sal         doj
#~4   1005  Valentina Eastwood  26589.5  13-09-2021
#~5   1006        Allison Rode  63485.5  24-07-2011

#% Retrieving a range of rows

# df[2:5]
#~    empid               ename      sal         doj
#~ 2   1003         Grace Smith  64215.0  24-08-2018
#~ 3   1004         Everly John  58785.0  05-04-2010
#~ 4   1005  Valentina Eastwood  26589.5  13-09-2021
# df[:2]
#~    empid           ename      sal         doj
#~ 0   1001  Veronica Cruiz  95050.0  14-02-2008
#~ 1   1002    Ariana White  45845.0  21-05-2012
# df[::2]
#~   empid               ename      sal         doj
#~ 0   1001      Veronica Cruiz  95050.0  14-02-2008
#~ 2   1003         Grace Smith  64215.0  24-08-2018
#~ 4   1005  Valentina Eastwood  26589.5  13-09-2021
# df[5:0:-1]
#~   empid               ename      sal         doj
#~ 5   1006        Allison Rode  63485.5  24-07-2011
#~ 4   1005  Valentina Eastwood  26589.5  13-09-2021
#~ 3   1004         Everly John  58785.0  05-04-2010
#~ 2   1003         Grace Smith  64215.0  24-08-2018
#~ 1   1002        Ariana White  45845.0  21-05-2012

#% Retrieve column names from data frame.
# df.columns
#~ Index(['empid', 'ename', 'sal', 'doj'], dtype='object')

#% To retrieve column data
# df.empid  
#~ 0    1001
#~ 1    1002
#~ 2    1003
#~ 3    1004
#~ 4    1005
#~ 5    1006

# df['empid']

#% Retrieve data from multiple columns
#* format:
#* df[[list of column names]]

# df[['empid','ename']]   
#~    empid               ename
#~ 0   1001      Veronica Cruiz
#~ 1   1002        Ariana White
#~ 2   1003         Grace Smith
#~ 3   1004         Everly John
#~ 4   1005  Valentina Eastwood
#~ 5   1006        Allison Rode

#% Finding maximum & minimum values
# df['sal'].max()
#~ 95050.0
# df['sal'].min()
#~ 26589.5

#% Displaying Statistical Information

# df.describe()
## describe() method displays:

## - total of values (count)
## - average(mean)
## - standard deviation (std)
## - minimum(min)
## - 25% of the total values
## - 50% of the total values
## - 75% of the total values
## - maximal(max)

#% Performing queries o data

# df[df.sal>50000]

## Will return the salary more than 50000

#! Following code will display the line with max salary

# df[df.sal == df.sal.max()]

## Following code will return only those lines with sal >= 50000

# df[['empid','ename']][df.sal>50000]

#@ Setting column as Index

# df1 = df.set_index('empid')

## To modify the original 'df' and set empid as colum, we should
## add 'inplace = True' as shown below

# df.set_index('empid', inplace=True)

## following code will return data of only index 1004.
# df.loc[1004]

#@ Resetting the Index

# df.reset_index(inplace=True)

# df

#@ Sorting the data

df = pd.read_csv('C:/Users/shekh/Projects/Python_Tutorials/Core_Python/empdata.csv',parse_dates=['doj'],dayfirst=True)

## Here we are loading the data empdata.csv file and informing
## to take 'doj' as data type field using parse_dates option.

# print(df)

# df1 = df.sort_values('doj')   ## sort in ascending order
# df1

# df1 = df.sort_values('doj',ascending=False)
# df1

## To sort on 'doj' in descending order and in 'sal' in ascending ## order. This means, when two employees have same 'doj, then
## their salaries will be sorted into ascending order.

df1 = df.sort_values(by=['doj', 'sal'],ascending=[False, True])
df1

#@ Handling missing data

## we can use fillna() method to replace the Na or NaN values
## by a specified values by 0.

# df1 = df.fillna(0)  ## Will replace missing values in df by 0

## To fill 'ename' column with 'Name missing', 'sal' with 0.00
## and 'doj' with '00-00-00', supply these values in a dict to
## fillna() method as shown below:

# df1 = df.fillna({'ename':'name missing', 'sal': '0.00', 'doj': 00-00-00})

## To remove those rows having Na and NaN values, use dropna()

# df1 = df.dropna()