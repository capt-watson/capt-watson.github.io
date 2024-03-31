import numpy as np
import pandas as pd

df = {'index':[0,1,2],'cols':[{'name':'growth', 'data':[.5, .7, 1.2]}, {'name':'Name', 'data':['Paul', 'George', 'Ringo']},]}

def get_row(df, idx):
    results = []
    value_idx = df['index'].index(idx)
    for col in df['cols']:
        results.append(col['data'][value_idx])
    return results

get_row(df,1)

def get_col(df, name):
    for col in df['cols']:
        if col['name'] == name:
            return col['data']
        
get_col(df,'Name')


#! DataFrames creation from column - (dict of lists)

df = pd.DataFrame({'growth':[.5, .7, 1.2], 'Name':['Paul', 'George', 'Ringo']})

#~ 	growth	Name
#~ 0	0.5	Paul
#~ 1	0.7	George
#~ 2	1.2	Ringo

#% Accessing row

df.iloc[2]

#~ growth      1.2
#~ Name      Ringo
#~ Name: 2, dtype: object

#% Accessing columns

df['Name']

#~ 0      Paul
#~ 1    George
#~ 2     Ringo
#~ Name: Name, dtype: object

df.Name     ## dataFrame column can also be accessed this way df.<column name>

#~ 0      Paul
#~ 1    George
#~ 2     Ringo
#~ Name: Name, dtype: object

#! DataFrame creation from rows (list of dicts)

pd.DataFrame([{'growth':.5, 'Name':'Paul'}, {'growth':.7, 'Name':'George'}, {'growth':1.2, 'Name':'Ringo'}])


#~ growth	Name
#~ 0	0.5	Paul
#~ 1	0.7	George
#~ 2	1.2	Ringo

#! DataFrame creation from a CSV File

#^ csv_file = StringIO<File url here>

#^ pd.read_csv(csv_file)  pd.read_csv will down load the file. If the extension ends in .xz, .bzz2, or .zip, it will decompress the file automatically

#! DataFrame creation from NumPy array as well

np.random.seed(42)
pd.DataFrame(np.random.randn(5,3),columns= ['a', 'b', 'c'])

#~ a	b	c
#~ 0	0.496714	-0.138264	0.647689
#~ 1	1.523030	-0.234153	-0.234137
#~ 2	1.579213	0.767435	-0.469474
#~ 3	0.542560	-0.463418	-0.465730
#~ 4	0.241962	-1.913280	-1.724918
#~ 5	-0.562288	-1.012831	0.314247
#~ 6	-0.908024	-1.412304	1.465649
#~ 7	-0.225776	0.067528	-1.424748
#~ 8	-0.544383	0.110923	-1.150994
#~ 9	0.375698	-0.600639	-0.291694

#! DataFrame Axis

#@ axis 0 or index (or rows) axis
#@ axis 1 or columns axis


df.sum(axis=0)

#~ growth                2.4
#~ Name      PaulGeorgeRingo
#~ dtype: object

# df.axes

df.sum(axis=1, numeric_only=True)

#~ 0    0.5
#~ 1    0.7
#~ 2    1.2
#~ dtype: float64


df.sum(axis='index')

#~ growth                2.4
#~ Name      PaulGeorgeRingo
#~ dtype: object


df.sum(axis='columns',numeric_only=True)

#~ 0    0.5
#~ 1    0.7
#~ 2    1.2
#~ dtype: float64


df.axes[0]

#~ RangeIndex(start=0, stop=3, step=1)

df.axes[1]

#~ Index(['growth', 'Name'], dtype='object')


df = pd.DataFrame({'Score1': [None, None], 'Score2': [85,90]})

df.apply(np.sum, axis=0)        ## Will give total column wise


df.apply(np.sum, axis=1)        ## will give total column wise


