import pandas as pd
import matplotlib.pyplot as plt
from shiv_parvati import shiv_parvati

url= 'https://github.com/mattharrison/datasets/raw/master/data/siena2018-pres.csv'

df = pd.read_csv(url, index_col=0)

pres =shiv_parvati(df)

## Pandas will plot the index in the X-Axis and each column will be its own line.Here X-Axis is the presidents (from first to last). Each line represents what happens to the score from President to President.

#! .legend(bbox_to_anchor=(1,1)) means to start the graph legends from coordinate (1,1) outside the plot box.The coordinates are specified as a tuple of four values: (x, y, width, height). The x and y values specify the lower-left corner of the legend, and the width and height values specify the size of the legend.By default, the coordinates are in the range [0, 1], where (0, 0) is the lower-left corner of the plot and (1, 1) is the upper-right corner.

# pres.plot().legend(bbox_to_anchor= (1,1))

## following operation will pull out every second row starting from beginning to end and columns from 'background to Overall. The letter 'T' will transpose column name from Y axis to X axis and vice versa.

# pres.set_index('President').loc[::2,'Background':'Overall'].T.plot().legend(bbox_to_anchor=(1,1))

## # Create a figure and axes object with a dpi of 600 and a figsize of (10, 4)
# fig, ax = plt.subplots(dpi=600, figsize= (10,4))

# pres.set_index('President').loc[::2,'Background':'Overall'].T.plot(ax=ax, rot=45).legend(bbox_to_anchor=(1,1))

# ## following operation will create a plot with 21 ticks on the X-axis (ranging from 0 to 20). These ticks will be evenly spaced along the X-axis.
# ax.set_xticks(range(21))

# ## Will set x-axis labels at the tick position set by above code. ha has 3 options. Center, left and right. This indicates the starting position of the label with respect to its tick marks. Center is the default.
# ax.set_xticklabels(pres.loc[:, 'Background':'Overall'], ha= 'right')

# ## Following code labels 'Rank' to the Y-axis.

# ax.set_ylabel('Rank')

# fig, ax = plt.subplots(dpi=600, figsize=(10, 4))

# colors = []


# def set_colors(df):
#     for col in df.columns:
#         if "George" in col:
#             colors.append("#990000")
#         else:
#             colors.append("#999999")
#     return df


# ##.pipe() method allows you to apply one or more functions to the dataframe.
# pres.set_index("President") \
#     .loc[::2, "Background":"Overall"]\
#     .T.pipe(set_colors) \
#     .plot(ax=ax, rot=45, color=colors) \
#     .legend(bbox_to_anchor=(1, 1))

# ax.set_xticks(range(21))

# ax.set_xticklabels(pres.loc[:, "Background":"Overall"].columns, ha="right")

# ax.set_ylabel("Rank")


#^ Bar Plots



# pres.set_index('President') \
#     .iloc[:,-5:] \
#     .plot.barh(figsize= (4,12)) \
#     .legend(bbox_to_anchor=(1,1))  ## For horizontal plot, rot param removed.


#^ Scatter Plots

## A scatter plot is useful to determine the relationship between two columns that are numeric.

## 'c' represents the column name whose values will be used to color the marker points according to colormap.

## 'cmap' represents the colormap name 'viridis'. For more colormap, refer matplotlib document page bookmark.

# pres.plot.scatter(x='Integrity', y='Avoid_crucial_mistakes',\
#     c = 'Luck', cmap = 'viridis')

## Following colormap shows the relationship between two continuous values as well as density as a Hexbin plot. Here colormap is continuous and increasing from white to dark for this plot.

# pres.plot.scatter(x='Integrity', y='Avoid_crucial_mistakes',\
#     c= 'Luck', cmap = 'Greens')

#^ Area Plots and Stacked Bar Plots

## A stacked area plot is useful where one wants to understand each columns relative contribution and the order of the data is important. 

## If there is no relationship and order between the values, stacked bar plot is preferred.

# pres.plot.area(x= 'President',\
#     y= 'Background Imagination Integrity Intelligence Luck ' \
#        'Willing_to_take_risks Ability_to_compromise'.split(), rot=45)

# ax.set_xticks(range(len(pres)))

# ax.set_xticklabels(labels=pres.President, ha = 'right')

# pres.plot.bar(x = 'President', y= 'Background Imagination Integrity Intelligence Luck '\
#     'Willing_to_take_risks Ability_to_compromise'.split(), rot=45, stacked= True)  

# ax.set_xticks(range(len(pres)))
# ax.set_xticklabels(labels=pres.President, ha = 'right')

#^ Column Distribution with KDEs, Histograms and Boxplots

## Will print 22 rows and 9 columns
# pres.set_index('President').loc[:,'Background':'Average_rank'].iloc[:9].T


## The .describe() method summarizes each column, in this case the scores for each president.

# pres.set_index('President').loc[:, 'Background':'Average_rank'].iloc[:9].T.describe()



## Each president's scores with a Kernel Density Estimation (KDE)

# pres.set_index('President')\
#     .loc[:, 'Background':'Average_rank']\
#     .iloc[:9]\
#     .T\
#     .plot.density()


# pres.set_index('President')\
#     .loc[:, 'Background':'Average_rank']\
#     .iloc[:9]\
#     .T\
#     .plot.hist()
    
# ax = pres.set_index('President')\
#     .loc[:, 'Background':'Average_rank']\
#     .iloc[:9]\
#     .T\
#     .plot.box(rot=45)

# ax.set_xticklabels(labels = (pres.President[:9]), ha= 'right')

