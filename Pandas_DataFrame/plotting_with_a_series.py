import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt


url = 'https://github.com//mattharrison/datasets/raw/master/data/alta-noaa-1980-2019.csv'

alta_df = pd.read_csv(url)

dates = pd.to_datetime(alta_df.DATE)

snow = alta_df.SNOW.rename(dates)

#! The plot attribute

#! Histograms

# snow.plot.hist()

# snow[snow>0].plot.hist(bins=20, title='SnowFall Histogram (In)')

#^ The bins here represent numbers of towers/vertical bars to be created from the given data. The default value of the number of bins to be created in a histogram is 10. Number of bins displayed will always be one less that the number of created, since bins are read as first bin = 1 to 2, second bit = 2 to 3, third bin = 3 to 4 and so forth.

#! Box Plot

# snow.plot.box()

# snow[lambda x:(x.index.month == 1) & (x>0)].plot.box()

#% Bottom green horizontal line of blue box plot is minimum value.

#% First green horizontal line of rectangle shape of blue box plot is First quartile or 25%

#% Second green horizontal line of rectangle shape of blue box plot is Second quartile or 50% or median.

#% Third green horizontal line of rectangle shape of blue box plot is third quartile or 75%

#% Top green horizontal line of rectangle shape of blue box plot is maximum value.

#% Small circle shape of box plot are outlier data or erroneous data.


#! Kernel Density estimation plot

# snow[lambda x:(x.index.month ==1) & (x>0)].plot.kde()


#! Line Plots

#% Plots values on the y-axis and the index on the x-axis

# snow.iloc[-300:].plot.line()


# snow.resample('ME').mean().plot.line()

#! Line plots with Multiple Aggregations

# snow.resample('QE').quantile([.5,.9,.99]).unstack().iloc[-100:].plot.line()

#^ unstack() method moves the rows to become columns and the columns to become rows

#! Bar Plots

season2017 = snow.loc['2016-10':'2017-05']

# season2017.resample('ME').sum().div(season2017.sum()).mul(100).rename(lambda idx:idx.month_name()).plot.bar(title='2017 Monthly Percent of Snowfall')


url = 'https://github.com/mattharrison/datasets/raw/master/data/vehicles.csv.zip'

df = pd.read_csv(url, low_memory=False)

make = df.make    ## make is the name of the column in the given data

# make.value_counts().plot.bar()


top10 = make.value_counts().index[:10]

# make.where(make.isin(top10), 'Other').value_counts().plot.barh()

#^ barh means horizontal bars



#! Pie Plots

# season2017.resample('ME').sum().div(season2017.sum()).mul(100).rename(lambda idx:idx.month_name()).plot.pie(title='2017 Monthly Percent of Snowfall')


#! Styling with Seaborn library

color_palette = ['#440154','#482677','#404788','#33638d','#287d8e','#1f968b','#29af7f','#55c667','#73d055','#b8de29','#fde725']

fp = matplotlib.font_manager.FontProperties(fname='/Fonts/roboto/Roboto-Condensed.ttf')


with sns.plotting_context(rc=dict(font='Roboto',palette=color_palette, hue=None)):  ## code from seaborn
    fig, ax= plt.subplots(dpi=600, figsize=(10,4))      ## This code is from matplotlib.
    
snow.plot.hist()             ## This is from matplotlib.
# sns.histplot(snow)           ## This is a seaborn code
# fig.savefig('snowhist.png',dpi=600,bbox_inches='tight')  ## This is a matplotlib code

#! with function acts as a context manager to temporarily change parameters values.

#* plt.fig takes following parameters:


#! figsize = 6.4, 4.8 (default size) dimension (width, height) in inches.

#! dpi = 100.0 (default)

#! savefig('filename.png', dpi of the fig to be saved, bbox_inches means bounding box in inches)
#! tight parameters would save the fig without any margins


# #% Plot example

# data = np.array([44, 45, 40, 41, 39]) 
# keys = ['Class 1', 'Class 2', 'CLass 3', 'Class 4', 'Class 5'] 

# explode = [0, 0.1, 0, 0, 0]

# plt.pie(data, labels=keys, explode=explode, startangle=90, shadow=True, autopct='%.0f%%')

# plt.show()

# sns.color_palette('tab10')

# sns.color_palette('hls',8)

