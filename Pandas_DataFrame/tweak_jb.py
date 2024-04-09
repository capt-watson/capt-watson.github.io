import numpy as np
import collections
import catboost as cb


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
        ## split col names at '.' and return first 2 values if part_end = 2 else return first value. This restricts column name to max of two words. This word will become 'keys'
        parts = col.split('.')[:part_end]
        # ## join the split parts together as col names as keyword arguments and append all the values given in the list as its values.
        counter['.'.join(parts)].append(col)
    ## create an empty list    
    uniq_cols = []
    for cols in counter.values():
        if len(cols) == 1:
            ## Select only those columns that has only one value list and add their list values to the uniq_cols list.
            uniq_cols.extend(cols)
            ## The extend() method adds the specified list elements (or any iterable) to the end of the current list.
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
    ## following code will take string as its arguments and return all rows of df where column col is not null.
    missing = df.query(f"~{col}.isna()")
    cat_idx = []
    ## for dtype(typ) in datatypes of cols. The i variable will store the index of the current dtype, and the typ variable will store the dtype itself.
    for i, typ in enumerate(df.drop(columns=[col]).dtypes):
        if str(typ) == "object":
            cat_idx.append(i)
            ## drop all columns without any missing values, leaving only columns with missing values
    X = missing.drop(columns=[col]).values
            ## columns without any missing values. X represents train data
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
    
jb2 = tweak_jb()