import pandas as pd

url = 'https://github.com//mattharrison/datasets/raw/master/data/vehicles.csv.zip'

df = pd.read_csv(url, low_memory=False)

make = df.make

# make.value_counts()

#^ If every value is unique or free form text, it is not categorical.

make.shape, make.nunique()
## DataFrame.shape. Returns a tuple representing the dimensionality of the DataFrame
## DataFrame.nunique(axis=0, dropna=True). Counts number of distinct elements in specified axis.
#~ ((41144,), 136)

#! category type uses very less memory

cat_make = make.astype('category')

# make.memory_usage(deep=True)
# 2277247

# cat_make.memory_usage(deep=True)
# 94804

# %timeit cat_make.str.upper() 
# #~ 413 µs ± 868 ns per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

# %timeit make.str.upper()
# #~ 4.4 ms ± 18.9 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

#* If the above code gives error, reload the python and error will go away.

make_type = pd.CategoricalDtype(categories=sorted(make.unique()),ordered=True)
ordered_make = make.astype(make_type)

## pandas.CategoricalDtype(categories=None, ordered=False)
## the above code returns ordinal categorical list

ordered_make.max()
#~ 'smart'

#^ sort the series according to the order.

ordered_make.sort_values()

#! The .cat Accessor

## .cat is called an accessor object. It allows you to access attributes and methods that are specific to categorical columns. There are similar accessors in pandas: .dt for date-time, .str for string, .plot for plotting and so on.

# cat_make.cat.rename_categories([c.lower() for c in cat_make.cat.categories])
#~ 
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
#~ Name: make, Length: 41144, dtype: category
#~ Categories (136, object): ['am general', 'asc incorporated', 'acura', 'alfa romeo', ..., 'volvo', 'wallace environmental', 'yugo', 'smart']


## The above code renames the categories to lowercase.

# ordered_make.cat.rename_categories({c:c.lower() for c in ordered_make.cat.categories})

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
#~ Name: make, Length: 41144, dtype: category
#~ Categories (136, object): ['am general' < 'asc incorporated' < 'acura' < 'alfa romeo' ... 'volvo' < 'wallace environmental' < 'yugo' < 'smart']

# ordered_make.cat.reorder_categories(sorted(cat_make.cat.categories,key=str.lower))

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
#~ Categories (136, object): ['Acura' < 'Alfa Romeo' < 'AM General' < 'American Motors Corporation' ... 'Volvo' < 'VPG' < 'Wallace Environmental' < 'Yugo']

## Series.cat.reorder_categories(self, *args, **kwargs)

## sorted(iterable, key=key, reverse=reverse)

## The above code sorts the list ignoring the case.

#! Category Gotchas

#@ The first() method returns the first n rows

#^ Optional parameter for groupby() method called 'observed = True'

## observed = True, tells it to only include results for which there are values.

cat_make.iloc[:100].groupby(cat_make.iloc[:100],observed=True).first()

def generalize_topn(ser, n=5, other='Other'):
    topn = ser.value_counts().index[:n]
    if isinstance(ser.dtype, pd.CategoricalDtype):
        ser = ser.cat.set_categories(topn.set_categories(list(topn)+[other]))
    return ser.where(ser.isin(topn), other)

## Series.cat.set_categories(*args, **kwargs). Sets the categories to the specified new_categories

cat_make.pipe(generalize_topn, n=20, other='NA')

## The pipe() method allows one to apply one or more functions to the DataFrame object. Syntax= dataframe.pipe(func, args, kwargs) args	Optional, An iterable object with positional arguments that can be used in the function, kwargs	Optional. A dictionary with keyword arguments that can be used in the function.

def generalize_mapping(ser, mapping, default):
    seen = None
    res  = ser.astype(str)
    for old, new in mapping.items():
        mask = ser.str.contains(old)
        if seen is None:
            seen = mask
        else:
            seen |= mask                #% if seen already has mask value, it will append the new mask value to it as well.
        res = res.where(~mask, new)     #% If mask exists, do not keep its value instead replace it with the 'new' value.
        res = res.where(seen, default)
    return res.astype('category')

generalize_mapping(cat_make, {'Ford':'US', 'Tesla':'US', 'Chevrolet':'US', 'Dodge':'US','Oldsmobile':'US', 'Plymouth':'US','BMW':'German'},'Other')

