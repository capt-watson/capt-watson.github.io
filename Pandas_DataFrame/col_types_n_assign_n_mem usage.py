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


om.memory_usage(deep=True)

# #^ Here one can see that the ranking columns use least memory as they are stored as uint8 values instead of int64.

om.info(memory_usage='deep')

#~ <class 'pandas.core.frame.DataFrame'>
#~ Index: 44 entries, 1 to 44
#~ Data columns (total 26 columns):
#~  #   Column                          Non-Null Count  Dtype   
#~ ---  ------                          --------------  -----   
#~  0   Seq                             44 non-null     object  
#~  1   President                       44 non-null     object  
#~  2   Party                           44 non-null     category
#~  3   Background                      44 non-null     uint8   
#~  4   Imagination                     44 non-null     uint8   
#~  5   Integrity                       44 non-null     uint8   
#~  6   Intelligence                    44 non-null     uint8   
#~  7   Luck                            44 non-null     uint8   
#~  8   Willing_to_take_risks           44 non-null     uint8   
#~  9   Ability_to_compromise           44 non-null     uint8   
#~  10  Executive_ability               44 non-null     uint8   
#~  11  Leadership_ability              44 non-null     uint8   
#~  12  Communication_ability           44 non-null     uint8   
#~  13  Overall_ability                 44 non-null     uint8   
#~  14  Party_leadership                44 non-null     uint8   
#~  15  Relations_with_Congress         44 non-null     uint8   
#~  16  Court_appointments              44 non-null     uint8   
#~  17  Handling_of_economy             44 non-null     uint8   
#~  18  Executive_appointments          44 non-null     uint8   
#~  19  Domestic_accomplishments        44 non-null     uint8   
#~  20  Foreign_policy_accomplishments  44 non-null     uint8   
#~  21  Avoid_crucial_mistakes          44 non-null     uint8   
#~  22  Experts'_view                   44 non-null     uint8   
#~  23  Overall                         44 non-null     uint8   
#~  24  Average_rank                    44 non-null     uint8   
#~  25  Quartile                        44 non-null     category
#~ dtypes: category(2), object(2), uint8(22)
#~ memory usage: 7.2 KB

## We should the datatype only when the values in the df are numerals (between 0 and 255) and their current datatype is int64.