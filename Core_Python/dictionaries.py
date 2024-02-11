
#% EXERCISE

#* Create a dict with students details and retrieve values using keys

# dict = {'Name': 'Aarav', 'Id': 10, 'marks': 99}

#* Access values by giving keys

# print('Name of student= ',dict['Name'])
# print('ID Number= ',dict['Id'])
# print('Marks Obtained= ',dict['marks'])

#@ Operations on Dictionaries

#! To find no. of key-value pairs in the dict

# n = len(dict)       ## Tells no. of key-value pairs in dict
# print('Number of Key Value pairs= ',n)

# #! Modifying value of key

# dict['marks'] = 99.99

# #! Inserting a new key-value pair

# dict['Grade'] = 'A+'

# print('Name of student= ',dict['Name'])
# print('ID Number= ',dict['Id'])
# print('Marks Obtained= ',dict['marks'])
# print('Grades Obtained= ',dict['Grade'])
# print(dict)

#! Deleting a key value pair

# del dict['Id']
# print(dict)

#! Checking key membership

# 'Grade' in dict

# 'Gender' in dict

# 'Gender' not in dict

#@ Rules for Dictionary

#* Keys should be unique
#* No duplicate keys allowed
#* If same key entered again, old key will be overwritten

#* Keys should be immutable type
#* Can use a number, string or tuple as keys since they are immutable.
#* Can not use lists or dict as keys. If used as keys, will result in 'TypeError'.

# d = {'Nag': 10, 'Vishnu': 20, 'Nag':30}   ## Nag entered twice
# print(d)

#~ output = {'Nag': 30, 'Vishnu': 20} 'Nag' is replaced by new key


# d = {['Nag']:10, 'Vishnu': 20, 'Raj':30}
# print(d)

x = {'Vishnu':50}

#~ Output  = TypeError: unhashable type: 'list'

#@ Dictionary methods

# d = {'Ram': 10, 'Vishnu': 20, 'Nag':30}

# seq = {'a', 'b', 'c'}
# lst = [1,2,3]

# d2 = {'k': 5}

# d.clear()   ## Removes all key-value pairs from dictionary 'd'

# d1=d.copy() ## Copies all elements from 'd' into new dict 'd1'

# d.fromkeys(seq, lst)   ## Creates a new dict with specified keys and values

# d2.get('k', 'Not Found')    ## get value associated with key 'k' in dict d2. Else return 'Not Found'
                            
# d.items()   ## returns an object containing key-value pairs of 'd'. Pairs are stored as tuples in obj
# #~          dict_items([('Nag', 30), ('Vishnu', 20)])

# d.keys()    ## Returns a sequence of keys from dict 'd'

# d.values()  ## Returns a sequence of values from dict 'd'

# d.update(x) ## Adds all elements from dict 'x' to 'd'
# # print(d)

# d.pop('Key','Not Found') ## Removes the 'Nag' key and its value from the dict and returns only its value

# d.setdefault('Rag',50) ## If key found, its value returned. key not found, key & value stored in dict 'd'
# #~ {'Ram': 10, 'Vishnu': 50, 'Nag': 30, 'Rag': 50}

#% EXERCISE

#* Retrieve keys, values and key-value pairs from a dict

# dict = {'Name': 'Sushama', 'Id': 111, 'Salary': 500000}

# ## print entire dict

# print(dict)
#~ {'Name': 'Sushama', 'Id': 111, 'Salary': 500000}

# ## print only keys

# print('Keys in dict= ', dict.keys())
#~ Keys in dict=  dict_keys(['Name', 'Id', 'Salary'])

# ## print only values

# print('Values in dict= ',dict.values())
#~ Values in dict=  dict_values(['Sushama', 111, 500000])

# ## display both key and value pairs as tuples

# print('Items in dict= ',dict.items())
#~ Items in dict=  dict_items([('Name', 'Sushama'), ('Id', 111), ('Salary', 500000)])

#* Create a dict and find sum of values

# dict = eval(input('Enter elements in { }: '))   ## mind the gap between curly braces

## Find the sum of values

# s = sum(dict.values())
# print('Sum of all the values in dict is: ',s)

#* Create a dict from keyboard and display the elements

# x = {}

# print('How Many Elements? ', end=' ')

# n = int(input())        ## n indicates number of key-value pairs

# for i in range(n):
#     print('\nEnter key: ',end='')
#     k = input()             ## key is string
#     print('\nEnter its value: ',end='')
#     v = int(input())        ## value is an integer
#     x.update({k:v})         ## store key-value pair in dict
    
# ## Display the dict

# print('\nThe dictionary is: ', x)

#* Create a dict with Cricket players names & scores in match. Then retrieve runs by entering player's name.

# x = {}

# print('\nHow many players? ')
# n = int(input())

# for i in range(n):
#     print('Enter Players name: ')
#     k = input()         ## Player's name is string
#     print('Enter runs for this player: ')
#     v = int(input())
#     x.update({k:v})     ## Store kay-value pair in dict x

# ## Display player's name

# print('\nPlayers in this match: ')

# for names in x.keys():
#     print(names)
    
# ## Ask for a player's name from the keyboard

# print('\nEnter a players name to know his score: ',end='')
# name = input()

# ## find the runs made by this player

# runs = x.get(name, -1)
# if runs == -1:
#     print('\nPlayer did not play this match')
# else:
#     print('\n{} made runs: {}'.format(name, runs))

#@ Using for Loop with Dictionaries

#* Show usage of for loop to retrieve elements of dict

# colors = {'r': "Red", 'g': "Green", 'b': "Blue", 'w': "White"}

## Display only keys

# for k in colors:
#     print(k)
    
# ## Pass keys to dict and display values

# for k in colors:
#     print(colors[k])
    
# ## items() method returns key and value pair into k,v

# for k, v in colors.items():
#     print('key= {} value= {}'.format(k,v))

#% EXERCISE

#* Find the number of occurrences of each letter in a string using dictionary

str = 'Book'

## Take an empty directory

# dict = {}

# ## Store into dict each letter as key and its number of occurrences as value

# for x in str:
#     dict[x] = dict.get(x, 0) + 1
    
# ## Display key and value pairs of dict

# for k,v in dict.items():
#     print('Key = {}\t Its occurrences= {}'.format(k,v))    

#@ sorting Elements of a dictionary using lambdas

# colors = {10:'Red', 35:'Green', 15:'Blue', 25:'White'}

# ## sort the dictionary by keys

# c1 = sorted(colors.items(), key= lambda t: t[0])
# print(c1)

# c2 = sorted(colors.items(), key= lambda t: t[1])
# print(c2)


#@ Converting Lists into Dictionary

# countries = ["USA", "Bharat", "Germany", "France", "Norway"]
# cities = ['Washington', 'New Delhi', 'Berlin', 'Paris', 'Oslo']

## There are two steps involved to convert the lists into a dictionary.
## First step is to create a 'zip' class object by passing the two lists to zip()
## One or more sequences can be passed to zip() function.

# countries = ["USA", "Bharat", "Germany", "France", "Norway"]
# cities = ['Washington', 'New Delhi', 'Berlin', 'Paris', 'Oslo']

# ## Make a dictionary

# z = zip(countries,cities)

# d = dict(z)

# ## display key-value pairs from dictionary d

# print('{:15s} -- {:15s}'.format('Country', 'Capital'))

# for k in d:
#     print('{:15s} -- {:15s}'.format(k, d[k]))

#@ Converting Strings into a Dictionary

## Must follow 3  steps

## 1- Split the string into pieces where a comma is found using split() method
## 2- Then break string at equals (=) using for loop

#! for x in str.split(','):     First split
#!      y = x.split('=')        Second Split

## Now each piece of string is stored in Y. 

## Store above string pieces into a list

# lst = []

# lst.append(y)

## Convert the list into a dictionary using a dict() function

# d = dict(lst)

## This will give keys and values as strings. To get the values as int,

# for k,v in d.items():
#     d1[k] = int(v)

#% EXERCISE

#* Convert a string into key-value pairs and store them into a dictionary

# str = 'Shekhar=64, sushama=60, Ashish=36, Aakash=35'

# lst = []

# for x in str.split(','):
#     y = x.split('=')
#     lst.append(y)

# d = dict(lst)

# d1 = {}

# for k,v in d.items():
#     d1[k] = int(v)
    
# print(d1)

#@ Passing Dictionary to functions

#* Function to accept a dictionary and display its elements

# d = {'a':'Apple', 'b':'Book', 'c':'cook'}

# def fun(dict):
#     for i,j in dict.items():
#         print(i, '---', j)
        
  
# fun(d) 

#@ Ordered Dictionaries

#* Create a dictionary that does not change the order of entered elements

from collections import OrderedDict

d = OrderedDict()       ## d is an ordered dictionary

d[10] = 'A'
d[11] = 'B'
d[12] = 'C'
d[13] = 'D'

## Display the ordered dictionary

for i,j in d.items():
    print(i,j)
