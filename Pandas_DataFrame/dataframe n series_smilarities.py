import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


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

fig, ax = plt.subplots(figsize=(10,10), dpi=600)
g = sns.heatmap((shiv_parvati(df)     # doctest: +SKIP
   .set_index('President')
   .iloc[:,2:-1]),annot=True, cmap='viridis', ax=ax)
g.set_xticklabels(g.get_xticklabels(), rotation=45, fontsize=8,
    ha='right')    # doctest: +SKIP
_ = plt.title('Presidential Ranking')

pres = shiv_parvati(df)

#! Annot − The sns. heatmap() annot (annotation) feature allows you to show the numerical value associated with each cell in a python seaborn heatmap.

#! In Seaborn, the letter "g" is often used to refer to a FacetGrid object. FacetGrid object is a grid of subplots that is used to visualize data that is grouped by one or more categorical variables. 

#! cmap : Specifies the colormap for the heatmap.

# #* qcut means quantile cut    
# ## Following code includes or excludes given dtypes from the dataFrame
# #^ dataframe.select_dtypes(include, exclude)



# url = 'https://en.wikipedia.org/wiki/Historical_rankings_of_presidents_of_the_United_States'

# dfs = pd.read_html(url)

# df =dfs[7]

# def shiv_parvati(df):
#     def int64_to_uint8(df_):
#         cols = df_.select_dtypes('int64')
#         return (df_
#                 .astype({col:'uint8' for col in cols}))
#     return (df
#      .rename(columns={'Political party':'Party'})
#      .rename(columns={'Seq.':'Seq'})    # 1
#      .rename(columns={k:v.replace(' ', '_') for k,v in
#         {'Bg': 'Background',
#          'PL': 'Party leadership', 'CAb': 'Communication ability',
#          'RC': 'Relations with Congress', 'CAp': 'Court appointments',
#          'HE': 'Handling of economy', 'L': 'Luck',
#          'AC': 'Ability to compromise', 'WR': 'Willing to take risks',
#          'EAp': 'Executive appointments', 'OA': 'Overall ability',
#          'Im': 'Imagination', 'DA': 'Domestic accomplishments',
#          'Int': 'Integrity', 'EAb': 'Executive ability',
#          'FPA': 'Foreign policy accomplishments',
#          'LA': 'Leadership ability',
#          'IQ': 'Intelligence', 'AM': 'Avoid crucial mistakes',
#          'EV': "Experts' view", 'O': 'Overall'}.items()})
#      .astype({'Party':'category'})  # 2
#      .pipe(int64_to_uint8)  # 3
#      .assign(Average_rank=lambda df_:(df_.select_dtypes('uint8') # 4
#                  .sum(axis=1).rank(method='dense').astype('uint8')),
#              Quartile=lambda df_:pd.qcut(df_.Average_rank, 4,
#                  labels='1st 2nd 3rd 4th'.split())
#             )
#     )

# # # df1 = df['background'].replace('22 (tie)','22')

# pres = shiv_parvati(df)

