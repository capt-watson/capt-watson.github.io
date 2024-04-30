
from pathlib import Path

import json

# path = Path('test1.txt')

# contents = path.read_text().rstrip()

#! pathlib that makes it easier to work with files and directories, no matter which operating system you or your program’s users are working with. Path object that points to a file.

#! .rstrip() method removes any trailing whitespace from the string. This approach is called method chaining,

# print(contents) 
#~ 3.1415926535
8979323846
2643383279


#! The splitlines() method returns a list of all lines in the file

# contents = path.read_text()

# lines = contents.splitlines()

# for line in lines:
    # print(line)
    
#! Following method will join all lines together into a single string.

#% Difference between the following method and join() method is that the following method will join all lines together without any separators whereas join() method will require separator to be specified.

# pi_string = ''

# for line in lines:
#     pi_string += line
    
# print(pi_string)

# print(len(pi_string))

## len displays the total number of chars of the string including 3 and a decimal place.

#~ 3.141592653589793238462643383279
#~ 32

#! When Python reads from a text file, it interprets all text in the file as a string. If you read in a number and want to work with that value in a numerical context, you’ll have to convert it to an integer using the int() function or a float using the float() function.

# lines = contents.splitlines()
    
# pi_string = ''
    
# for line in lines:
#     pi_string += line.lstrip()
    
# print(f"{pi_string[:51]}...")

#! The lstrip(s) (left strip) function removes leading whitespace (on the left) in the string. The rstrip(s) (right strip) function removes the trailing whitespace (on the right). The strip(s) function removes both leading and trailing whitespace.

#% Replacing character of word of a string

# msg = "I really like dogs"

# print(msg.replace('dog', 'cat'))    ## replaces complete word

# print(msg.replace('d', 'c'))        ## replaces only the given character


#^ Writing to a text file

# path = Path('test2.txt')

# path.write_text('I love programming')

#! To write more than one line to a file, you need to build a string containing the entire contents of the file, and then call write_text() with that string.

contents = 'I love programming. \n'
contents += ' I love using ML and AI. \n'
contents += 'I love working with data. \n'

# path = Path('test2.txt')

# path.write_text(contents)

#^ Using try-except Blocks

# try:
#     x = 5/0
#     print(x)

# except ZeroDivisionError:
#     print("You can't divide by zero")

#! if more codes were to follow the try-except block, the program would continue to run next codes after printing the except block message.

#! The try-except block is a good way to handle errors in your program without stopping the program entirely.

#^ Using Exceptions to prevent crashes

# print("Give me two numbers and I'll divide them.\n")
# print("Enter 'q' to quit.\n ")


# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         print("Exiting the program")
#         break
#     second_number = input("\nSecond number: ")
#     if second_number == 'q':
#         print("exiting the program")
#         break
#     try:
#         answer = int(first_number)/int(second_number)
#     except ZeroDivisionError:
#         print("\nYou are not allowed to divide by zero!")
#     except ValueError:
#         print("\nPlease enter only numbers.")
#     else:
#         print(answer)
        
#! File not found error

# path = Path("alice.txt")
# try:
#     contents = path.read_text(encoding='utf-8')
# except FileNotFoundError:
#     print(f"Sorry, the file {path} does not exist.")

#! UTF-8 is a character encoding that represents text in a way that is compatible with most computers and devices. it is also the default encoding for Python strings.

#^ Analyzing Text

# path = Path("test2.txt")

# path.write_text(contents)

# def count_words():   
#     """Storing content of the file in 'utf-8' format"""
#     filenames = ['alice.txt', 'test1.txt','test3.txt', 'test2.txt']        
#     for file in filenames:
#         try:
#             path = Path(file)
#             contents = path.read_text(encoding='utf-8')
#         except FileNotFoundError:
#             print(f"file {path} doesn't exist")
#         else:
#             """Count the number of words in the file"""
#             words = contents.split()  ## use split() to produce a list of all the words in the book
#             num_words = len(words)
#             print(f"The file {path} contains total {num_words} words.")
    
# count_words()


# def value_errors():
#     usr1, usr2 = input('Enter two numbers: ').split()
#     try:
#         answer = int(usr1) + int(usr2)
#     except ValueError:
#         print('Please enter only whole numbers!')
#     else:
#         print(f"The sum of the given numbers is: {answer}")

# value_errors()


# flag = True

# while flag:
#     usr1, usr2 = input('Enter two numbers: ').split()
#     try:
#         answer = int(usr1) + int(usr2)
#     except ValueError:
#         print('Please enter only whole numbers!')
#     else:
#         print(f"The sum of the given numbers is: {answer}")
#         flag = False

# line = "Row, row, row your boat"

# line.count('row')

# line.lower().count('row')       ## converts 'Row' to 'row' and then counts total number of 'rows'.


#^Using json.dumps() and json.load()

#% json.dumps() stores the data into a file

#! json.loads() loads the into the memory from the file.

# num = [2, 3, 5, 7, 11, 13]

# path = Path('num.json')  ## Use the file extension .json to indicate that the data in the file is stored in the JSON format.

# contents = json.dumps(num) ## use the json.dumps() function to generate a string containing the JSON representation of the data.

# path.write_text(contents)  ## write it to the file using the write_text()

# path = Path('num.json')  ## make sure to read from the same file we wrote to

# contents = path.read_text()  ## file is just a text file with specific formatting, read it with the read_text() method

# num = json.loads(contents)  ## pass the contents of the file to json.loads() to convert it back into a list. This function takes in a JSON-formatted string and returns a Python object (in this case, a list)

# print(num)

#^ Another example of saving data

# path = Path('username.json')    ## create the file & save the path into 'path' variable

# username = input('Enter your User Name: ')  

# print(f"Hello {username}, I'll remember you when you come back\n")

# contents = json.dumps(username)  ## Encode username into json format and pass it to content variable

# path.write_text(contents)   ## write the contents to the 'path' variable 



# path = Path('username.json')        ## get the username.json file content to the path variable. 

# contents = path.read_text()         ## apply read_text() method on the path variable & save output to contents variable.

# username = json.loads(contents)     ## Now decode contents file from json format back to regular text format n save in username

# print(f"Hello {username}, Welcome back")



# def greet_user():
#     """Greet User by name"""
#     path = Path('username.json')

#     if path.exists():
#         contents = path.read_text()
#         username = json.loads(contents)
#         print(f"Welcome back, {username}!")
#     else:
#         username = input('Enter your Name: ')
#         contents = json.dumps(username)
#         path.write_text(contents)
#         print(f"Hello {username}, we'll remember when you come back")

# greet_user()


def get_stored_user_info(path):
    """Checks & returns stored user_dict if available"""
    if path.exists():
        contents = path.read_text()
        user_dict = json.loads(contents)
        return user_dict
    
    
def get_new_user_info(path):
    """Creates and returns a new user_dict"""
    username = input("Please enter your name")
    age = input("Please enter your age")
    city = input("Please enter your city")
    
    user_dict = {
        'username' : username,
        'age' : age,
        'city' : city,
    }
    contents = json.dumps(user_dict)
    path.write_text(contents)
    return user_dict    ## user_dict is what we want from this function
    
    
def greet_user():
    """Assigns/Creates path if it doesn't exist"""
    path = Path('user_info.json')
    user_dict = get_stored_user_info(path)  ## gets user_dict from get_stored_info_path function
    if user_dict:                           ## if user_dict exists
        verify = input("Please enter your username")
        if verify == user_dict['username']:
            print(f"Welcome back {user_dict['username']}!")
            print(f"Your age is {user_dict['age']}")
            print(f"You are from {user_dict['city']}")
        else:
            print(f"Your username {verify} doesn't exist")
            user_dict = get_new_user_info(path)
            print(f"Hello {user_dict['username']}, we'll remember when you come back")

greet_user()



#^ favorite number question:

# def get_stored_number(path):
#     """Get stored user number if available"""
#     if path.exists():                   ## if file exists
#         contents = path.read_text()     ## read the contents
#         number = json.loads(contents)   ## convert from json to txt file
#         return number                   ## return the number to function

# def get_new_number(path):
#     """prompt for new number"""
#     number = input('Enter your favorite number: ') ## prompt for new number
#     contents = json.dumps(number)                  ## convert the number to json
#     path.write_text(contents)                      ## write the contents to file
#     return number                                  ## returns number to function

# def greet_user():
#     """Give user his/her favorite number"""
#     path = Path('number.json')          ## First step is to create a path to file
#     number = get_stored_number(path)    ## second step to call get_stored_num function
#     if number:                          ## if number exist
#         print(f"Your favorite number is {number}")  ## print number
#     else:
#         number = get_new_number(path)   ## else call get_new_number function
#         print(f"I'll remember your {number} when you come next time.")
        
# greet_user()