
#% When artificial neural networks are used in machine learning programs, they are known as 'deep learning' programs.

#* Machine learning process

#% step 1:

#% The data should be in a file. First, we should read the data from the file and provide that data to the computer in the form of DataFrame object. A DataFrame object represents the data in the form of a table.

#% Step 2:

#% This data should be analyzed and understood properly by the computer. For this purpose, we have to provide brain (logic) to the computer. The brain of the computer represents the logic or algorithm, which is called a 'machine learning model'. This model helps the computer to go through all the data and understand them. This is known as 'training'.

#% Step 3:

#% Once computer gets trained on the given data, it is now ready to make predictions on new data.

#% When we can show the relationship between the 'Sales' and 'TV ads' using a straight line, it is called a linear relationship and in this case, we can use a machine learning model called 'LinearRegression'.

#! Predict the number of advertisements based on the targeted sales using the Linear Regression machine learning model.

from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import pandas as pd


## Load the data into the DataFrame
df = pd.read_csv('C:/Users/shekh/Projects/Python_Tutorials/Core_Python/advt.csv')

## take the Sales column as input data(x)
## take the TV_ads column as target data(y)

x = df.iloc[:,1:2] ## select all rows for cols 1
y = df.iloc[:,2]    ## select all rows for cols 2

## plot a scatter plot to know the relation between x and y

# plt.scatter(x,y,color='red')
# plt.xlabel('Sales ($)')
# plt.ylabel('Number of TV ads')
# plt.show()

#% IMPORTANT:

#% The above scatter plot shows that the points can be shown on a straight line. Hence we can use Linear Regression model.

model = LinearRegression()
model.fit(x.values,y)  ## fitting means 'training'

## Find the accuracy of our model
model.score(x.values,y) ## Result of model accuracy

#~ 0.9309806250753205
## The above means that the accuracy of the model is more than 93%

## For all x values, the model can predict its own y values

predicted_y = model.predict(x.values)

## plot a scatter plot again with the predicted y values

## Straight line indicates output from linear regression model

plt.xlabel('Sales ($)')
plt.ylabel('Number of TV ads')
plt.scatter(x,y,color='red', marker='+')
plt.plot(x, predicted_y, color='blue')

model.predict([[20000]])

#~ array([152.11752883])

#% The above prediction of 152.12 ads to achieve the sales target of 20000 TV is the outcome of the linear regression model.

