import numpy as np
import pandas as pd
import random

pd.options.display.max_rows = 999
pd.set_option('display.max_rows',999)
pd.set_option('display.max_columns',999)
pd.set_option('display.width',1000)

url = 'https://github.com/mattharrison/datasets/raw/master/data/vehicles.csv.zip'
df = pd.read_csv(url,low_memory=False) 

city_mpg = df.city08
highway_mpg = df.highway08
make = df.make

make

#~ 0        Alfa Romeo
#~ 1           Ferrari
#~ 2             Dodge
#~ 3             Dodge
#~ 4            Subaru
#~             ...    
#~ 41139        Subaru
#~ 41140        Subaru
#~ 41141        Subaru
#~ 41142        Subaru
#~ 41143        Subaru
#~Name: make, Length: 41144, dtype: object

#% To convert the above dtype from object to string type, use .astype() method:

make.astype('string')

#~ 0        Alfa Romeo
#~ 1           Ferrari
#~ 2             Dodge
#~ 3             Dodge
#~ 4            Subaru
#~             ...    
#~ 41139        Subaru
#~ 41140        Subaru
#~ 41141        Subaru
#~ 41142        Subaru
#~ 41143        Subaru
#~ Name: make, Length: 41144, dtype: string

#! Categorical Strings

#% If string column has less number of elements in it, one should use a categorical type fo them. It will have access to many of the same string manipulation methods. Main advantage here is memory saving and performance improvements as the operations need to be done only on the individual categories & not each value in the series.

make.astype('category')

#~ 0        Alfa Romeo
#~ 1           Ferrari
#~ 2             Dodge
#~ 3             Dodge
#~ 4            Subaru
#~             ...    
#~ 41139        Subaru
#~ 41140        Subaru
#~ 41141        Subaru
#~ 41142        Subaru
#~ 41143        Subaru
#~ Name: make, Length: 41144, dtype: category
#~ Categories (136, object): ['AM General', 'ASC Incorporated', 'Acura', 'Alfa Romeo', ..., 'Volvo', 'Wallace Environmental', 'Yugo', 'smart']

#! The str Accessor

#% The object 'string' & 'category' types have a .str accessor that provides string manipulation methods.
 
make.str.lower()  

#~ 0        alfa romeo
#~ 1           ferrari
#~ 2             dodge
#~ 3             dodge
#~ 4            subaru
#~             ...    
#~ 41139        subaru
#~ 41140        subaru
#~ 41141        subaru
#~ 41142        subaru
#~ 41143        subaru
#~ Name: make, Length: 41144, dtype: object

 ## .find() will return index position of the first occurrence of the substring, only if the substring exists in the input string. If the string is not found, then the function will return -1. .find() is case sensitive.

make.str.find('a')

#~ 0        3
#~ 1        4
#~ 2       -1
#~ 3       -1
#~ 4        3
#~         ..
#~ 41139    3
#~ 41140    3
#~ 41141    3
#~ 41142    3
#~ 41143    3
#~ Name: make, Length: 41144, dtype: int64

make.str.extract(r'(\W)')  ## will extract all non alpha numeric characters

make.str.extract(r'([^A-Z a-z])') ## will extract all non alpha numeric characters (same as above)


#~ 0	NaN
#~ 1	NaN
#~ 2	NaN
#~ 3	NaN
#~ 4	NaN
#~ ...	...
#~ 41139	NaN
#~ 41140	NaN
#~ 41141	NaN
#~ 41142	NaN
#~ 41143	NaN
#~ 41144 rows × 1 columns

## The above method will return all missing values.


make.str.extract(r'([^a-z A-Z 0-9])', expand= False).value_counts() 

#~ make
#~ -    1727
#~ .      46
#~ ,       9
#~ Name: count, dtype: int64

## Here - 1727 is the count of - chars in place of values in the series.
## Here . 46 is the count of '.' chars in place of values in the series.
## Here , 9 is the count of ';' chars in place of values in the series

#^  will return a Series if expand=False.
#^ill return a DataFrame with one column if expand=True.

#! Splitting

#% Splitting is useful in removing dashes from a string, e.g. age 20-29, 30-39 and 40-49 etc as pandas can not handle dashes properly.

age = pd.Series(['8-10','11-15', '11-15', '61-65', '46-50'])

age.str.split('-', expand=True)  ## expand=True presents output data without list.


#~ 0	1
#~ 0	8	10
#~ 1	11	15
#~ 2	11	15
#~ 3	61	65
#~ 4	46	50

# age.str.split('-', expand=True).iloc[:,0]  ## Will print only the 0th column and everything from the rows.

#~ 0     8
#~ 1    11
#~ 2    11
#~ 3    61
#~ 4    46
#~ Name: 0, dtype: object

age.str.split('-', expand=True).iloc[:,0].astype(int)  ## We convert the object datatype to integer type.

#~ 0     8
#~ 1    11
#~ 2    11
#~ 3    61
#~ 4    46
#~ Name: 0, dtype: int32

age.str.slice(-2).astype(int)       ## slice() method accepts (start, stop, step) as argument.

#~ 0    10
#~ 1    15
#~ 2    15
#~ 3    65
#~ 4    50
#~ dtype: int32

#% The above result can also be obtained using the following method.

age.str[-2:].astype((int))  ## here the string starts at -2 index value and goes till the end.

#~ 0    10
#~ 1    15
#~ 2    15
#~ 3    65
#~ 4    50
#~ dtype: int32


#% Calculate the average of the above mentioned bin.

age.str.split('-', expand = True).astype(int).mean(axis='columns')  ## Will return the average of both the columns

#~ 0     9.0
#~ 1    13.0
#~ 2    13.0
#~ 3    63.0
#~ 4    48.0
#~ dtype: float64

def between(row):
    return random.randint(*row.values)

age.str.split('-', expand = True).astype(int).apply(between, axis='columns') 

## Will return a random number between two numbers of each row after splitting the string and converting it into integer.

#% apply(func, axis='rows/columns'). Apply method is used only with the func created by the user. 

#~ 0     8
#~ 1    12
#~ 2    14
#~ 3    61
#~ 4    49
#~ dtype: int64

#! Replacing Text

make.str.replace('A', 'Å')

#~ 0        Ålfa Romeo
#~ 1           Ferrari
#~ 2             Dodge
#~ 3             Dodge
#~ 4            Subaru
#~             ...    
#~ 41139        Subaru
#~ 41140        Subaru
#~ 41141        Subaru
#~ 41142        Subaru
#~ 41143        Subaru
#~ Name: make, Length: 41144, dtype: object

## str.replace would replace a capital 'A' with a capital letter 'Å' for all the occurrences of the capital letter 'A'.

## str.replace is used to replace only a single character in a string or substring.

## .replace would replace the entire string or replace mapping of complete strings.



make.replace('A', 'Å')

## make.replace method did not make any changes as it is looking for whole string consisting of letter 'A'.



make.replace('A', 'Å', regex=True)

#~ 0        Ålfa Romeo
#~ 1           Ferrari
#~ 2             Dodge
#~ 3             Dodge
#~ 4            Subaru
#~             ...    
#~ 41139        Subaru
#~ 41140        Subaru
#~ 41141        Subaru
#~ 41142        Subaru
#~ 41143        Subaru
#~ Name: make, Length: 41144, dtype: object

## Here regex is used for replacing just a portion of a string.

#! Other string operations

make.str.capitalize()   ## All strings have their first letter capitalized

make.str.casefold()     ## All strings have their first letter in lowercase

make.str.cat(others=None, sep=' ', na_rep=None, join='inner')

## All the strings of this series would be joined with a given separator (space).


#~ 'Alfa Romeo Ferrari Dodge Dodge Subaru Subaru Subaru Toyota Toyota Toyota Toyota Volkswagen Volkswagen Volkswagen Dodge Volkswagen Volvo Volvo Audi Audi BMW BMW BMW Buick Buick Dodge Buick Buick Buick Buick Buick Cadillac Cadillac Cadillac Cadillac Chevrolet Dodge Chevrolet Chevrolet Chevrolet Chevrolet Chrysler CX Automotive CX Automotive Nissan Nissan Nissan Dodge Dodge Dodge Dodge Dodge Dodge Dodge Dodge Dodge Ford Ford Dodge Ford Ford Ford Ford Ford Hyundai Hyundai Hyundai Infiniti Infiniti Dodge Lexus Mercury Mercury Mercury Mercury Mazda Mazda Mazda Mazda Mazda Dodge Oldsmobile Oldsmobile Oldsmobile.

## Parameters for others= series, index, DataFrame, np.ndarray or list-like. If others is specified, this function concatenates the Series/Index and elements of others element-wise. If others is not passed, then all values in the Series/Index are concatenated into a single string with a given sep.

## na_rep : It means NA representation. Representation that is inserted for all missing values. If na_rep is None, and others is None, missing values in the Series/Index are omitted from the result. If na_rep is None, and others is not None, a row containing a missing value in any of the columns (before concatenation) will have a missing value in the result.


make.str.center(15,fillchar=' ')  ## Aligns characters of the column to the center with column width = 15

#~ 0           Alfa Romeo  
#~ 1            Ferrari    
#~ 2             Dodge     
#~ 3             Dodge     
#~ 4             Subaru    
#~               ...       
#~ 41139         Subaru    
#~ 41140         Subaru    
#~ 41141         Subaru    
#~ 41142         Subaru    
#~ 41143         Subaru    
#~ Name: make, Length: 41144, dtype: object

make.str.contains('rari', case=True, flags=0, na=np.nan, regex=True)
## Test if pattern or regex is contained within a string of a Series or Index.

#~ 0        False
#~ 1         True
#~ 2        False
#~ 3        False
#~ 4        False
#~          ...  
#~ 41139    False
#~ 41140    False
#~ 41141    False
#~ 41142    False
#~ 41143    False
#~ Name: make, Length: 41144, dtype: bool

make.str.count('Romeo',flags=0)
## Count occurrences of pattern in each string of the Series/Index. Make sure that the pattern follows upper or lower case as given in the series.

#~ 0        1
#~ 1        0
#~ 2        0
#~ 3        0
#~ 4        0
#~         ..
#~ 41139    0
#~ 41140    0
#~ 41141    0
#~ 41142    0
#~ 41143    0
#~ Name: make, Length: 41144, dtype: int64


make.str.decode('ascii')
## Decode character string in the Series/Index using indicated encoding.

#~ 0       NaN
#~ 1       NaN
#~ 2       NaN
#~ 3       NaN
#~ 4       NaN
#~          ..
#~ 41139   NaN
#~ 41140   NaN
#~ 41141   NaN
#~ 41142   NaN
#~ 41143   NaN
#~ Name: make, Length: 41144, dtype: float64


make.str.encode('ascii')
## Encode character string in the Series/Index using indicated encoding.

#~ 0        b'Alfa Romeo'
#~ 1           b'Ferrari'
#~ 2             b'Dodge'
#~ 3             b'Dodge'
#~ 4            b'Subaru'
#~              ...      
#~ 41139        b'Subaru'
#~ 41140        b'Subaru'
#~ 41141        b'Subaru'
#~ 41142        b'Subaru'
#~ 41143        b'Subaru'
#~ Name: make, Length: 41144, dtype: object

make.str.endswith('ari')
## Test if the end of each string element matches a pattern.

#~ 0        False
#~ 1         True
#~ 2        False
#~ 3        False
#~ 4        False
#~          ...  
#~ 41139    False
#~ 41140    False
#~ 41141    False
#~ 41142    False
#~ 41143    False
#~ Name: make, Length: 41144, dtype: bool

make.str.extract(r'([A])(\w+)', flags=0, expand=True)
## For each subject string in the Series, extract groups from the first match of regular expression pat.

## This code searches for pattern starting with the chars enclosed in [] and returns it with all the chars following the first character in that string.

## expand = True returns output in the form of a dataframe (rows and columns). expand=False will return output in the form of series with only one column.


#~ 0	1
#~ 0	A	lfa
#~ 1	NaN	NaN
#~ 2	NaN	NaN
#~ 3	NaN	NaN
#~ 4	NaN	NaN
#~ ...	...	...
#~ 41139	NaN	NaN
#~ 41140	NaN	NaN
#~ 41141	NaN	NaN
#~ 41142	NaN	NaN
#~ 41143	NaN	NaN
#~ 41144 rows × 2 columns
