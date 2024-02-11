# import array as ar

# a= ar.array('i',[4,6, 2, 9])        # Here ar represents module name and array represents class name for which object a is created

## Creating an integer type array
# a = ar.array('i',[5,6,-7,8])

# print('The array elements are: ')
# for i in a:
#     print(i)

## from array import *     # means import all from array module

# a = array('i',[5,6,-7,8])           # i means signed integer

# print('The array elements are: ')
# for i in a:
#     print(i)
    
## Create an array with a group of characters

# from array import *
# a = array('u',['a', 'b', 'c', 'd', 'e']) # u means unicode characters

# print('The array elements are: ')
# for i in a:
#     print(i)
    
## Creating one array from another array

# from array import *

# arr1 = array('d', [1.5, 2.5, -3.5, 4])      # Here 'd' represents 'double precision floating point'

## use same type code and multiply each element off arr1 with 3

# arr2 = array(arr1.typecode,(a*3 for a in arr1))
# print('The arr2 elements are: ')
# for i in arr2:
#     print(i)

## Indexing and slicing on Arrays

# from array import *

# x = array('i', [10, 20, 30, 40, 50])

# n = len(x)

## Display array elements using indexing

# for i in range(n):
#     print(x[i], end=' ')        

## Retreive elements of an array using while loop

# from array import *

# x = array('i',[10, 20, 30, 40, 50])

# n = len(x)

# i = 0
# while i<n:
#     print(x[i], end=' ')
#     i += 1
    
## General format of a slice is:
## arrayname[start,stop, stride] We can eleminate one or any two of the items. Stride means step size

## e.g arr[1:4]  here slice gives elements from 1 to 3 from the array arr.

## Create array with y elements from 1st to 3rd from x.

# y = x[1:4]      # here 1 & 4 represent index numbers.
# print(y)

## Create array with elements from 0th till the last element in x

# y = x[0:]
# print(y)

## Create array with elements from 0th to 3rd from x.

# y = x[:4]
# print(y)

## Create array y with last elements from x.

# y = x[-4:]
# print(y)

## Create y with last 4th element and with 3 elements towards right.

# y = x[-4:-1]
# print(y)

## Create y with 0th to 5th element from x.
## Stride 2 means, after 0th element, retrieve :every 2nd element from x.

# y = x[0:5:2]
# print(y)

## Updating an array

# y = x[1:3] = array('i', [5,7])      # element 1 and 3 are replaced with elemets 5 & 7.
# print(y)

# from array import *

# x = array('i', [10, 20, 30, 40, 50, 60, 70])

## Display elements from 2nd to 4th only

# for i in x[2:5]:
#     print(i)

## Python program to understand various methods of array clas:

# from array import *

## Create an array with int values

# arr = array('i',[10, 20, 30, 40, 50])
# print('Original array:  ',arr)

## append 30 to the array arr
# arr.append(30)                  # append method
# arr.append(60)
# print('After appending 30 & 60: ',arr)

## insert 99 at position number 1 in arr
# arr.insert(1, 99)               # insert method
# print('After inerting 99 at position number 1 in arr: ',arr)

## remove an element from arr
# arr.remove(20)
# print('After removing 20: ',arr)

## remove last element from arr using pop() method
# n = arr.pop()
# print('Array after using pop() method: ',arr)
# print('Popped element: ',n)

## finding position of an element using index() method
# n = arr.index(30)
# print('First occurance of element 30 is at: ',n)

## convert an array into a list using tolist() method
# lst = arr.tolist()
# print('List: ',lst)
# print('Array: ',arr)

# Python Program for storing studentx into an array and finding total marks and percentage of marks

# from array import *

# lst = [int(i) for i in input('Enter Marks:  ').split(' ')]

# marks = array('i', lst)     # Creates an integer array from the above list

## Displays marks and the final total

# sum = 0
# for x in marks:
#     print(x)
#     sum += x
# print('Total Marks: ',sum)

## Display percentage

# n = len(marks)
# percent = sum/n
# print('Percentage: ',percent)

## Sort the array elements using bubble sort technique

# from array import *

# x = array('i', [])      # Create an empty array to store integers

# print('How many elements? ', end=' ')
# n = int(input())        # Accept input into n

# for i in range(n):          # repeat for n number of times
#     print('Enter Element: ', end=' ')
#     x.append(int(input()))  # add the element to the array x

# print('Original Array: ', x)

# flag = False                 # bubble sort begins
# for i in range(n-1):         # i is from 0 to n-1
#     for j in range(n-1-i):   # J is from 0 to one element less than n-1
#         if x[j] > x[j+1]:    # Fisrt element is greater  than the second element
#             t = x[j]            # Swap j and j+1 elements
#             x[j] = x[j+1]
#             x[j+1] = t
#             flag = True         # Swapping is done and hence flag is True
#     if flag == False:       # No swapping means array is in sorted order
#         break               # Exit the inner loop  
#     else:
#         flag = False        # Assign initial value to the flag
# print('Sorted array= ', x)

## Search for position of an element in the array using sequential search

# from array import *

# x = array('i', [])          # Create an empty array to store integers

# print('How many elements? ', end='')

# n = int(input())            # Accept the inpur value in n

# for i in range(n):
#     print('Enter element: ', end='')
#     x.append(int(input()))  # Add the element to the array
# print('Original Array: ', x)

# print('Enter element to search: ', end='')
# s = int(input())            # Accept element to be searched

# Flag = False                # This becomes true if the element is found

# for i in range (len(x)):
#     if s == x[i]:
#         print('Found at position=: ', i+1)      # We add 1 as array elements start from 0th position
#         flag = True
    
# if flag == False:
#     print('Not found in the array')
    
# import numpy as np

# arr = np.array([10, 20, 30, 40, 50])        # Create a single dimensioal array

# print(arr)                                  # Display the array

## Creating Arrays using Array()

# from numpy import *
# arr = array([10,20,30,40,50,60,70])
# print(arr)

# arr = array([10, 20, 30.1, 40])               # If array contains mix of intergers and floats, it will convert all element of arr into float
# print(arr)

# arr = array(['a', 'b', 'c', 'd', 'e'])
# print(arr)

# arr = array(['Mumbai', 'Ahmedabad','Delhi','Hyderabad'],dtype=str)      # old style
# print(arr)

# arr = array(['Delhi', 'Hyderabad', 'Mumbai', 'Ahmedabad'])
# print(arr)

## Create an array from another array

# from numpy import *

# a = array([1,2,3,4,5])          # Original array
# b = array(a)                    # Create array b from array a using array()
# c = a                           # Also can create c by assigning a to c

## Display the array
# print('a= ',a)
# print('b= ',b)
# print('c= ',c)

## Creating Arrays using linspace
## linspace(start, stop, n)      start represents starting element, stop represents ending element.
## 'n' is an integer that represents the number of parts the element should be divided.
## if 'n' is omitted, then it is taken as 50

# from numpy import *

## divide 0 to 10 into 5 parts and take those points in the array

# a = linspace(0, 10, 5)
# print('a= ', a)

## Creating Arrays using logspace
## It produces evenly spaced point on logarithmically spaced scale

# from numpy import *

# a = logspace(1, 4, 5)

# n = len(a)          # Find the number of elements in a

# for i in range(n):
#     print('%.1f' % a[i], end=' ')
    
# Create Arrays using arrange()

## Arange function in numpy is same as range function in Python

# Creating Arrays using zeros() and ones()
# zeros(n, datatype)        n represents the number of elements
# ones(n, datatype)     if we don't specify the datatype, then default datatype used by numpy is float.

# from numpy import *

# a = zeros(5)
# print(a)        # Notice the dots after the numbers as they are in float format

# b = zeros(5, int)
# print(b)        # Notice there are no dots after the numbers as the output is in int format

# c = ones(5, int)
# print(c)

## Mathmetical Operations on Arrays

## Some mathmetical operations on numpy arrays
# from numpy import *

# arr = array([10,20,30.5,-40])
# print('Original array: ', arr)

## Some mathmetical operations on the elements of a numpy array

# print('After adding 5: ', arr+5)
# print('After subtracting 5: ', arr-5)
# print('After multiplying with 5: ', arr*5)
# print('After dividing with 5: ', arr/5)
# print('After modulus with 5: ', arr%5)
# print('Expression Value: ', (arr+5)**2-10)
# print('Sine values: ', sin(arr))
# print('Cos value: ', cos(arr))
# print('Tan value: ', tan(arr))
# print('Biggest Element: ', max(arr))
# print('Smallest Element: ', min(arr))
# print('Sum of All Elements: ', sum(arr))
# print('Average of all elements: ', mean(arr))

## Comparing Arrays
## Comparing two arrays

# from numpy import *
# a = array([1,2,3,0])
# b = array([0,2,3,1])

# c = a == b
# print('Result of a==b: ',c)

# c = a > b
# print('Result of a>b: ',c)

# c = a <= b
# print('Result of a<=b: ',c)

# from numpy import *

# a = array([1,2,3,0])
# b = array([0,2,3,1])

# c = a>b
# print('Result of a > b: ',c)

# print('Check if any one element is true: ', any(c))
# print('Check if all elements are true: ', all(c))

# if(any(a>b)):
    # print('a contains atleast one one element greater than those of b')
    
    
## logical_and(), logical_or(), logical_not()

# from numpy import *

# a = array([1,2,3],int)
# b = array([0,2,3],int)

# c = logical_and(a>0, a<4)
# print(c)

# c = logical_or(b>=0, b==1)
# print(c)

# c = logical_not(b)
# print(c)

# # Using While()

# from numpy import *

# a= array([10,20,30,40,50], int)
# b = array([1,21,3,40,51], int)

# c = where(a>b, a, b)        # if a>b then take element from a else b
# print(c)

# # using nonzero()

# from numpy import *

# a= array([1,2,0,-1,0,6], int)

# c = nonzero(a)                  # retrieves indexes of non zero elements from a

# for i in c:                     # Display indexes of non zero elements
#     print(i)
    
# print(a[c])                     # display the non zero elements

## 'Aliasing' is not 'copying'. Aliasing means giving another name to existing object.

# from numpy import *

# a = arange(1, 6)                  # Create a array with elements 1 to 5.

# b = a                             # Give another name b to array a. Here array memory location is same

# print('Original array: ',a)
# print('Alias array: ',b)

# b[0] = 99                          # modify 0th element of b

# print('After modification: ')
# print('Original array: ',a)
# print('Alias array: ',b)

## Creating view() of an array

# from numpy import *

# a = arange(1,6)          # Creates a with elements 1 to 5
# b = a.view()             # Create a view of 'a' and call it'b'. Although b and a occupy different memory location, the b likes to mimic changes in a.

# print('Original array: ',a)
# print('New array: ',b)

# b[0] = 99               # modify 0th element of b

# print('After modification: ')
# print('Original array: ',a)
# print('New array: ',b)

## Copying an array where both the arrays are independent

# from numpy import *

# a = arange(1,6)     # Creates a with elements 1 to 5
# b = a.copy()        # create a copy of 'a' and call it'b

# print('Original array: ',a)
# print('New array: ',b)

# b[0] = 99

# print('After modification: ')
# print('Original Array: ',a)     # array a still unmodified
# print('New Array: ',b)          # Index 0 element is modified while rest remains same as a

# Slicing and indexing in numpy arrays

# arrayname[start:stop:stepsize]

# a[:] or a[::] means extract from 0th element till the end of the array.
# a[2:] extract from 2nd element until the end of the array

## Slicing operations on arrays

# from numpy import *

# a = arange(10, 16)
# print(a)

# b = a[1:6:2]        #Retrieve from 1st to one element prior to 6th element in step of 2
# print(b)

# b = a[::]           # Retrieve all elements from array
# print(b)

# b = a[-2:2:-1]  # Retrieve fm 6-2=4th elementn to one element prior to 2nd element
# print(b)

# b = a[:-2:]     # Retrieve fm 0th to one element prior to 4th element (6-2=4th)
# print(b)

## Retrieve & display elements of numpy array using indexing

# from numpy import *

# a = arange(10, 16)
# print(a)

# b = a[1:6:2] # Retrieve from 1st to one element prior to 6th element in step of 2
# print(b)

# i=0
# while(i<len(a)):        # Displays elements using indexing
#     print(a[i], end=' ')
#     i += 1
    
## One dimensional array (1D)
# from numpy import *

# arr1 = array([1,2,3,4,5])

# print(arr1)

# arr2 = array([10,
#               20,
#               30,
#               40])
# print(arr2)

## Two dimensional array (2D)

# arr2 =array([[1,2,3],
#             [4,5,6]])
# print(arr2)

# arr3 = array([[[1,2,3], [4,5,6]], [[1,1,1], [1,0,1]]])
# print(arr3)

## ndim Attribute

## ndim attribute represents the number of dimensions of the array.
## Number of dimensions is also referred to as 'rank'

# from numpy import *

# arr1 = array([1,2,3,4,5])
# print(arr1.ndim)

# arr2 = array([[1,2,3], [4,5,6]])
# print(arr2.ndim)

## shape attribute
## shape attribute describes the shape of the array. 
## shape is a tuple listing the number of elements along each dimension
## a dimension is called an axis.
## for 1D array, shape gives the number of elements in the row.
## for 2D array, shape specifies the number of rows and columns in each row.

# from numpy import *

# arr1 = array([1,2,3,4,5])       # Will print number of elements in the row
# print(arr1.shape)

# arr2 = array([[1,2,3], [4,5,6]])
# print(arr2.shape)               # Will show 2 rows and 3 columns in each row

# arr2.shape = (3,2)              # Change the shpae of arr2 to 3 rows and 2 columns
# print(arr2)

## Size Attribute
## Size attribute gives total number of elements in the array.

# from numpy import *

# arr1 = array([1,2,3,4,5])   # Will print number of elements in the row
# print(arr1.size)

# arr2 = array([[1,3,3], [4,5,6]])
# print(arr2.size) # Will show 6 since 3+3 = 6

## Itemsize attribute

## itemsize gives the memory size of the array elements in bytes (1 byte equals to 8 bits)

# from numpy import *

# arr1 = array([1,2,3,4,5])
# print(arr1.itemsize)

# arr2 = array([1.1,2.1,3.5,4,5.0])
# print(arr2.itemsize)

## dtype attribute
## datatype attribute gives the datatype of the array elemens in the array. 

# from numpy import *

# arr1 = array([1,2,3,4,5])
# print(arr1.dtype)

# arr2 = array([1.1, 2.1, 3.5, 4.5, 0])
# print(arr2.dtype)

## nbyte attribute

## nbytes attribute gives the total number of bytes occupied by an array
# from numpy import *

# arr2 = array([[1,2,3], [4,5,6]])
# print(arr2.nbytes)

# # reshape() method

# from numpy import *

# arr1 = arange(10)
# print(arr1)

# arr1 = arr1.reshape(2,5)        # change the shape to 2 rows, 5 columns
# print(arr1)

# arr1 = arr1.reshape(5,2)
# print(arr1)

## flatten method

## flatten method is useful to return a copy of the array collapsed into one dimension.

## arr1 = array([[1,2,3], [4,5,6]])
## print(arr1)

## arr1 = arr1.flatten()           # Converts 2D array into 1D array
## print(arr1)

## Flatten method. Collapse 2D arrays into one dimension

# from numpy import *

# arr1 = array([[1,2,3], [4,5,6]])
# print(arr1)

# arr1 = arr1.flatten()
# print(arr1)

# A 2D array with 'm' rows and 'n' columns is called m x n matrix.

# Array()
# used for creating multidimensional array
# pass one list of elements to this function, then it will create 1D array
# pass two lists of elements, then this function will create a 2D array.

# ones() and zeros()

# Ones() is useful to create a 2D array with several rows and columns where all elements
#  will be taken as 1. 
# ones() format: ones((r,c), dtype)

# from numpy import *

# a = ones((3,4), float)  # Decimal point after each element represents that numbers are float
# print(a)

# b = zeros((3,4), float) 
# print(b)

## eye()
## this function creates a 2D array and fills the elements in the diagonal with 1s.
## format: eye() - eye(n, dtype = datatype)

# a = eye(3)      # Creates 3 rows and 3 columns.
# print(a)

## reshape() function
## format: reshape(arrayname,(n, r,c))
## Here arrayname represents the name of the aarray whose elements to be converted.
## n indicates the number of arrays in the resultant array
## r and c indicates the number of rows and columns

# a = array([1,2,3,4,5,6])

# b= reshape(a, (2,3))
# print(b)

# b = reshape(a, (3, 2))
# print(b)

# a = arange(12)
# print(a)

# b = reshape(a, (2,3,2)) # 2 means 2 arrays each with 3 rows and 2 columns
# print(b)

# b = reshape(a, (3,2,2)) # 3 means 3 arrays each with 2 rows and 2 columns
# print(b)

# retrieve elements from a 2D array

# from numpy import *

# a = [[1,2,3], [4,5,6], [7,8,9]]

# for i in range(len(a)):
#     print(a[i])
    
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j], end=' ')
        

## retrieve elements from a 3D array

# a = [[[1,2,3],
#      [4,5,6]],
     
#      [[7,8,9],
#      [10,11,12]]]

# for i in range(len(a)):
#     for j in range(len(a[i])):
#         for k in range(len(a[i][j])):
#             print(a[i][j][k], end=' ')
#         print()
#     print()

# Slicing multi Dimensional arrays

# from numpy import *

# a = [[1,2,3], [4,5,6], [7,8,9]]

# a = reshape(a,(3,3))
# print(a[:,:])
# print(a[:])       # Without start and end parameters, it will print entire array

# print(a[0,:])       # Will print only 0th row

# print(a[:, 0])        # Will print only 0th column

# print(a[0:1, 0:1])    # Will print only 1st element from 0th row and 0th column

# print(a[1:2, 1:2])    # Will print only 1st element from 1st row and 1st column

# print(a[2:3, 1:2])    # row 2 to 2 (n-1 = 3-1=2) & column 1 to 1. Only element here is 8

# a = reshape(arange(11, 36, 1), (5,5))
# print(a)

# # To display top 2 rows and 3 columns

# print(a[0:2, 0:3])      # Slice 2 rows from 0th row and 3 columns from 0th column

# print(a[0:2, 2:])       # slice 2 rows from 0th row an 2 columns from 2nd column

# print(a[2:, 3:])        # slice everything from 2nd row below and everything from 3rd column

# Matrices in Numpy

# if matrix has only 1 row, it is called a 'row matrix'

# if matrix has only 1 column, it is called a 'column matrix'

# from  numpy import *

## a = matrix([[1,2,3], [4,5,6]])
## print(a)

# b = matrix('1 2; 3 4; 5 6')
# print(b)

## To retrieve diagonal elements of matrix, use diagonal() function:

# a = diagonal(matrix)

# a = matrix('1 2 3; 4 5 6; 7 8 9')
# print(a)

# dia = a.diagonal()
# print(dia)

## Find max & min elements

# Use max() and min() functions

# big = a.max()
# print(big)

# small = a.min()
# print(small)


##Sum & Average of elements

# total = a.sum()
# print(total)

# avg = a.mean()
# print(avg)

## Product if elements

# m = matrix(arange(12).reshape(3,4))
# print(m)

# a = m.prod(0)    # will give multiplication results each column wise. '0' means column wise
# print(a)

# a = m.prod(1)   # will give multiplication results each row wise. '0' means row wise
# print(a)

## Sorting the Matrix

# m = matrix([[5,4,1], [2,7,0]])
# print(m)

# a = sort(m)     # Without axis value, only rows will be sorted ascending order
# print(a)

# b = sort(m, axis=0)
# print(b)

## Transpose of Matrix

## Transpose means rewriting matrix rows into columns and columns into rows.

# from numpy import *

# m = matrix('1 2 3; 4 5 6; 7 8 9')
# print(m)

# t = m.transpose()
# print(t)

# t1 = m.getT()       # Find transpose using getT()
# print(t1)

# from numpy import *

# r, c = [int(a) for a in input('Enter rows, cols: ').split()]

# str = input(' Enter matrix elements:\n ')

# x = reshape(matrix(str), (r,c))

# print('The Original Matrix: ', x)

# print('The Transpose matrix: ')

# y = x.transpose()
# print(y)


## Matrix Addition & Multiplication

# a = matrix('1 2 3; 4 5 6')
# b = matrix('2 2 2; 1 -1 2')
# print(a)

# print(b)

# c = a+b     # Addition of two matrix
# print(c)

# d = a/b
# print(d)

## Matrix Multiplication conditions

## The number of columns in 'a' should be equal to the number of rows in 'b'

# from numpy import *
# import sys

# r1, c1 = [int(a) for a in input('First matrix Rows, Cols:  ').split()]

# r2, c2 = [int(a) for a in input('Second Matrix Rows, Cols: ').split()]

# if c1 != r2:        # Test the condition if c1 != r2, then multiplication not possible
#     print('Multplication is not possible')
#     sys.exit()    # Terminate the program
    
# str1 = input('Enter First Matrix Elements:\n ') # Accept first element as string

# x = reshape(matrix(str1), (r1,c1))

# str2 = input('Enter Second Matrix Elements:\n ')

# y = reshape(matrix(str2), (r2,c2))

# print('The Product Matrix is: ')

# z = x*y

# print(z)

## random Numbers

from numpy import *

a = random.rand(5)
print(a)

b = random.rand(2,3)        # Print output in 2 rows and 3 columns
print(b)
