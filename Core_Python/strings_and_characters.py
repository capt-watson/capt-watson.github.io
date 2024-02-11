
## Triple single quotes (''') are used for representing a string 
## that occupies several lines.

# s1 = r"Welcome to\t Core Python\n Prgramming"
# print(s1)

## Here 'r' which means raw string is added before the string to
## nullify the effect of escape characters.

# name = u'\u0915\u094b\u0930 \u092a\u093E\u092F\u0925\u0964\u0928'
# print(name)

## The above unicodes will print Core Python in Hindi.
## A complete list of Unicode characters are saved in bookmarks
## under Python Programming

str = 'Core Python'

# n = len(str)
# i = 0

# while i<n:
#     print(str[i], end='')
#     i += 1
# print() ## puts cursor into the next line

#@ access in reverse order

# i = -1
# while i >= -n:
#     print(str[i], end='')
#     i -= 1

# print()

#@ Access in reverse order using negative index

# i = 1
# n = len(str)

# while i<= n:
#     print(str[-i], end='')
#     i += 1

    
#@ Use of for loop to access each element of string

# for i in str:
#     print(i, end=' ')
    
#@ To display string in reverse order, use slicing operation

# for i in str[: :]:
#     print(i, end=' ')
    
# for i in str[: :-1]:
#     print(i, end=' ')    ## step = -1 displays the string in reverse

#@ Slicing Operation

str = 'Core Python'

# a = str[0:9:1]

# print(a)

# a = str[0:9:2]
# print(a)

# a = str[-4:-1]  ## access fm str[-4] to str[-2] left to right
# print(a)

# a = str[-6:]
# print(a)

# a = str[-1:-4:-1]   ## access fm str[-1] to str[-3] left to right
# print(a)

# a = str[-1::-1]     ## access fm str[-1 to till end fm right to left
# print(a)

#@ Repetition Operator '*'

# str = 'Core Python'
# print(str*2)

## repeat 5th and 6th characters for 3 times
# s = str[5:7]*3
# print(s)

# s1 = 'Core'
# s2 = 'Python'
# s3 = s1+s2      ## cocatenate s1 and s2
# print(s3)

#@ in and not in operators

# str = input('Enter main string')
# sub = input('Enter string to be searched')

# if sub in str:
#     print(sub+' is found in main string')
# else:
#     print(sub+' not found in main string')
    
#@ Comparing Strings

# s1 = 'Box'
# s2 = 'Boy'
# if(s1 == s2):
#     print('Both are same')
# else:
#     print('Both are not same')
    
# if s1 < s2:     ## the string which comes 1st in dict order will have lower value
#     print('s1 less than s2')
# else:
#     print('s1 is greater than s2')
## Output as s1 less than s2 because x comes before y hence box is less than boy

#@ Removing spaces from a string

# name = '  Mukesh Deshmukh  '    ## Observe space before and after string
# print(name.rstrip())            ## Removes spaces at right

# print(name.lstrip())            ## Removes spaces at left

# print(name.strip())             ## Removes spaces from both sides

#@ Finding sub strings

# str = input('Enter main string')
# sub = input('Enter sub string')

# n = str.find(sub, 0, len(str))    ## search from 0th to last char in str

# if n == -1:         ## find() returns -1 if sub string not found
#     print('Sub string not found')
# else:
#     print('Sub string found at position: ', n+1)
    
    ## output as 3 because string 'this' contains 'is'
    ## We write n+1 as find() method starts counting from 0th position and we count
    ## from 1st position
    
    ## Find first occurance of sub string in a main string
    
# str = input('Enter main string')
# sub = input('Enter sub string')
    
#@ search from 0th to last character in string
    
# try:
#     n = str.index(sub, 0, len(str))
# except ValueError:
#     print('Sub string not found')
# else:
#     print('Sub string found at position: ', n+1)
    
## find() method and index() method returns only the first occurance of the sub string

#@ Display all positions of sub string in a given main string

# str = input('Enter main string')
# sub = input('Enter sub string')

# i = 0
# flag = False        ## Becomes True if sub string is found

# n = len(str)

# while i < n:
#     pos = str.find(sub, i, n)
#     if pos != -1:       ## if found, display its position
#         print('Found at position: ', pos+1)
#         i = pos+1       ## search from pos+1 position onwards
#         flag = True
#     else:
#         i = i+1         ## Search from next character onward
# if flag == False:
#     print('Sub string not found')
 
#@ Display all positions of sub string in a given main string

# str = input('Enter main string')
# sub = input('Enter Sub String')

# flag = False

# pos = -1

# n = len(str)

# while True:
#     pos = str.find(sub, pos+1, n)
#     if pos == -1:
#         break
#     print('Found at position: ', pos+1)
#     flag = True
# if flag == False:
#     print(' Sub string not found')
    
#@ Counting substring in a string

## stringname.count(substring, beg, end)

# str = 'Quick brown fox jumps over the lazy dog'

# n = str.count('fox')
# print(n)

# n =str.count('o', 0, len(str))
# print(n)

#@ Strings are Immutable

# str = 'abcd'
# print(str[0])

# str[0] ='x'

# s1 = 'one'
# s2 = 'two'

# s2 = s1  ## store s1 into s2

# print(s2)

# print(s1)

## Here name 'S2' will be adjusted to the object that is referenced by 's1'. But the
## original value of the 's2' that is 'two' is not altered. Since 'two' is not
## referenced, the garbage collector deletes that object from memory. 

# s1 ='one'
# s2 = 'two'

# id(s1)
# id(s2)
# s2 = s1
# id(s1)
# id(s2)

#@ Replacing a string with another string

## stringname.replace(old, new)

# str = 'That is a beautiful girl'
# s1 = 'girl'
# s2 = 'horse'
# str1 = str.replace(s1, s2)
# print(str1)

#@ Splitting & Joining Strings

## Split() method brakes string into pieces and returns output as a list.

## str.split(',')   Here comma is called seperator
## str.split(' ')   Here space is called seperator

# str = input('Enter numbers seperated by space')

# lst = str.split(' ')

#@ Display numbers from the list

# for i in lst:
#     print(i)
    
#@ To join group of strings

## seperator.join(str)

# str = ('One', 'Two', 'Three')       ## To join a tuple strings

# str1 = '-'.join(str)
# print(str1)

# str = ['apple', 'guava', 'grapes','mango']
# sep = ':'
# str1 = sep.join(str)
# print(str1)

#@ Changing case of string

## upper(), lower(), swapcase(), title()

## upper() method converts all characters into uppercase
## lower() method converts string into lower case.
## swapcase() method converts capital letters into small letters & vice versa
## title() method converts each word in the string to start with a capital letter

# str = 'Python is the future'
# print(str.upper())

# print(str.lower())

# print(str.swapcase())

# print(str.title())

#@ Checking starting and ending of a string

## str.startswith(substring)

## when a substring is found in the main string,it returns a TRUE.

# str = 'This is Python'

# print(str.startswith('This'))


## str.endswith(substring)

# str = 'This is Python'
# print(str.endswith('Python'))

#@ String Testing Methods

## isalnum()  isalpha()  isdigit()  isupper()  islower()  istitle()  isspace()

# str = 'Delhi9999'

# str.isalpha()       ## all characters are only alphabets

# str.isalnum()       ## all characters are alpha numeric

# str.isdigit()       ## all characters are digits

# str.islower()       ## all characters are in lower case

# str.isupper()       ## all characters are in upper case

# str.istitle()       ## Each word of string starts with capital letter

# str.isspace()       ## String contains only spaces

#@ formatting the string

## .format(values)

## it formats string with replacement fields. 
## Replacement fields are denoted by curly braces {} that contain names or indexes

id = 10
name = 'Shekhar'
sal = 49500.75

# str = '{}-{}-{}'.format(id, name, sal)

# print(str)

## we can also display message strings before every value:

# str = 'Id = {}\nName = {}\nSalary = {}'.format(id, name, sal)
# print(str)

## We can also mention order numbers in the replacement fields as 0, 1, 2, etc.

# str = 'Id = {0}\tName = {1}\tSalary = {2}'.format(id, name, sal)
# print(str)

## By changing the numbers in the replacement fields, can change order of value displd

# str = 'Id = {2}\tname = {0}\tSal = {1}'.format(id, name, sal)
# print(str)

## We can also mention names in the replacement fields

# str = 'Id = {One}, Name = {Two}, Salary = {Three}'.format(One=id, Two=name, Three= sal)
# print(str)

## Formatting specification starts with a colon(:) and after that, format is specified
## in the curly braces {}. Use 'd' or 'i' for decimal number, 'c' for characters, 's'
## for strings and 'f' or 'F' for floating point numbers.
## If no type specifier used, it would assume string datatype.

## 'x' or 'X' is used for hexadecimal number
## 'b' for Binary and 'o' for octal numbers.

# str = 'Id = {:d}, name = {:s}, salary = {:10.2f}'.format(id, name, sal)
# print(str)

## in the above example of 10.2f, 10 represents that salary should be displayed in
## 10 places. Among these 10 places, a decimal point and 2 fraction digits should be
## displayed.

## '<' means align left
## '>' means align right
## '^' means align in the center
## '=' means justified
## Any character in the replacement field represents that the field will be filled
## with that character.

# num = 5000
# print('{:*>15d}'.format(num))   ## No space should be left in replacement field

# print('{:*^15d}'.format(num))   ## center aligned

# n1 = 1000

# print('hexadecimal = {:.>15x}\nBinary = {:.<15b}'.format(n1, n1)) 

#! To print above hex and binary number with 0X and 0B, use # symbol

# print('Hexadecimal= {:.>#15x}\nBinary = {:.<#15b}'.format(n1, n1))

#@ Working with characters

# str = 'Sushama'

# ch = str[1]
# print(ch)

# print(str[1:2])

#@ Check if the given 'ch' character is a alphabetic character

#! isalpha()

#@ To know the type of character entered by the user

# str = input('Enter a character')

# ch = str[0]

## test ch

# if ch.isalnum():
#     if ch.isalpha():
#         print('It is an alphabet')
#         if ch.isupper():
#             print('It is a capital letter')
#         else:
#             print('It is a lower case letter')
#     else:
#         print('It is a numeric digit')
# elif ch.isspace():
#     print('It is a space')
# else:
#     print('It may be a special character')
    
#@ Sorting Strings

## Sort a group of strings into alphabetical order using
## sort() method and sorted() function

#! sort()

#% sort() method output will be without original order of string
#% Use sorted() to retain the original array even after sorting

# str = []

# n = int(input('How many strings?'))

## append strings to str array

# for i in range(n):
#     a = input('Enter string: ')
#     print('Entered string: ',a)
#     str.append(a)
    
    
# str1 = sorted(str)

# print('Sorted List: ')
# for i in str1:
#     print(i)
    
#@ Searching in the string

# str = []

# n = int(input('How many string?'))

# for i in range(n):
#     a = input('Enter string: ')
#     print('Enter String: ', a)
#     str.append(a)
    
## Ask for input to search

# s = input('Enter the string to search: ')
# print('Enter the string to search: ',s)

## linear search or sequential search

# flag = False
    
# for i in range(len(str)):
#     if s == str[i]:
#         print('Found at: ',i+1)
#         flag = True
# if flag == False:
#     print('String not found')

#@ Finding number of Characters

# str = input('Enter a string: ')

# i = 0
# for s in str:
#     print(str[i], end='')
#     i += 1
# print('\nNo. of Characters: ',i)

#@ Finding number of Words in a string

# str = input('Enter a String: ')

# i=c=0       ## c is counter

# Flag = True     ## This becomes false when no space is found

# for s in str:
    ## Count only when no space previously
    # if Flag == False and str[i] == ' ':
    #     c += 1
        
    ## if space is found, take flag as true
#     if str[i] == ' ':
#        Flag = True
#     else:
#         Flag = False
#     i += 1
# print('No. of Words: ', c+1)

#@ Inserting sub string into a string
  
# str = input('Enter a string: ')
# sub = input('enter a sub string: ')

# n = int(input('Enter position number: '))

# n -=1   ## Decrease n by 1 to insert at correct position

#     ## find the number of char in str, sub
# l1 = len(str)
# l2 = len(sub)

#     ## Take another string as a list
# str1 = []

#     ## append 0 to n-1 char from str to str1
# for i in range(n):
#     str1.append(str[i])
    
#     ## append sub string to str1
    
# for i in range(l2):
#     str1.append(sub[i])
    
#     ## append remaining characters from str to str1
    
# for i in range(n, l1):  ## start from n and go up to l1
#     str1.append(str[i])
    
#     ## Convert individual char of list into string using join()

# str1 = ''.join(str1) 

#     ## Display new string
    
# print(str1)