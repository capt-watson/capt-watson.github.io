import pandas as pd
import numpy as np

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

#!Index alignment

scores = om.loc[:,'Background':'Average_rank']

s1 = scores.iloc[:3, :4]

s2 = scores.iloc[1:6, :5]

s1 + s2


#! Duplicate Index Entries

#^ Creating a dataFrame with duplicated values, created by concatenating the dataFrame itself.

scores.iloc[:3, :4] + pd.concat([scores.iloc[1:6, :5]*2])


#~ Background	Imagination	Integrity	Intelligence	Luck
#~ 1	NaN	NaN	NaN	NaN	NaN
#~ 2	9.0	39.0	12.0	12.0	NaN
#~ 3	6.0	6.0	42.0	3.0	NaN
#~ 4	NaN	NaN	NaN	NaN	NaN
#~ 5	NaN	NaN	NaN	NaN	NaN
#~ 6	NaN	NaN	NaN	NaN	NaN


# pd.concat([scores.iloc[1:6, :5]]*2).index.duplicated().any()
#~ True


#! Examples for Practice

s = pd.DataFrame([(0.0, np.nan, -2.0, 2.0), (np.nan, 2.0, np.nan, 1), (2.0, 5.0, np.nan, 9.0), (np.nan, 4.0, -3.0, 16.0)], columns=list('abcd'))

#@ Checking for NaN values

s.isnull()

#@ Replacing NaN values

s.fillna(0)

#@ Alternatively, you can also mention the values column-wise. That means all the NaNs under one column will be replaced with the same value.

values = {'a': 0, 'b': 1, 'c': 2, 'd': 3}

s.fillna(value=values)


#@ Drop rows containing NaN values

#^ To drop rows with NaNs use:

s.dropna()

#@ Drop columns containing NaN values

s.dropna(axis='columns')

s.add(5,axis='columns')

s.sub(2,axis='columns')

s.mul(5, axis='columns')

s.div(2, axis='columns')

s.floordiv(2, axis='columns')

s.pow(2, axis='columns')

