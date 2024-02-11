
#@ Opening a file

#! file handler (f) = open('file name', 'open mode', 'buffering')

#! f = open('myfile.txt'. 'w')

#* Here the file name is the name of the actual file to be opened

#* 'Open Mode' represents the purpose of opening the file.

#% File opening Modes:

#% w - Write. If data already exists, delete old data & write new data

#% r - Read only. Pointer is placed at the beginning of file.

#% a - Append data to file. Pointer placed at the end of file.

#% w+ - Write & then read data. Prev data will be deleted.

#% r+ - Read & Write data into file. Prev data will not be deleted.

#% a+ - Append & read data. Pointer will be at the end of the file.

#% x -  Open file in exclusive creation mode. File creation fails if
#%      file already exists.


## if we attach 'b' to the 'file open mode char', they represent
## modes for binary files.
## e.g. wb, rb, ab, w+b, r+b and a+b are the modes of the binary files.

#@ Closing a file

#~ A file which is open must be closed using 'close()' method.

#! f.close()    

## f.close() means that the file object 'f' is closed. In other words, the obj 'f' is
## deleted from the memory.

#! Program to create a text file to store individual characters.

## creating a file to store characters

# f = open('myfile.txt', 'w')

# ## enter characters from keyboard

# str = input('Write something: ')

# ## write the string into the file

# f.write(str)

# ## closing the file

# f.close()

#! Python program to read characters from a text file

# f = open('myfile.txt','r')

# ## read all characters from the file

# str = f.read()    ## if a number is entered in read(), then only that many char printed

# ## Display it on the screen

# print(str)

# ## closing the file

# f.close()

# #@ Working with Text files containing strings

# #! Program to store a group of strings into a text file

# ## open the file for writing data

# f = open('myfile.txt', 'w')

# ## Enter strings from keyboard

# print('Enter text (@ at end): ')

# while str != '@':
#     str = input()   ## Accept string into str
    
#     ## write the string into file
    
#     if str != '@':
#         f.write(str+'\n')
        
# ## closing the file

# f.close()

#! Program to read all the strings from the text file & display it

# f = open('myfile.txt', 'r')

# print('This file\'s content are: ')

# str = f.read()
# print(str)

# f.close()

#% To place the file handler to the beginning of the file using
#% seek() method as:

#! f.seek(offset, fromwhere)

#~ Here, 'offset' represents how many bytes to move. 'fromwhere' 
#~ represents from which position to move. 

#! fromwhere = 0 represents from the beginning of file.
#! fromwhere = 1 represents from current position.
#! fromwhere =  2 represents from the ending of the file.

#& Python program to append data to an existing file and then display
#& the entire file.

# f = open('myfile.txt', 'a+')

# print('Enter Text to append with @ at the end: ')

# while str != '@':
#     str = input()
    
#     if str != '@':
#         f.write(str+'\n')
        
# ## Move the file pointer to the beginning of the file

# f.seek(0,0)     ## means 0 offset and start from the beginning

# ## read strings from the file

# print('The contents of the file are: ')

# str = f.read()
# print(str)

# f.close()


#@ Knowing whether a File Exists or Not

#! Python program to know if the desired file exists or not

# import os, sys

# fname = input('Enter the desired file\'s name: ')

# try:
#     if os.path.isfile(fname):
#         f = open(fname, 'r')
#         print('The file\'s contents are: ')
#         str = f.read()
#         print(str)
#     else:
#         print(fname+' does not exist')
#         sys.exit()
# except SystemExit:
#     print('')
# finally:      
#     f.close()


#! A program to count number of lines, words and characters in a
#! text file.

# import os, sys

# try:
#     fname = input('Enter file name: ')

#     if os.path.isfile(fname):
#         f = open(fname, 'r')
# ## Initialize the counters to 0
#         cl = cw = cc = 0  ## cl line count, cw=word count, cc=char count

# ## read line by line fom the file
#         for line in f:
#             words = line.split() ## words is a list containing all words of a line
#             cl += 1             ## for each line, add 1 to cl 
#             cw += len(words)    ## for each line, add number of words to cw
#             cc += len(line)     ## for each line, add number of chars to cc
#             print('Number of lines: ',cl)
#             print('Number of Words: ',cw)
#             print('Number of Characters: ',cc)
#     else:
#         print(fname+' - Requested file does not exist')
#         sys.exit()

# except SystemExit:
#     print('')

# finally:
#     f.close()

#@ Working with Binary Files

#! A Python program to copy an image file into another file

## Open the file into binary mode

# f1 = open('C:\\Users\\shekh\\Desktop\\pexels.jpg', 'rb')    ## Must use two '\\'
# f2 = open('new.jpg', 'wb')

# ## read bytes from f1 and write into f2

# bytes = f1.read()
# f2.write(bytes)

# ## Close files
# f1.close()
# f2.close()

#@ The 'with' statement

#* It is used while opening the file.

#* It takes care of closing a file which is opened by it.

#* In case of Exception also, 'with' statement will close the file before the exception
#* is handled.

#! format:
#% with open('filename', 'openmode') as fileobject:

#! A Python program to use 'with' to open a file and write some strings into the file.

# with open('Sample.txt', 'w') as f:
#     f.write('How are you Darling?\n')
#     f.write('Give me a Kiss\n')

#! A python program to use 'with' to open a file and read data from it.

# with open('Sample.txt', 'r') as f:
#     x = f.read()
#     print(x)
    
#@ Pickle in Python

#! To store structured data into a file, we need to create a class 'Employee' with the
#! instance variables id, name and sal as shown here.

# class Emp:
#     def __init__(self,id, name, sal):
#         self.id = id
#         self.name = name
#         self.sal = sal
        
#     def display(self):
#         print('{:5d} {:20s} {:10.2f}'.format(self.id, self.name, self.sal))
    
#% We now create an object to this class and store actual values into that object.

#% Later, this obj should be stored into a binary file in the form of bytes. This is
#% called 'pickle or serialization'.

#! Pickling is done using the dump() method of 'pickle' module as:

## Create an object to Emp class

#! A python program to pickle Emp class objects.

# import Emp, pickle

# # open emp.dat file as binary file for writing

# f = open('emp.dat', 'wb')
# n = int(input('How many Employees: '))

# for i in range(n):
#     id = int(input('Enter id: '))
#     name = input('Enter name: ')
#     sal = float(input('Enter salary: '))
    
#     ## Create Emp class object
    
#     e = Emp.Emp(id, name, sal)
    
#     ## store the object e into the file f
#     pickle.dump(e, f)
    
# ## close the file
# f.close()

# #! Python program to unpickle Emp class

# import Emp, pickle

# ## open the file to read objects

# f = open('Emp.dat', 'rb')

# print('Employee details: \n')

# while True:
#     try:
#         ## read objects from file f
#         obj = pickle.load(f)
#         ## display the contents of employee obj
#         obj.display()
#     except EOFError:
#         print('\nEnd of File reached...')
#         break
# ## close the file
# f.close()

import Emp, pickle

## open emp.dat file as binary file for writing

# f = open('emp.dat', 'wb')
# ## n = int(input('How many Employees: '))

# while input('Enter more employee details? Enter - Yes/No: ') != 'No':
#     id = int(input('Enter id: '))
#     name = input('Enter name: ')
#     sal = float(input('Enter salary: '))
    
#     ## Create Emp class object
    
#     e = Emp.Emp(id, name, sal)
    
#     ## store the object e into the file f
#     pickle.dump(e, f)
    
# ## close the file
# f.close()

# f = open('Emp.dat', 'rb')

# print('Employee details: \n')

# while True:
#     try:
#         ## read objects from file f
#         obj = pickle.load(f)
#         ## display the contents of employee obj
#         obj.display()
#     except EOFError:
#         print('\nEnd of File reached...')
#         break
# ## close the file
# f.close()

#@ Python program to create a binary file and store a few records

## Create cities.bin file with cities name

# reclen = 20

# with open('cities.bin', 'wb') as f:
    
#     while input('Enter details? y or n') != 'n':
#         city = input('Enter City Name: \n')
#         ln = len(city)
#         city = city + (reclen - ln)*' '
#         city = city.encode()
#         f.write(city)
        
        
# with open('cities.bin', 'rb') as f:
#     n = int(input('Enter record number: '))
#     f.seek(reclen*(n-1))    ## move the cursor to new position
#     str = f.read(reclen)    
#     print(str.decode())    

#! A program to search for city name in the file and display record
#! number that contains the city name

# import os

# reclen = 20         #! Record Length

# ## find the size of the file

# size = os.path.getsize('cities.bin')
# print('size of file = {} bytes'.format(size))

# ## find number of records in file

# n = int(size/reclen)
# print('No of records = {}'.format(n))

# ## Open the file in binary mode for reading

# with open('cities.bin', 'rb') as f:
#     name = input('Enter city name: ')

# ## convert name into a binary string
#     name = name.encode()

# ## Position represents the position of the pointer in the file

#     position = 0

# ## found becomes True if city is found in the file
#     found = False

#     for i in range(n):
#         f.seek(position)
#         ## read 20 characters
#         str = f.read(20)
#         if name in str:
#             print('Name found at record no.: ',(i+1))
#             found = True
#         ## go to the next record
#         position += reclen
# if not found:
#     print('City name not found!')


#! Program to update or modify a record in a binary file.

# import os

# reclen = 20

# size = os.path.getsize('cities.bin')
# print('File size is {} bytes'.format(size))

# n = int(size/reclen)
# print('Number of records in this file: {}'.format(n))

# with open('cities.bin', 'r+b') as f:     #! r+b means r+ & b i.e. read & write in binary
#     name = input('Enter city name: ')
#     name = name.encode()

#     newname = input('Enter New name: ')
#     ## find the length of the new name
#     ln = len(newname)
#     ## add spaces to make its length to be 20
#     newname = newname + (reclen-ln)*' '
#     newname = newname.encode()

#     position = 0

#     found = False

#     for i in range(n):
#         ## place the pointer at position
#         f.seek(position)
#         str = f.read(reclen)    ## Will read every time 20 chars
#         ## if found
#         if name in str:
#             print('Updated record no.: ',i+1)
#             ## Go back 20 bytes from current position
#             f.seek(-20, 1)
#             ## update the record
#             f.write(newname)
#             found = True    ## will jump out of the for loop
#         position += reclen        
#     if not found:
#         print('City not found')
        
#! Python program to delete a specific record from the binary file

# import os

# reclen = 20

# size = os.path.getsize('cities.bin')

# n = int(size/reclen)

# f1 = open('cities.bin','rb')

# f2 = open('file2.bin', 'wb')

# city = input('Enter city name to delete')

# ln = len(city)

# city = city + (reclen - ln)*' '

# city = city.encode()

# for i in range(n):
#     ## read 1 record from f1 file
#     str = f1.read(reclen)
#     ## if it is not city name, store it into f2 file
#     if str != city:
#         f2.write(str)
# print('Record deleted...')

# f1.close()
# f2.close()

# ## delete cities.bin file
# os.remove('cities.bin')

# # rename fil2.bin as cities.bin
# os.rename('file2.bin', 'cities.bin')

#@ Random Accessing of Binary Files using mmap

#! mmap == 'Memory Mapped File'

#! Python program to create phone book with names and phone numbers

# with open('phonebook.dat', 'wb') as f:
    
#     ## write data into the file
    
#     while input("Enter 'Y' to proceed or '#' to quit: ") != '#':
#         name = input("Enter name: ' or '#' to quit")
#         phone = input('Enter Phone number: ')
#         name = name.encode()
#         phone = phone.encode()
#         ## write data into the file
#         f.write(name+phone)
        
#! Program to use mmap and performing various operations on binary file

# import mmap, sys

# ## Display a menu
# print(' 1 to Display all the entries')
# print(' 2 to Display phone number')
# print(' 3 to modify an entry')
# print(' 4 to exit')

# ch = input('your choice: ')
# if ch == '4':
#     sys.exit()

# with open('phonebook.dat','r+b') as f:
#     ## memory-map the file, size 0 means whole file
#     mm = mmap.mmap(f.fileno(), 0)

#     ## Display entire file
#     if ch == '1':
#         print(mm.read().decode())

#     ## Display phone number
#     if ch == '2':
#         name = input('Enter name: ')

#         ## find position of name
#         n = mm.find(name.encode())

#         ## go to the end of the name
#         n1 = n+len(name)

#         ## Display the next 10 bytes
#         ph = mm[n1:n1+10]
#         print('Phone number: ', ph.decode())

#     ## modify phone number
#     if ch == '3':
#         name = input('Enter name to modify phone number: ')        
#         ## find position of name
#         n = mm.find(name.encode())
#         n1 = n + len(name)
        
#         ## Enter new phone number
#         ph1 = input('Enter new phone number: ')
        
#         ## The old phone number is 10 bytes after n1
#         mm[n1: n1+10] = ph1.encode()
        
#     ## close the map
#     mm.close()
    
#@ Zipping and Unzipping Files
    
#! zipfile contains ZipFile class that helps us zip or unzip a file contents.
    
#! A program to compress the contents of files
    
# from zipfile import ZipFile, ZIP_DEFLATED

# f = ZipFile('test.zip','w', ZIP_DEFLATED)   ## ZIP_DEFLATED is an attribute
# # An empty zip file is now created

# # Add some files which are to be zipped
    
# f.write('file1.txt')
# f.write('file2.txt')
# f.write('file3.txt')

# ## close the zip file
# print('test.zip file created')

# f.close()


#! Program to unzip the contents of the files that are available in
#! zip file

# from zipfile import ZipFile

# ## Open the zip file
# z = ZipFile('test.zip','r')

# ## extract all the files which are in the zip file

# z.extractall()

# with open('file3.txt','r') as f:
#     str = f.read()
#     print(str)
    

#@ working with Directories

# import os

# ## get current working directory

# current = os.getcwd()
# print('Current working Directory: ',current)

#! A program to create a sub directory and then sub-sub directory in the current directory

# import os

# ## Create a sub directory by the name  mysub
# os.mkdir('mysub')

# ## Create a sub-sub directory by the name mysub2

# os.mkdir('mysub/mysub2')


#! Program to use the makedirs() function to recursively create sub and sub-sub directories

# import os

# os.makedirs('newsub/newsub2')

## In the above example, we have created newsub2 sub directory without
## first creating newsub directory and then creating newsub2 directory.
## newsub2 has been created in a single step using makedirs() function

#! Program to change CWd to another existing directory

# import os

# ## Change to newsub2 directory

# goto = os.chdir('newsub/newsub2')

# goto = os.chdir('..')       ## To go back to previous directory

# current = os.getcwd()
# print('Current directory= ',current)


#! A program to remove a sub directory that is inside another
#! directory

# import os

# os.rmdir('newsub/newsub2')

#! A program to remove a group of directories in the path.

# import os

# os.removedirs('mysub/mysub2')   ## Removes both the directories

#! A program to rename a directory

# import os

# os.rename('num', 'new_num')  ## 'num' dir old name, 'new_num' newname

 #% To know the contents of given directory, foll syntax is used:
 
 #& os.walk(path, topdown=True, oneerror=none, followlinks= False)
 
 ## Here path represents directory name. for current dir, use dot (.)
 
 ## if 'topdown' is true, the directory and its subdirectories are
 ## traversed in top to down manner. If False, then traversal will be in bottom-up manner.
 
 ## 'oneerror' represents what to do when an error is detected.
 
 ## By default, walk() will not walk down into symbolic links that resolve to directories
 
 #! A Program to display all contents of the current directory
 
# import os
 
# for dirpath, dirnames, filenames in os.walk('.'):
#     print('Current path: ',dirpath)
#     print('Directories: ',dirnames)
#     print('Files: ',filenames)
#     print()         ## All the above output will be printed with a spacing of one line
    
# #! To display content of only one directory, use following:

# os.walk('mysub')    ## Will display the contents of only 'mysub' directory

#@ Running other programs from Python Program

#! A program to display Python program files available in the current directory

import os

## execute dir command of DOS operating sys

os.system('dir *.py')   ## Display all the files names having py suffix.

#% Note that the output of the os.system can only be viewed in terminal
