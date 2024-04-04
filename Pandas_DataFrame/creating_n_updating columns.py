import pandas as pd
import numpy as np
import collections
import catboost as cb


pd.set_option("future.no_silent_downcasting", True)


url = 'https://github.com/mattharrison/datasets/raw/master/data/2020-jetbrains-python-survey.csv'

jb = pd.read_csv(url,low_memory=False)

counter = collections.defaultdict(list)  ## creates an empty list []
for col in sorted(jb.columns):
        period_count = col.count('.')       ## counts the number of dots '.' in each list
        if period_count >= 2:
            part_end= 2                     ## if list has 2 dots or more, mark 2
        else:
            part_end = 1                    ## if list has 1 dots or less, mark 1
        parts = col.split('.')[:part_end]   ## split the list from dot (.) but include values except after last dot.
        counter['.'.join(parts)].append(col)
uniq_cols = []            ## Creates an empty list []
for cols in counter.values():   ## Runs for loop on retrieved counter values of dict.
    if len(cols) == 1:
        uniq_cols.extend(cols)  ## Will keep appending cols with only one key:value pair to the unique_cols list
uniq_cols


# ~ ['age',
# ~  'are.you.datascientist',
# ~  'company.size',
# ~  'country.live',
# ~  'employment.status',
# ~  'first.learn.about.main.ide',
# ~  'how.often.use.main.ide',
# ~  'ide.main',
# ~  'is.python.main',
# ~  'job.team',
# ~  'main.purposes',
# ~  'missing.features.main.ide',
# ~  'nps.main.ide',
# ~  'python.years',
# ~  'python2.version.most',
# ~  'python3.version.most',
# ~  'several.projects',
# ~  'team.size',
# ~  'use.python.most',
# ~  'years.of.coding']

jb[uniq_cols].rename(columns=lambda c:c.replace('.','_')).age.value_counts(dropna=False)  ## running lambda func on cols to replace '.' by '_'.

# ~ age
# ~ NaN            29701
# ~ 21–29           9710
# ~ 30–39           7512
# ~ 40–49           3010
# ~ 18–20           2567
# ~ 50–59           1374
# ~ 60 or older      588
# ~ Name: count, dtype: int64

jb[uniq_cols].rename(columns=lambda c:c.replace('.','_')).age.str.slice(0,2).astype('Int64')

# ~ 0          30
# ~ 1          21
# ~ 2          30
# ~ 3        <NA>
# ~ 4          21
# ~          ...
# ~ 54457      21
# ~ 54458    <NA>
# ~ 54459      21
# ~ 54460      30
# ~ 54461      21
# ~ Name: age, Length: 54462, dtype: Int64

# ^ Int64 is a dtype that stores integers that may or may not be present.


jb[uniq_cols].rename(columns=lambda c:c.replace('.','_')).assign(age=lambda df_:df_.age.str[0:2].astype('Int64'))


jb[uniq_cols].rename(columns=lambda c:c.replace('.','_')).assign(age=lambda df_:df_.age.str[0:2].astype('Int64'),are_you_datascientist = lambda df_:df_.are_you_datascientist.replace({'Yes':True, 'No':False,np.nan:False})).are_you_datascientist

# ~ 0        False
# ~ 1         True
# ~ 2        False
# ~ 3        False
# ~ 4        False
# ~          ...
# ~ 54457    False
# ~ 54458    False
# ~ 54459    False
# ~ 54460     True
# ~ 54461    False
# ~ Name: are_you_datascientist, Length: 54462, dtype: object


jb[uniq_cols].rename(columns=lambda c:c.replace('.','_')).assign(age=lambda df_:df_.age.str[0:2].astype('Int64'),are_you_datascientist = lambda df_:df_.are_you_datascientist.replace({'Yes':True,'No':False,np.nan:False})).company_size.value_counts(dropna=False)

# ~ company_size
# ~ NaN                35037
# ~ 51–500              4608
# ~ More than 5,000     3635
# ~ 11–50               3507
# ~ 2–10                2558
# ~ 1,001–5,000         1934
# ~ Just me             1492
# ~ 501–1,000           1165
# ~ Not sure             526
# ~ Name: count, dtype: int64


jb2 = jb[uniq_cols].rename(columns=lambda c: c.replace('.','_')).assign(age=lambda df_:df_.age.str.slice(0,2).astype('Int64'),are_you_datascientist = lambda df_:df_.are_you_datascientist.replace({'Yes':True,'No':False,np.nan:False}), company_size= lambda df_:df_.company_size.replace({'Just me':1, 'Not sure': np.nan, 'More than 5,000': 5000, '2–10' : 2, '11–50': 11, '51–500': 51,'501–1,000': 501,  '1,001–5,000': 1001}).astype('Int64'),country_live = lambda df_:df_.country_live.astype('category'),employment_status = lambda df_:df_.employment_status.fillna('Other').astype('category'),is_python_main = lambda df_:df_.is_python_main.astype('category'),team_size = lambda df_:df_.team_size.str.split(r'-',n=1, expand=True).iloc[:,0].replace('More than 40 people',41).where(df_.company_size != 1, 1).astype(float),years_of_coding = lambda df_:df_.years_of_coding.replace('Less than 1 year', .5).str.extract(r'(\d+)').astype(float), python_years = lambda df_:df_.python_years.replace('_','.').str.extract(r'(\d+)').astype(float), use_python_most = lambda df_:df_.use_python_most.fillna('Unknown')).drop(columns=['python2_version_most'])

jb2.query('team_size.isna()').employment_status.value_counts(dropna=False)

# ~ employment_status
# ~ Fully employed by a company / organization                                                        5279
# ~ Working student                                                                                    696
# ~ Partially employed by a company / organization                                                     482
# ~ Self-employed (a person earning income directly from one's own business, trade, or profession)     430
# ~ Freelancer (a person pursuing a profession without a long-term commitment to any one employer)       0
# ~ Other                                                                                                0
# ~ Retired                                                                                              0
# ~ Student                                                                                              0
# ~ Name: count, dtype: int64

# def prep_for_ml(df):        ## prepare for machine learning model
# ## Remove pandas types)
#     return (df.assign(**{col:df[col].astype(float) for col in df.select_dtypes('number')},
#               **{col:df[col].astype(str).fillna('') for col in df.select_dtypes(['object','category'])}))

# def predict_col(df,col):
#     df = prep_for_ml(df)
#     missing = df.query(f'~{col}.isna()')
#     cat_idx = [i for i, typ in enumerate(df.drop(columns = [col]).dtypes) if str(typ) == 'object']

#     X = (missing.drop(columns = [col]).values)

#     y = missing[col]

#     model = cb.CatBoostRegressor(iterations=20, cat_features=cat_idx)
#     model.fit(X,y,cat_features=cat_idx)
#     pred = model.predict(df.drop(columns = [col]))
#     return df[col].where(~df[col].isna(), pred)

# jb2 = jb[uniq_cols].rename(columns=lambda c: c.replace('.','_')).assign(
#     age=lambda df_:df_.age.str.slice(0,2).astype('Int64'),
#     are_you_datascientist = lambda df_ : df_.are_you_datascientist
#     .replace({'Yes':True, 'No':False, np.nan: False}),
#     company_size =lambda df_ : df_.company_size
#     .replace({'Just me': 1, 'Not sure': np.nan,
#                'More than 5,000': 5000, '2–10':2, '11–50': 11,
#                '51–500': 51, '501–1,000': 501, '1,001–5,000':1001}).astype('Int64'),
#     country_live = lambda df_ : df_.country_live.astype('category'),
#     employment_status = lambda df_ : df_.employment_status.fillna('Other').astype('category'),
#     is_python_main = lambda df_ : df_.is_python_main.astype('category'),
#     team_size = lambda df_ : df_.team_size.str.split(r'-', n=1, expand=True)
#     .iloc[:,0].replace('More than 40 people', 41).where(df_.company_size !=1, 1).astype(float),
#     years_of_coding = lambda df_ : df_.years_of_coding.replace('Less than 1 year', .5)
#     .str.extract(r'(\d+)').astype(float),
#     python_years = lambda df_ : df_.python_years.replace('Less than 1 year', .5)
#     .str.extract(r'(\d+)').astype(float),
#     python3_ver = lambda df_ : df_.python3_version_most.str
#     .replace('_', '.').str.extract(r'(\d\.\d)').astype(float),
#     use_python_most = lambda df_ : df_.use_python_most.fillna('unknown')
#     ).assign(team_size = lambda df_ : predict_col(df_,'team_size').astype('int')).drop(columns = ['python2_version_most']).dropna()

# jb2


# # #^ Creating a snippet for DataFrame cleaning

url = "https://github.com/mattharrison/datasets/raw/master/data/2020-jetbrains-python-survey.csv"

jb = pd.read_csv(url)

def get_uniq_cols(jb):
    ## Create a defaultdict with a list as the default value
    counter = collections.defaultdict(list)
    for col in sorted(jb.columns):
        ## count numbers of periods in the column names
        period_count = col.count('.')
        if period_count >= 2:
            part_end = 2
        else:
            part_end = 1
        ## split col names from one period to another
        parts = col.split('.')[:part_end]
        ## join the split parts together as col names as keyword arguments and append col part_end values as its values.
        counter['.'.join(parts)].append(col)
    ## create an empty list    
    uniq_cols = []
    for cols in counter.values():
        if len(cols) == 1:
            ##  ## The col.extend(col) method in pandas extends the col column with the values of the col column. This means that the resulting column will contain all of the values from the original column, plus any additional values that were passed to the extend() method.
            uniq_cols.extend(cols)
    return uniq_cols


def prep_for_ml(df):
    ## convert datatypes of columns of numbers dtype to floats dtype
    ## convert dtypes of columns of object and category dtype to strings dtype
    ## In assign method, the column names are keywords.
    #! assign returns a new object with all original columns in addition to new ones. Existing columns that are re-assigned will be overwritten.
    return df.assign(
        **{col:df[col].astype(float) for col in df.select_dtypes("number")},
        **{col:df[col].astype(str).fillna('') for col in df.select_dtypes(["object","category"])},)


def predict_col(df, col):
    df = prep_for_ml(df)
    ## find all columns with not any missing values
    missing = df.query(f"~{col}.isna()")
    cat_idx = []
    ## for type in datatypes of cols
    for i, typ in enumerate(df.drop(columns=[col]).dtypes):
        if str(typ) == "object":
            cat_idx.append(i)
            ## drop all columns without any missing values, leaving only columns with missing values
    X = missing.drop(columns=[col]).values
            ## columns without any missing values.
            ## X represents train data
    y = missing[col]
            ## y represents train label
    model = cb.CatBoostRegressor(iterations=20, cat_features= cat_idx)
            ## cat_features represents a one-dimensional array of categorical columns indices (specified as integers) or names (specified as strings). It represents column names
    model.fit(X, y,cat_features=cat_idx)
    pred = model.predict(df.drop(columns=[col]))
    return df[col].where(~df[col].isna(), pred)


def tweak_jb(jb):
    uniq_cols = get_uniq_cols(jb)
    return (
        jb[uniq_cols]
        .rename(columns = lambda c : c.replace('.','_'))
        .assign(
            age=lambda df_:df_.age.str.slice(0,2).astype('Int64'),
            are_you_datascientist = lambda df_:df_
                .are_you_datascientist
                .replace({'Yes': True, 'No': False, np.nan: False}),
            company_size=lambda df_:df_.company_size
                .replace({
                    'Just me': 1,
                    'Not sure': np.nan,
                    'More than 5,000': 5000,
                    '2–10': 2,'11–50':11,
                    '51–500': 51,
                    '501–1,000': 501,
                    '1,001–5,000': 1001})
                .astype('Int64'),
            country_live = lambda df_:df_.country_live
                .astype('category'),
            employment_status = lambda df_: df_.employment_status
                .fillna('Other')
                .astype('category'),
            is_python_main = lambda df_:df_.is_python_main
                .astype('category'),
            team_size = lambda df_:df_.team_size
                .str.split(r'-',n=1, expand=True)
                .iloc[:,0]
                .replace('More than 40 people',41)
                .where(df_.company_size != 1, 1)
                .astype(float),
            years_of_coding = lambda df_:df_.years_of_coding
                .replace('Less than 1 year', .5)
                .str
                .extract(r'(\d+)')
                .astype(float),
            python_years = lambda df_: df_.python_years
                .replace('Less than 1 year', .5)
                .str
                .extract(r'(\d+)')
                .astype(float),
            python3_ver = lambda df_: df_.python3_version_most
                .str
                .replace('_', '.')
                .str
                .extract(r'(\d\.\d)')
                .astype(float),
            use_python_most = lambda df_: df_.use_python_most
                .fillna('Unknown'))
        .assign(team_size = lambda df_: predict_col(df_, 'team_size').astype(int))
        .drop(columns=['python2_version_most'])
        .dropna())
    


jb2 = tweak_jb(jb)

#~ Learning rate set to 0.5
#~ 0:	learn: 2.9695218	total: 28.9ms	remaining: 550ms
#~ 1:	learn: 2.8766539	total: 57.8ms	remaining: 521ms
#~ 2:	learn: 2.8387189	total: 88.6ms	remaining: 502ms
#~ 3:	learn: 2.8028751	total: 118ms	remaining: 470ms
#~ 4:	learn: 2.7899957	total: 146ms	remaining: 439ms
#~ 5:	learn: 2.7749439	total: 178ms	remaining: 415ms
#~ 6:	learn: 2.7719128	total: 210ms	remaining: 389ms
#~ 7:	learn: 2.7649792	total: 246ms	remaining: 369ms
#~ 8:	learn: 2.7649588	total: 273ms	remaining: 333ms
#~ 9:	learn: 2.7630617	total: 305ms	remaining: 305ms
#~ 10:	learn: 2.7625779	total: 337ms	remaining: 276ms
#~ 11:	learn: 2.7515902	total: 366ms	remaining: 244ms
#~ 12:	learn: 2.7513459	total: 397ms	remaining: 214ms
#~ 13:	learn: 2.7445634	total: 425ms	remaining: 182ms
#~ 14:	learn: 2.7443257	total: 462ms	remaining: 154ms
#~ 15:	learn: 2.7423142	total: 491ms	remaining: 123ms
#~ 16:	learn: 2.7419144	total: 523ms	remaining: 92.3ms
#~ 17:	learn: 2.7399388	total: 553ms	remaining: 61.4ms
#~ 18:	learn: 2.7384297	total: 586ms	remaining: 30.8ms
#~ 19:	learn: 2.7383591	total: 614ms	remaining: 0us
