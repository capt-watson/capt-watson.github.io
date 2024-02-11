
#% Regular expression is a string that contains special symbols and characters
#% to find and extract the information needed from the given data.

#* Also called 'regex'

#! In regular expression, 'r' is prefixed before the string to indicate that
#! it is a raw string. Escape chars such as '\n' are ignored in raw string.

#% The regular expression steps:

#~ Write the reg exp statement:

#% reg = r'\m\w\w'
 
## Here the 'm' means that the words starting with 'm' should be matched.

## Next char 'w' represents any chars in A to Z, a to z and 0 to 9.

## Since we used two '\w' chars, they represent any two chars after 'm'.

#~ Compile the above expression using compile() method

#% prog = re.compile(r'm\w\w')

## 'prog' represents an object that contains the regular expression.

#~ Run this expression on a string 'str' using the search() method or
#~ match() method.

#% str = 'cat mat bat rat'

#% result = prog.search(str)

## 'str' represents the string on which the regular expression will act.

#~ To display the result stored in 'result', group() method is called on the
#~ obj 'result'.

#% print(result.group())
#& mat

#! Execute the regular expression

# import re

# prog = re.compile(r'm\w\w')

# str = 'cat mat bat rat'

# result = prog.search(str)

# print(result.group())

#~ The above regular expression is generally written as:
# import re

# str = 'ban sun mop run'

# result = re.search(r'm\w\w', str)

# if result:                  ## if result is not None
#     print(result.group())
    
## The above expression will result only the first string containing 'm'.

## Will produce no output if None is found.

#! A program to create a regular expression to search for strings starting with 'm' and having
#! total of 3 chars using the findall() method

# import re
# str = 'man sun mop run'

# result = re.findall(r'm\w\w', str)
# print(result)

## The findall() method returns all resultant strings into a list

## The elements of the list can be displayed using for loop:

# for i in result:
#     print(i, end=' ')

#! A program to create a regular expression using the match() method to search for strings
#! starting with 'm' and having a total of 3 chars.

# import re

# str = 'ban dam sam man'

# result = re.match(r'm\w\w', str)

# print(result)
# print(result.group())

## match() method returns the resultant string only if it is found in the beginning of the string

#% re.split(r'\W+', str)

## 'W' represents any character that is not alpha numeric.
 
## Work of this regular expression is to split the string 'str' at the places where there is no
## alpha numeric character.

## '+' after 'W' represents to match 1 or more occurrences indicated by W.

#! A python program to create a regex to split into pieces where one or more non alpha numeric
#! chars are found.

# import re

# str = 'This; is the: "Core" Python\'s book'
# res = re.split(r'\W+', str)
# print(res)

#~ ['This', 'is', 'the', 'Core', 'Python', 's', 'book']

#& Sometimes, regex can also be used to find a string and then replace it with a new string.

#% sub(regular expression, new string, string)

#! A program to create a regular expression to replace a string with a new string

# import re

# str = 'Kumbhmela will be conducted at Prayag in India'
# res = re.sub(r'Prayag', 'Haridwar', str)
# print(res)

#! A Program to create a regular expression to retrieve all words starting with 'a' in a given
#! string.

# import re

# str = 'an apple a day keeps the doctor away'
# res = re.findall(r'a[\w]*', str)

# for i in res:
#     print(i, end=' ')
    
#~ an apple a ay away 
    
## Here, [\w]*  0 or more alphanumeric chars.

## a[\w]* represents the word should start with 'a' and may be followed by 0 or more alphanumeric
## chars.

# import re

# str = 'an apple a day keeps the doctor away'
# res = re.findall(r'\ba[\w]*\b', str)        

# for i in res:
#     print(i)
    
## \b before and after the words in the re will retrieve only the word and not the part of the words.
## \b will search for words starting after a space and ending before a space.

#! A program to create a regular expression to retrieve all words starting with a numeric digit:

# import re

# str = 'Classes will be held on 1st and 3rd week of every month'
# res = re.findall(r'\d[\w]*',str)
# for i in res:
#     print(i, end=' ')
# #~ 1st 3rd

## seq char \d will search only those words starting with digits (0 to 9)


#! A program to create a re to retrieve all words having 5 chars length

# import re

# str = 'one two three four five six seven eight nine ten thirteen 5 8 10 10000'
# res = re.findall(r'\b\w{5}\b',str)
# for i in res:
#     print(i, end=' ')
#~ three seven eight 10000 
    
## seq char \w{5} will pickup all words having only five chars or numbers in the string. Not more
## nor any less.

#! A program to create a regular expression to retrieve all words having 5 chars length using
#! search() method

# import re

# str =  'one two three four five six seven eight nine ten thirteen 5 8 10 10000'
# res = re.search(r'\b\w{5}\b', str)
# print(res.group())

## search() method returns only the first occurrence of the word meeting criteria.

#! A program to create a re to retrieve all the words having min 4 chars.

# import re

# str = 'one two three four five six seven eight nine ten thirteen 5 8 10 10000'
# res = re.findall(r'\b\w{4,}\b',str)     ## comma (,) means 4 or more characters
# for i in res:
#     print(i, end=' ')
#~ three four five seven eight nine thirteen 10000

#! A program to create a re to retrieve all the words having min 3 to 5 chars.

# import re

# str = 'one two three four five six seven eight nine ten thirteen 5 8 10 10000'

# res = re.findall(r'\b\w{3,5}\b',str)
# for i in res:
#     print(i, end=' ')
#~ one two three four five six seven eight nine ten 10000 


#! A program to create a re to retrieve only words having single digit from a string.

# import re

# str = 'one two three four five six seven eight nine ten thirteen 5 8 10 10000'

# res = re.findall(r'\b\d\b',str)
# for i in res:
#     print(i, end=' ')
# #~ 5 8 

#! A program to create a re to retrieve only words having double digits from a string.

# import re

# str = 'one two three four five six seven eight nine ten thirteen 5 8 10 10000'

# res = re.findall(r'\b\d\d\b',str)
# for i in res:
#     print(i, end=' ')
# #~ 10 


#! A program to create a re to retrieve the last word of a string, if it starts with t.

# import re

# str = 'one two three one two three'
# res = re.findall(r't[\w]*\Z', str)
# for i in res:
#     print(i, end=' ')
    
## \Z represents searching should be done at the end of the last word of a string meeting criteria

#@ Quantifiers in Regular Expressions

#! A program to create a re to retrieve the phone number of a person

# import re

# str = 'Shekhar Upadhyay: 9223588600'
# res = re.search(r'\d+',str)
# print(res.group())

## here the '+' quantifier keeps searching for single digits until all the digits in the string
## are found

#! A program to create a re to retrieve only name and not phone number of a person

# import re

# str = 'Shekhar Upadhyay 9223588600'
# res = re.search(r'\D+', str)
# print(res.group())

#! A program to create a re to find all words starting with 'an' or 'al'

# import re

# str = 'aarav aron aakash anil alfredo robert barber anne brittney andrew'
# res = re.findall(r'a[ln][\w]*',str)
# for i in res:
#     print(i, end=' ')
## Here a[nl] represents either 'n' or 'l' or both after 'a'.
    
#! A program to create a re to retrieve date of births from a string

# import re

# str = 'Aarav 10 17-01-2019, Ranveer 11 31-03-2018, Sita 12 5-09-2020'
# res = re.findall(r'\d{1,2}-\d{1,2}-\d{4}',str)
# for i in res:
#     print(i, end=' ')

## In the above re, {1,2} represents either 1 or 2 digits.

#! A program to create a regular expression to search wether a given
#! string is starting with 'He' or not.

# import re

# str = 'Hello World'
# res = re.search(r'^He', str)
# if res:
#     print('String starts with "He"')
# else:
#     print('String does not start with "He"')
    
#~ string starts with "He"
    
## The carat (^) symbol is useful to check if a string is starting
## with a sub string or not.

#! A program to search for a word at the ending of a string

# import re

# str = 'Quick Brown fox Jumps Over The Lazy Dog'
# res = re.search(r'Dog$',str)

# if res:
#     print('String ends with "Dog"')
# else:
#     print('String does not end with "Dog"')
    

#! A program to create a re to search at the ending of a string by
#! ignoring the case.

#! a program to create a regular expression to retrieve marks
#! and names from a given string

# import re

# str = 'Aarav got 99 marks, Sita got 98 marks, whereas Veronica got 85 marks'

# res = re.findall(r'\d{2}',str)
# for i in res:
#     print(i, end=' ')

# names = re.findall(r'[A-Z][a-z]*',str)
# for i in names:
#     print(i, end=' ')

## Square brackets represent a set of characters.


#! a program to create a re to retrieve the timings either 'am' or 'pm'.

# import re

# str = 'The meeting will be held either at 8am or 9am or 4pm or 5pm'

# res = re.findall(r'\dam|\dpm',str)
# for i in res:
#     print(i, end=' ')
    
    
 #@ Using Re on files

# import re

# f = open('mails.txt','r')

## Repeat for each line of the file

# for line in f:
#     res = re.findall(r'\S+@\S+',line)
#     if len(res) > 0:
#         print(res)

# f.close()

## \S+ represents several non white space chars
## \S+@\S+ represents several non white space chars before & after the @ sign


#! A program to retrieve data from a file using re and write data
#! into a new file

# import re

# f1 = open('salaries.txt','r')
# f2 = open('newfile.txt','w')

# for line in f1:
#     res1 = re.search(r'\d{4,}',line)    ## Extract id from f1
#     res2 = re.search(r'\d{4,}.\d{2}', line) ## Extract salary frm f1
#     print(res1.group(),res2.group())    
#     f2.write(res1.group()+'\t') ## Write id into f2
#     f2.write(res2.group()+'\n') ## Write salary into f2
# f1.close()
# f2.close()


#@ Retrieving information from a HTML file

# import urllib.request

# f = urllib.request.urlopen(r'file:///C:\Users\shekh\Projects\Python_Tutorials\Core_Python\breakfast.html')
## 'fil:///' indicates file URL scheme that is used to refer to files in the local
## computer system.

## Next word 'f/py' indicates the drive name 'f' and the sub directory 'py'.
## In this, we have the file breakfast.html. Once this file is open, we can read
## the data using read() method as:

## text = f.read()

## str = text.decode()  To decode HTML file byte strings data into normal strings.

#! A program to retrieve information from a HTML file using re.

import re

import urllib.request

## open the html file using urlopen() method

f = urllib.request.urlopen(r'file:///c|/Users/shekh/Projects/Python_Tutorials/Core_Python/breakfast.html')
## 'file:///' indicates that file is on local drive.
## <drivename> ('|') & all directory names should be preceded by '/' <forward />

## read data from the file object into byte string
text = f.read()

## convert the byte string into normal string
str = text.decode()

## apply regular expression on the string

result = re.findall(r'<td>\w+</td>\s<td>(\w+)</td>\s<td>(\d{2,}.\d\d)</td>',str)

## Display result
print(result)

## Display the items of the result

for item, price in result:
    print('Item = %-15s Price= %-10s' %(item, price)) 
## Here %-15s creates a field for 15 strings with converted value left adjusted  

f.close()

#~ [('Roti', '50.00'), ('chapati', '15.00'), ('Biryani', '200.00'), ('Omlette', '50.00'), ('PavBhaji', '120.00'), ('Paneer', '220.00'), ('IceCream', '70.00')]
#~ Item = Roti            Price= 50.00     
#~ Item = chapati         Price= 15.00     
#~ Item = Biryani         Price= 200.00    
#~ Item = Omlette         Price= 50.00     
#~ Item = PavBhaji        Price= 120.00    
#~ Item = Paneer          Price= 220.00    
#~ Item = IceCream        Price= 70.00  

## Deciphering - '<td>\w+</td>\s<td>(\w+)</td>\s<td>(\d{2,}.\d\d)</td>',str) =
## First - <td>\w+</td> means that there would be either letter or numbers between
##                      the first tag open and its close.

## \s                   means that there would be an space between the first tag
##                      close and the second tag open

## Second - <td>(\w+)</td> means that there would be second block of either letter
##                         or numbers or both between the tag  open & close.

## \s                   means that there would be an space between the first tag
##                      close and the second tag open.

## (\d{2,}.\d\d)        Here the first \d{2,}. means that there would be two or more
##                      digit numbers followed by a decimal(.)

##                      \d\d means that this group of number would consist of
##                      two single digits.