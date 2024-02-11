
#@ Creating list using range()

#! range(start, stop, stepsize)

## if stepsize is not mentioned, it is taken to be 1

# for i in range(0,10,1): 
#     print(i, end=' ')
    
# lst = list(range(4,15,2))
# print(lst)

#! It is important to use the for loop or convert the range object into a list t0
#! to get the range output

# list = [10, 20, 30, 40, 50]

# for i in list:
#     print(i)
    
# #@ updating the elements of a list

# lst = list(range(1,5))
# print(lst)

# lst.append(9)
# print(lst)

# #! updating the list means changing the value of the element in the list

# lst[1] = 8
# print(lst)

# lst[1:3] = 10, 11
# print(lst)

# #@ Deleting an element from the list using position number

# del lst[1]      ## here we need to pass the position number of the element
# print(lst)

# #@ Deleting an element from the list using the element value

# lst.remove(11)
# print(lst)


# #@ Retrieving the elements of the list in the reverse order.

# # lst.reverse()
# # print(lst)

# days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

# days.reverse()

# print(days)

# for i in days:
#     print(i)

# #@ Repetition of lists

# x = [10, 20, 30, 40, 50]

# print(x*2)      ## repeat list x two times

# #@ Membership in List - To check if element is a member of the list

# y = [10, 20, 30, 40, 50]

# a = 20

# print(a in y)       ## check if a is a member of list y

# print(a not in y)   ## check if a is not a member of list

# #@ Aliasing Lists

# X = [10, 20, 30, 40, 50]

# Y = X   ## here the same list is having two names.

# print(X)
# print(Y)    ## In aliasing, if one list is modified, the other list also gets modified

# #@ Cloning Lists

# Y = X[:]    ## X is cloned as Y

# #! When we clone like the above, a separate copy of all elements is stored into Y. The list X & Y are independent

# X[1] = 99
# print(X)
# print(Y)

# Y = X.copy()    ## using copy method to copy the list

#@ Using various list processing methods

# num = [10, 20, 30, 40, 50]

# print('Number of elements in this list: ',len(num))       ## Gives number of elements in the list

# num.append(65)  ## appends the given number in the list
# print('The new appended list: ',num)

# num.insert(0,5)     ## Inserts number 5 at 0 index position
# print('List after inserting new number at 0th position: ',num)

# num1 = num.copy()          ## Will copy all elements from num to num1
# print('Newly created independent list: ',num1)

# num.extend(num1)          ## will append num1 list to num list
# print('num list after appending num1: ',num)

# n = num.count(50)       ## Will count total occurrence of number 50 in the given list
# print('Number of times number 50 found in the list: ',n)

# num.remove(50)
# print('Num list after removing first occurrence of number 50: ',num)

# num.pop()
# print('Num list after removing last element from this list: ', num)

# num.sort()
# print('Num list after sorting: ', num)

# num.reverse()
# print('Num list after reversing: ',num)

# num.clear()
# print('Num list after removing all elements: ', num)

#@ Finding Biggest and smallest elements in list

# z = [5, 10, 20, 30, 40, 65, 5, 10, 20, 30, 40, 50]

# big = max(z)
# print('Biggest element in z list: ',big)

# sml = min(z)
# print('Smallest element in z list: ',sml)

#% EXERCISE 1

# x = []      ## take an empty list

# print('How many elements? ',end=' ')
# n = int(input())        ## accept input into variable n

# for i in range(n):
#     print('Enter elements: ', end=' ')
#     x.append(int(input()))

# big = max(x)
# sml = min(x)

# print('\nThe Biggest number in the given list is: ', big)
# print('The Smallest number in the given list is: ', sml)

#@ Sorting the List Elements

# list2 = [12, 18, 9, 3, 15, 6]

# list2.sort()

# print(list2)

#@ Number of occurrences of an element in the list

#% EXERCISE 2

# x = []      ## take an empty list

# print('How many elements? ')
# n = int(input())

# for i in range(n):
#     print('Enter desired elements: ')
#     x.append(int(input()))

# print('The list provided is: ',x)

# y = int(input('Enter the element whose total count is required: '))

# n = x.count(y)

# print('The total count for number',y,'is: ',n)

#@ Finding common elements in two lists

# n1 = ['Shekhar', 'Sushama', 'Ashish','Aakash', 'Ranveer', 'Aarav']
# n2 = ['Ashish', 'Nibha', 'Aarav']

# p = set(n1)
# q = set(n2)

# s = p.intersection(q)

# common = list(s)
# for i in common:
#     print(i)

#@ storing different types of Data in a list

# emp = []        ## Create an empty list to store employee data

# n = int(input('How many employees? '))

# for i in range(n):                  ## This will store data for all the employees
#     print('Enter ID: ', end=' ')
#     emp.append(int(input()))
#     print('Enter Name: ', end=' ')
#     emp.append(input())
#     print('Enter Total Salary: ', end=' ')
#     emp.append(float(input()))

# print('\nThe list is created with employee data.')

# id = int(input('Enter Employee id: '))      ## Here enter the id of the employee whose data is required

# for i in range(len(emp)):                   ## This will retrieve the data for the desired employee
#     if id==emp[i]:
#         print('Id = {:d}, Name= {:s}, Salary = {:.2f}'.format(emp[i],emp[i+1], emp[i+2]))
#         break
    

#@ Nested Lists

## A list within another list is called a nested list

# a = [80, 90]
# b = [10, 20, 30, a]     ## Here a is inserted as an element of b and hence 'a' is called a nested list.

# print(b)

# b[0] = 10
# b[1] = 20
# b[2] = 30
# b[3] = [80, 90]         ## Here b[3] represents a nested list

# for i in b[3]:
#     print(i)
    
#% EXERCISE 3

#@ Create a nested list and display its content

# list = [10, 20, 30, [80, 100]]

# print('Total Lists = ', list)       ##  Display entire list

# print('First Element = ',list[0])   ## Display first element

# print('Last element is nested list = ',list[-1])

# for i in list[-1]:
#     print(i)

#! We can also refer nested list elements as: 
#! list[-1][0]
#! list[-1][1]

#@ Nested Lists as Matrices

#! Create a matrix with 3 rows and 3 columns

mat = [[1,2,3], [4,5,6], [7,8,9]]   ## Here 'mat' is a list that contains 3 lists which are rows of mat list.

# [[1,2,3],
#  [4,5,6],
#  [7,8,9]]

# for r in mat:
#     print(r)        ## Display row by row
    
# for r in mat:
#     for c in r:     ## Display columns in each row
#         print(c, end=' ')
#     print()
    
#! Another way of displaying matrix elements is using indexing:

## mat[i][j] represents ith row and jth column. Also matrix has 'm' rows and 'n' columns

# for i in range(len(mat)):                           ## i value changes from 0 to m-1
#     for j in range(len(mat[i])):                    ## value changes from 0 to n-1
#         print('%d' % mat[i][j], end=' ')
#     print()
    
#% Exercise 4

#% Retrieve elements from a matrix and display them

## Displaying nested list as matrix

# mat =[[1,2,3], [4,5,6], [7,8,9]]


# print('Display the list as it is: \n',mat)

# print('Display row by row: ')

# for r in mat:
#     print(r)
    
# print('Display each column in row 0: ')
# for c in mat[0]:
#     print('%d' % c, end=' ')        ## This will print only 1 char from the first col first row
# print()                             ## This will loop until all 3 chars are printed in the 1st row

# print('Display each column in row 1: ')
# for c in mat[1]:
#     print('%d' % c, end=' ')        ## This will print only 1 char from the first col first row
# print()

# print('Display each column in row 2: ')
# for c in mat[2]:
#     print('%d' % c, end=' ')        ## This will print only 1 char from the first col first row
# print()

# print('Display all elements using for: ')
# for r in mat:
#     for c in r:
#         print('%d' % c, end=' ')
#     print()
    
# print('Display all elements using for: ')
# for i in range(len(mat)):
#     for j in range(len(mat[i])):
#         print('%d' % mat[i][j], end=' ')
#     print()
    
#% EXERCISE 5

#% Add two matrices and display the sum matrix using lists

# #! matrix 1 with 3 rows & 4 cols

# m1 = [[1,2,3,0],
#       [4,5,6,0],
#       [7,8,9,0]]

# #! matrix 2 with 3 rows & 4 cols

# m2 = [[1,2,3,4],
#       [1,0,1,0],
#       [2,-1,-2,1]]

# #! Take matrix 3 with 3 rows & 4 cols and initialize with all 0s

# m3 =  [ 4*[0] for i in range(3)]        ## repeat four 0s for 3 times

#! Add the corresponding elements of m1 & m2 and store into m3

# for i in range(3):                          ## for loop will go through rows thrice
#     for j in range(4):                      ## for loop will go through columns 4 times
#         m3[i][j] =  m1[i][j]+m2[i][j]
        
# #! Display 3rd matrix using for loop

# for i in range(3):
#     for j in range(4):
#         print('%d' % m3[i][j], end=' ')
#     print()

#@ List Comprehension

#* List comprehensions represent creation of new lists from an iterable object (e.g. a list, set, tuple, dict or range)

#% EXERCISES

#! Create a list with squares of integers from 1 to 10.

# squares = []

# for x in range(1, 11):          ## Get numbers between 1 and 10
#     squares.append(x**2)        ## Add square of x to the list

# print('The squares of the given numbers are: ',squares)

#* Get squares of integers from 1 to 10 and take only even numbers from the result.

# sq = [i**2 for i in range(1, 11) if i%2 == 0]
       
# print(sq)

#! The above expression can also be written without using if statement

# x = [i**2 for i in range(2,11,2)]
# print(x)

#* We have 2 lists x & y. Add each element of 'x' with each element of 'y'.

x = [10, 20, 30]
y = [1,2,3,4]

# lst = []

# for i in x:
#     for j in y:
#         lst.append(i+j)
        
# print(lst)

#! Same list can be achieved using list comprehension as:

# lst = [i+j for i in x for j in y]

# print(lst)

#! Or we can directly mention the lists in the list comprehension as:

# lst = [i+j for i in [10,20,30] for j in [1,2,3,4]]
# print(lst)

#! The above expression can also be written using strings as:

# lst = [i+j for i in 'ABC' for j in 'DE']

# print(lst)

#* Store the first letters from the given strings and store them in a new list

words = ['Apple', 'Grapes', 'Banana', 'Orange']

# lst = []

# for w in words:
#     lst.append(w[0])
        
# print(lst)

#! The above result can also be obtained by comprehension:

# lst = [w[0] for w in words]
# print(lst)

#! Create a new list num3 with numbers present in num1 but not in num2

# num1 = [1,2,3,4,5]
# num2 = [10,11,1,2]

# num3 = []

# for i in num1:
#     if i not in num2:
#         num3.append(i)
# print(num3)

#! The above result can also be achieved using comprehension

# num3 = [i for i in num1 if i not in num2]
# print(num3)

#* Like list comprehensions, it is also possible to create set comprehensions and dictionary comprehensions.

# dict = {1001: 'Pratap', 1002: 'Mohan', 1003: 'Ankita'}

## Here 1001 is the hall ticket number of the student named pratap. 

## We can create dictionary comprehension to convert keys as values and vice versa as:

# dict1 = {value : key for key, value in dict.items()}

# #* in above expression, value:key is an instruction to interchange key with value and value with key
# #* for every key and value in dictionary items.

# print(dict1)

#@ Tuples

## A tuple is a Python sequence to store a group of elements or items.
#* Tuples are immutable.
#* Hence we can not perform append(), extend(), insert(), remove(), pop() and clear() on Tuples.

#* Tuples are used to store data which should not be modified. Its data can only be retrieved on demand.

#@ Creating Tuples

# tup1 = ()       ## empty tuple

# tup2 = (10,)    ## To create a tuple with only one element, we need to add a comma after the element

# tup3 = (10, 20, -30.1, 40.5, 'Mumbai', 'Varanasi')  ## Tuple with different types of element

# tup4 = (10,20,30)   ## Tuple with only integers

#* If we do not apply any brackets and write the elements, separated by commas, then they are taken by
#* default as tuple. It will not become list or any other datatype.

tup5 = 1,2,3,4,5        ## no braces

#! Creating tuple from a list

# list = [1,2,3]
# tpl = tuple(list)       ## Converting list into tuple
# print(tpl)

#! Creating tuple using range() function

# tpl = tuple(range(4,9,2))   ## numbers from 4 to 8 in steps of 2
# print(tpl)

#@ Accessing the tuple elements

# tup = (50,60,70,80,90,100)

# #* Indexing represents the position number of the element in the tuple.

# print(tup[0])       ## Print element at 0th index in the given tuple

# print(tup[-1])      ## Would print the last element in the given tuple

# print(tup[-6])      ## Would print 6th element from the left in the given tuple

# #* Slicing operation on tuple

# #! format:  [start:stop:stepsize]

# print(tup[:])       ## print everything from the beginning to end

# print(tup[1:4])     ## would print all elements between 1st index position to 3rd index position

# print(tup[::2])     ## would print every other elements in the tuple

# print(tup[::-2])    ## would print every other elements in the reverse order

# print(tup[-4:-1])   ## Would print from the 4th element from the last until the second last element

#* Extracted elements from the tuple should be stored in separate variables.

# student = (10, 'Vinay Kumar', 50, 60, 65, 61, 70)

# rno, name = student[0:2]    ## here rno represents 10 and name represents 'vinay Kumar'

# print(rno)

# print(name)

# #* To retrieve the marks of student from student tuple:

# marks = student[2:7]    ## store the elements from 2nd to 6th into 'marks'

# for i in marks:
#     print(i)

#@ Basic Operations on Tuples

#* Find the length of Tuple

student = (10, 'Vinay Kumar', 50, 60, 65, 61, 70)
# print(len(student))

#* Concatenate two tuples and store result in a new tuple

fees = (25000.00,)*4        ## repeat the tuple element 4 times
# print(fees)

student1 = student+fees
# print(student1)

#* Searching if an element is a member of the tuple or not can be done using 'in' and 'not in' operators.

name = 'Vinay Kumar'

name in student1

name not in student1

#* repetition operator '*' will repeat the tuple elements

# tpl = (10, 11, 12)
# tpl1 = tpl*3            ## repeat for 3 times and store result in tpl1
# print(tpl1)

#* Functions to process Tuples

# len(tpl)            ## Returns number of elements in the given tuple
# min(tpl)            ## Returns smallest element in the tuple
# max(tpl)            ## Returns biggest element in the tuple.
# tpl.count(x)        ## Returns how many times the element 'x' has been found in tpl
# tpl.index(x)        ## Returns the first occurrence of the element 'x' in tuple.
# sorted(tpl)         ## Sorts the elements of the tuple in ascending order.
# sorted(tpl, reverse=True)   ## sorts the elements of the tuple in reverse order

#% Exercise

#* Accept elements in the form of tuple and display their sum and average

# num = eval(input('Enter elements in (): ')) ## eval() evaluates if the typed elements are a list or tuple.
# sum = 0
# n = len(num)    ## 'n' is the number of elements in the given tuple

# for i in range(n):
#     sum += num[i]       ## add each element to the sum
    
# print('Sum of numbers: ',sum)
# print('Average of numbers: ',sum/n)

#* When a group of elements are entered with commas (,), then they are taken by default as a tuple in Python

#* Find the first occurrence of an element in a tuple

# str = input('Enter elements separated by commas: ').split(',')
#       #* accepts elements from keyboard as strings separated by commas

# lst = [int(num) for num in str]     ## string is converted into an integer using for loop

# tup = tuple(lst)        ## list is converted into tuple

# print('The tuple is: ', tup)        ## display the tuple

# ele = int(input('Enter an element to search: '))

# try:
#     pos = tup.index(ele)    ## returns the first occurrence of the given element
#     print('Element position number: ', pos+1)
# except ValueError:          ## if element is not found, valueError will rise
#     print('Element supplied is not found in tuple')

#@ Nested Tuples

# tup = (50, 60, 70, 80, 90, (200, 201))  ## tuple with 6 elements

#* Sorting Nested Tuples

emp = ((10, 'vijay', 90000.90), (20, 'sundari', 55000.75), (30, 'veronica', 89000.00), (40, 'betty', 60000.50))

#! print(sorted(emp))

## Will sort the tuple 'emp' in ascending order of the 0th element in the nested tuples.

## If wish to sort the tuple based employee name, which is the 1st element in the nested tuples, we can use
## a lambda expression

# print(sorted(emp, key = lambda x: x[1]))    ## sort on name

## here key indicates the key for the sorted() function that tells on which element sorting should be done.
## the lambda function: lambda x: x[1] indicates that x[1] should be taken as the key, which is 1st element

#* Sort a tuple with nested tuples

# emp = ((10, 'vijay', 90000.90), (20, 'sundari', 55000.75), (30, 'veronica', 89000.00), (40, 'betty', 60000.50))

# print(sorted(emp))                          ## sorts by default on Id
# print(sorted(emp, reverse=True))            ## sorts by default on reverse id
# print(sorted(emp, key = lambda x: x[1]))    ## Sort on name
# print(sorted(emp, key = lambda x: x[2]))    ## sort on salary

#@ Inserting elements in a Tuple

#% Exercise

#* Insert a new element into a tuple of elements at a specified position

# names = ('clint', 'betty', 'veronica', 'andrea')
# print(names)

# ## accept new names and position number
# lst = [input('Enter a new name: ')]
# new = tuple(lst)
# pos = int(input('Enter a position number: '))

# ## copy from 0th to pos-2 into another tuple 'names1'
# names1 = names[0:pos-1]

# ## concatenate new element at pos-1
# names1 = names1 + new

# ## concatenate the remaining elements of names from pos-1 till end
# names = names1 + names[pos-1:]
# print(names)

#@ Modify Elements of a Tuple

#% Exercise

#* Modify or replace an existing element of a tuple with a new element

# num = (10,20,30,40,50)
# print(num)

# ## Accept a new element and position number

# lst = [int(input('Enter a new element: '))]
# new = tuple(lst)
# pos = int(input('Enter position number: '))

# ## Copy from 0th to pos-2 into another tuple

# num1 = num[0:pos-1]

# ## Concatenate new element at pos-1
# num1 = num1+new

# ## Concatenate the remaining elements of num from pos till end
# num = num1 + num[pos:]
# print(num)

#@ Deleting an element from Tuple

#* Simplest way to delete an element from a particular position in the tuple is to copy all
#* the elements into a new tuple except the element which is to be deleted.

#% Exercise

#* Delete an element from a particular position in the tuple

num = (10, 20, 30, 40,50)

## Accept position number of the element to delete
pos = int(input('Enter position number of the element to be deleted: '))

## copy from 0th to pos-2 into another tuple

num1 = num[0:pos-1]

## Concatenate the remaining elements of num from pos till end

num = num1 + num[pos:]

print(num)
