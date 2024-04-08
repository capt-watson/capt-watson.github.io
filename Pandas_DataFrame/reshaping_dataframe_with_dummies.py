import pandas as pd
import numpy as np
pd.set_option('future.no_silent_downcasting', True)

url = 'https://github.com/mattharrison/datasets/raw/master/data/2020-jetbrains-python-survey.csv'

jb = pd.read_csv(url)

## Following codes will filter out those columns having strings specified by 'like=' in their names.
# jb.filter(like ='job.role')

## In the following codes, .idxmax() method will scan along given axis and report the index (or column) where the max value is found.

# jb.filter(like=r'job.role')\
#   .where(jb.isna(), 1)\
#   .fillna(0)\
#   .idxmax(axis='columns')

## Finally, we remove the 'job.role':

##  By default, regex=True, which means that the pattern will be treated as a regular expression. If regex=False, the pattern will be treated as a literal string.

job = jb.filter(like=r'job.role').where(jb.isna(), 1).fillna(0).idxmax(axis='columns')\
        .str.replace('job.role.', ' ', regex=False)
        
job


dum = pd.get_dummies(job)

dum

#^ Undoing dummy columns

dum.idxmax(axis='columns')

## Another faster way to undo dummy columns

i, j = np.where(dum)

pd.Series(dum.columns[j], i)
