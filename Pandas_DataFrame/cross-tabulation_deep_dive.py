import pandas as pd
from tweak_jb import tweak_jb
pd.set_option('future.no_silent_downcasting', True)

url = 'https://github.com/mattharrison/datasets/raw/master/data/2020-jetbrains-python-survey.csv'

jb = pd.read_csv(url, dtype='unicode')

jb2 = tweak_jb(jb)

pd.crosstab(index=jb2.country_live, columns=jb2.age)

#^ Adding Margins

## margins = True will put the sums of rows and columns at their respective ends.
pd.crosstab(index=jb2.country_live, columns=jb2.age, margins= True)

#^ Normalizing results

## To calculate the percentage of each cell, use normalize = True. Normalize by dividing all values by the sum of values. True, will normalize over all values.  ‘index’ will normalize over each row to sum up to 1. ‘columns’ will normalize over each column to sum up to 1.0. margins is True, will also normalize margin values.

pd.crosstab(index=jb2.country_live, columns=jb2.age, normalize=True)

pd.crosstab(index= jb2.country_live, columns=jb2.age, normalize= 'columns')

pd.crosstab(index=jb2.country_live, columns=jb2.age, normalize='index')

#^ Hierarchical columns with Cross Tabulations.

pd.crosstab(index=[jb2.country_live, jb2.age], columns=[jb2.use_python_most, jb2.python3_version_most]).loc[['United States']]

## following codes will pull out only United states for index and Data analysis & Web development as columns.

pd.crosstab(index=[jb2.country_live, jb2.age], columns=[jb2.use_python_most, jb2.python3_version_most]).loc[['United States'], ['Data analysis', 'Web development']]

#^ Heatmaps

pd.crosstab(index=[jb2.country_live, jb2.age], columns=[jb2.use_python_most, jb2.python3_version_most]).loc[['United States'], ['Data analysis', 'Web development']].style.background_gradient(cmap='viridis', axis=None)
            
## The above heatmap shows that the Python 3.8 is the most popular and popular age is 30    