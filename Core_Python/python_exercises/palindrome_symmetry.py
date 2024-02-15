## Check if string is:

#! Symmetrical or palindrome

# def palindrome(a):
#     ## Finding start, mid and end index of string
#     start = 0
#     mid = (len(a)-1)//2
#     last = len(a)-1

#     flag = True
    
#     ## A loop till the mid of the string
#     while start <= mid:
#         ## comparing letters from right with letters from left
#         if a[start] == a[last]:
#             start += 1
#             last -= 1
#         else:
#             flag = False
#             break
#         ## checking the flag variable to see if the string is palindrome or not
#     if flag == True:
#         print('The string is Palindrome')
#     else:
#         print('The string is not Palindrome')

# def symmetry(a):
#     n = len(a)
#     flag = True
#     ## check if the string's length is odd or even
#     if n % 2:
#         mid = n//2+1
#     else:
#         mid = n//2
        
#     start1 = 0
#     start2 = mid
    
#     while start1 < mid and start2 <n:
#         if a[start1] == a[start2]:
#             start1 = start1 + 1
#             start2 = start2 + 1
#         else:
#             flag = False
#             break
        
#     ## Checking flag variables to see if the string is symmetrical or not
#     if flag == True:
#         print('The given string is Symmetrical')
#     else:
#         print('The given string is not Symmetrical')
        
# string = input('Enter a string: ')
# palindrome(string)
# symmetry(string)

#! Or using slicing method

# string = input('Enter a string: ')
# half = int(len(string)/2)

# first_str = string[:half]
# second_str = string[half:]

# ## symmetric
# if first_str == second_str:
#     print('String is symmetrical')
# else:
#     print('String is not symmetrical')

# ## Palindrome

# if first_str == second_str[::-1]:
#     print('string is Palindrome')
# else:
#     print('String is not a Palindrome')

#! Using a re module

# import re

# string = input('Enter a string: ')
# reverse_string = string[::-1]

# if string == reverse_string:
#     print('String is symmetrical')
# else:
#     print('String is not symmetrical')
    
    
# if re.match(r'^(\w+)\Z',string) and string == string[::-1]:
#     print('String is a Palindrome')
# else:
#     print('String is not a Palindrome')


#! Using reversed() function

str = 'malayalam'

x = list(str)

y = list(reversed(x))


if y == x:
    print('String is a Palindrome')
else:
    print('String is not a Palindrome')
    