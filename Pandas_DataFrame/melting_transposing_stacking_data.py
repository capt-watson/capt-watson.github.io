import pandas as pd
from tweak_jb import tweak_jb

pd.set_option('future.no_silent_downcasting', True)

url = 'https://github.com/mattharrison/datasets/raw/master/data/2020-jetbrains-python-survey.csv'

jb = pd.read_csv(url, dtype='unicode')

jb2 = tweak_jb(jb)

#^ Melting Data

#% OLAP (Online Analytical Processing) databases are organized into cubes that make it easier to retrieve and analyze data. OLAP data is organized hierarchically and stored in cubes instead of tables. OLAP is optimized for querying and reporting, instead of processing transactions. OLAP data is derived from Online Transactional Processing (OLTP) databases, which are commonly stored in data warehouses.

## example of Wide Format: Here names represent name of salesman. Each row represents data for one salesman at a time.

#~ name    jan    feb    mar    apr  ... dec
#~ jim     $100   $200   $200   $300     $300
#~ mike    $200   $250   $50    $100     $170



## example of Long Format (aka tidy data):

#~ name    month    kpi     value
#~ jim     jan      amount  100
#~ jim     feb      amount  120
#~ ...
#~ jim     jan      items   10
#~ jim     feb      items   10
#~ ...
#~ mike    dec      amount  170
#~ ...
#~ mike    dec      items   5

#* The advantages of this approach are the following:
## 
#! You don’t waste space if some data is missing.
#! If this happens then a row will not exist and that is all.
## 
#! You do not have to modify the table structure if for some reason a new feature is added, you just modify the data by adding rows with the new feature as needed.

#^ converting a wide data to long data:

scores = pd.DataFrame({
    'name' : ['Adam', 'Bob', 'Dave', 'Fred'],
    'age':   [15, 16, 16, 15],
    'test1' : [95,81,90, None],
    'test2' : [80, 82, 84, 88],
    'teacher' : ['Barbera', 'Hillary', 'Susan', 'Dolly']
})

#~ 0	Adam	15	    95.0	80	    Barbera
#~ 1	Bob	    16	    81.0	82	    Hillary
#~ 2	Dave	16	    90.0	84	    Susan
#~ 3	Fred	15	    NaN	    88	    Dolly

#! To convert data from wide to long format, you can use the melt() function.

scores.melt(id_vars=['name', 'age'], value_vars=['test1', 'test2'])


#~     name	    age	    variable	value
#~ 0	Adam	15	    test1	    95.0
#~ 1	Bob	    16	    test1	    81.0
#~ 2	Dave	16	    test1	    90.0
#~ 3	Fred	15	    test1	    NaN
#~ 4	Adam	15	    test2	    80.0
#~ 5	Bob	    16	    test2	    82.0
#~ 6	Dave	16	    test2	    84.0
#~ 7	Fred	15	    test2	    88.0


#! To change the name of the variable to 'test' and to change the value column name to 'score':

scores.melt(id_vars=['name', 'age'], value_vars=['test1', 'test2'], var_name= 'test', value_name= 'score')

#~  	   name	    age	    test	score
#~         Adam	    15	    test1	95.0
#~ 1	   Bob	    16	    test1	81.0
#~ 2	   Dave	    16	    test1	90.0
#~ 3       Fred	    15	    test1	NaN
#~ 4	   Adam	    15	    test2	80.0
#~ 5	   Bob	    16	    test2	82.0
#~ 6	   Dave	    16	    test2	84.0
#~ 7	   Fred	    15	    test2	88.0


scores.melt(id_vars=['name', 'age', 'teacher'], value_vars=['test1', 'test2'], var_name= 'test', value_name= 'score')


#~      name	age	    teacher	    test	score
#~ 0	Adam	15	    Barbera	    test1	95.0
#~ 1	Bob	    16	    Hillary	    test1	81.0
#~ 2	Dave	16	    Susan	    test1	90.0
#~ 3	Fred	15	    Dolly	    test1	NaN
#~ 4	Adam	15	    Barbera	    test2	80.0
#~ 5	Bob	    16	    Hillary	    test2	82.0
#~ 6	Dave	16	    Susan	    test2	84.0
#~ 7	Fred	15	    Dolly	    test2	88.0

#^ Un-melting Data

## Using a pivot table, one can go from long format to wide format.

melted = scores.melt(id_vars=['name', 'age', 'teacher'], value_vars= ['test1', 'test2'], var_name ='test', value_name='score')

## following code will reset the index.

melted.pivot_table(index=['name', 'age', 'teacher'], columns='test', values='score').reset_index()

#~ test	name	age	teacher	test1	test2
#~ 0	Adam	15	Barbera	95.0	80.0
#~ 1	Bob	    16	Hillary	81.0	82.0
#~ 2	Dave	16	Susan	90.0	84.0
#~ 3	Fred	15	Dolly	NaN	    88.0


#! The above results can also be obtained by groupby method()


# melted.groupby(['name', 'age', 'teacher', 'test'])\
#       .score\
#       .mean()\
#       .unstack()\
#       .reset_index()


#^ Transposing Data

#! Pandas uses numeric index values by default. When the numeric index goes into column, it takes up less horizontal space and one can see more data without having to scroll around.


#^ Stacking and Unstacking

#! unstack() method moves an index level into the columns. It creates a hierarchical column.

#! stack() method moves a multi-level column into the index.

jb2.groupby(['country_live', 'are_you_datascientist'],observed=True).size()

#~ country_live  are_you_datascientist
#~ Algeria       False                    12
#~               True                      5
#~               Other                     1
#~ Argentina     False                    89
#~               True                     16
#~                                        ..
#~ Venezuela     True                      4
#~               Other                     2
#~ VietNam       False                    16
#~               True                     14
#~               Other                     3
#~ Length: 210, dtype: int64

jb2.groupby(['country_live', 'are_you_datascientist'],observed=True)\
  .size()\
  .unstack()

#! By unstacking, we have moved the inner index ('are you datascientist) to a column.Now the series has been changed to a dataframe.
 
#~ are_you_datascientist	False	True	Other
#~ country_live			
#~ Algeria	                12.0	5.0	    1.0
#~ Argentina	            89.0	16.0	4.0
#~ Armenia	                15.0	2.0	    NaN
#~ Australia	            210.0	50.0	14.0
#~ Austria	                93.0	32.0	3.0
#~ ...	                    ...	    ...	    ...
#~ United States	        2008.0	589.0	100.0
#~ Uruguay	                10.0	9.0	    1.0
#~ Uzbekistan	            3.0	    1.0	    NaN
#~ Venezuela	            16.0	4.0	    2.0
#~ VietNam	                16.0	14.0	3.0
#~ 76 rows × 3 columns

#! We can also pull up the country index (which is outer index), we could specify it by name or by position. The position is 0 for outer index (country_live) and 1 for (are_you_datascientist).

jb2.groupby(['country_live', 'are_you_datascientist'],observed=True)\
   .size()\
   .unstack(0)

#~ country_live	            Algeria 	Argentina	Armenia	 Australia	Austria	 Bangladesh	 Belarus

#~ are_you_datascientist

#~                  False	 12.0	       89.0	      15.0	    210.0	  93.0	    22.0	  41.0
#~                  True	  5.0	       16.0	       2.0	     50.0	  32.0	    10.0	   4.0
#~                  Other	  1.0	        4.0	      NaN	     14.0	   3.0	     1.0	   2.0

## Above code using index name instead of index position:

jb2.groupby(['country_live', 'are_you_datascientist'],observed=True)\
   .size()\
   .unstack('country_live')


#~ country_live	            Algeria 	Argentina	Armenia	 Australia	Austria	 Bangladesh	 Belarus

#~ are_you_datascientist

#~                  False	 12.0	       89.0	      15.0	    210.0	  93.0	    22.0	  41.0
#~                  True	  5.0	       16.0	       2.0	     50.0	  32.0	    10.0	   4.0
#~                  Other	  1.0	        4.0	      NaN	     14.0	   3.0	     1.0	   2.0


#^ Stacking

#! Stacking puts column labels into the index.

#! Unstacking moves index labels into columns.

# jb2.pivot_table(index= 'country_live', aggfunc={'age': ['min', 'max'], 'company_size': ['min', 'max']},observed=True)\
#    .stack(0)

#~ 		                        max	    min
#~ country_live	     		
#~ Algeria	            age	    60	    18
#~              company_size	5000	 1
#~ Argentina	        age	    60	    18
#~              company_size	5000	1
#~ Armenia	            age	    30	    18
#~ ...                  ...	    ...	    ...
#~ Uzbekistan   company_size	5000	1
#~ Venezuela	        age	    50	    18
#~              company_size	5000	1
#~ VietNam	            age	    60	    18
#~              company_size	5000	1

#~ 152 rows × 2 columns

jb2.pivot_table(index='country_live',aggfunc={'age' : ['min','max'], 'company_size' : ['min','max']},observed=True)\
    .stack(1)\
    .swaplevel()

#~ 		            age	company_size
#~    country_live		
#~ max	Algeria	    60	5000
#~ min	Algeria	    18	1
#~ max	Argentina	60	5000
#~ min	Argentina	18	1
#~ max	Armenia	    30	5000
#~ ...	.       ..	...	...
#~ min	Uzbekistan	21	1
#~ max	Venezuela	50	5000
#~ min	Venezuela	18	1
#~ max	VietNam	    60	5000
#~ min	VietNam	    18	1

#^ Flattening Hierarchical Indexes anc columns

