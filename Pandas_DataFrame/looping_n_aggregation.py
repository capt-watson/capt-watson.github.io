import pandas as pd

#! For loops

## for loop is a slow operation.

## It does not take advantage of the vectorization that speeds up operations.

## It is generally used when labelling plots.

url = 'https://github.com/mattharrison/datasets/raw/master/data/siena2018-pres.csv'

df = pd.read_csv(url, index_col=0)

def shiv_parvati(df):
    def int64_to_uint8(df_):
        cols = df_.select_dtypes('int64')
        return (df_
                .astype({col:'uint8' for col in cols}))
    return (df
     .rename(columns={'Seq.':'Seq'})    # 1
     .rename(columns={k:v.replace(' ', '_') for k,v in
        {'Bg': 'Background',
         'PL': 'Party leadership', 'CAb': 'Communication ability',
         'RC': 'Relations with Congress', 'CAp': 'Court appointments',
         'HE': 'Handling of economy', 'L': 'Luck',
         'AC': 'Ability to compromise', 'WR': 'Willing to take risks',
         'EAp': 'Executive appointments', 'OA': 'Overall ability',
         'Im': 'Imagination', 'DA': 'Domestic accomplishments',
         'Int': 'Integrity', 'EAb': 'Executive ability',
         'FPA': 'Foreign policy accomplishments',
         'LA': 'Leadership ability',
         'IQ': 'Intelligence', 'AM': 'Avoid crucial mistakes',
         'EV': "Experts' view", 'O': 'Overall'}.items()})
     .astype({'Party':'category'})  # 2
     .pipe(int64_to_uint8)  # 3
     .assign(Average_rank=lambda df_:(df_.select_dtypes('uint8') # 4
                 .sum(axis=1).rank(method='dense').astype('uint8')),
             Quartile=lambda df_:pd.qcut(df_.Average_rank, 4,
                 labels='1st 2nd 3rd 4th'.split())
            )
    )

om = shiv_parvati(df)


#! Iteration over columns(col_name, series) tuple


# for col_name, col in om.items():
#     print(col_name, type(col))
#     break

#~ Seq <class 'pandas.core.series.Series'>


#! Iteration over rows(index, row(as a series)) tuple

# for idx, row in om.items():
#     print(idx, type(row))
#     break

#~ Seq <class 'pandas.core.series.Series'>

#! Iteration over rows as namedtuple(index as first item)

# for tup in om.itertuples():
#     print(tup[0], tup.Party)
#     break
 
 
 #! Aggregations (the sum)
 
scores = om.loc[ :,'Background':'Average_rank']

# scores.sum(axis='columns')/len(scores.columns)

## OR

# scores.mean(axis=1)

scores.agg(['count', 'size', 'sum', lambda col:col.loc[1]])


om.agg({'Luck':['count', 'size'], 'Overall':['count','max']})

#~ 
#~ Luck	Overall
#~ count	44.0	44
#~ size	44.0	NaN
#~ max	NaN	44

om.agg(Intelligence_count=('Intelligence', 'count'), Intelligence_size =('Intelligence', 'size'))


#~ Intelligence
#~ Intelligence_count	44
#~ Intelligence_size	44

#! The .describe() method is a mega-aggregation that returns a dataframe with summary statistics for each numeric columns:

om.describe()

## The describe method provides the count of non-missing values, the mean, standard deviation, minimum, maximum and quartiles.


#! Apply method()

#^ Apply method is recommended to be used only when one is dealing with non numbers.

# om.select_dtypes('number').pipe(lambda df_:df_.max(axis='columns')-df_.min(axis='columns'))

#~ 1     17
#~ 2     28
#~ 3     19
#~ 4     16
#~ 5     13
#~ 6     28
#~ 7     34
#~ 8     18
#~ 9     22
#~ 10    19

#~ 597 µs ± 1.14 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

#~ This method does an optimized max and min calculations.



# %timeit om.select_dtypes('number').apply(lambda row:row.max()-row.min(),axis='columns')

#~ 1     17
#~ 2     28
#~ 3     19
#~ 4     16
#~ 5     13
#~ 6     28
#~ 7     34
#~ 8     18
#~ 9     22
#~ 10    19

#~ 1.97 ms ± 139 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

#~ This method does separate calculations for each row


# %timeit om.select_dtypes('number').apply('sum')

#~ Background                        968
#~ Imagination                       957
#~ Integrity                         990
#~ Intelligence                      990
#~ Luck                              990
#~ Willing_to_take_risks             953
#~ Ability_to_compromise             968
#~ Executive_ability                 978
#~ Leadership_ability                990
#~ Communication_ability             990
#~ Overall_ability                   990
#~ Party_leadership                  990
#~ Relations_with_Congress           979
#~ Court_appointments                990
#~ Handling_of_economy               990
#~ Executive_appointments            990
#~ Domestic_accomplishments          990
#~ Foreign_policy_accomplishments    990
#~ Avoid_crucial_mistakes            990
#~ Experts'_view                     990
#~ Overall                           990
#~ Average_rank                      990
#~ dtype: uint64

#~ 307 µs ± 9.73 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)


#%timeit om.select_dtypes('number').sum()

#~ Background                        968
#~ Imagination                       957
#~ Integrity                         990
#~ Intelligence                      990
#~ Luck                              990
#~ Willing_to_take_risks             953
#~ Ability_to_compromise             968
#~ Executive_ability                 978
#~ Leadership_ability                990
#~ Communication_ability             990
#~ Overall_ability                   990
#~ Party_leadership                  990
#~ Relations_with_Congress           979
#~ Court_appointments                990
#~ Handling_of_economy               990
#~ Executive_appointments            990
#~ Domestic_accomplishments          990
#~ Foreign_policy_accomplishments    990
#~ Avoid_crucial_mistakes            990
#~ Experts'_view                     990
#~ Overall                           990
#~ Average_rank                      990
#~ dtype: uint64

#~ 248 µs ± 852 ns per loop (mean ± std. dev. of 7 runs, 1,000 loops each)