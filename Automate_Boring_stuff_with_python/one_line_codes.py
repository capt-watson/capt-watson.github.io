import functools
import math
from collections import Counter

#^ Swap Variables

a= 5
b =10

a,b = b,a

# print('a:',a)
# print('b:',b)

#~ a: 10
#~ b: 5


#^ check if given string is Palindrome

string = 'malayalam'

is_palindrome = string == string[::-1]

# print(string, 'is', is_palindrome)

#~ malayalam is True


#^ Calculate the factorial of a number

n= 5

factorial = 1 if n == 0 else functools.reduce(lambda x,y : x*y, range(1,n+1))

# print(factorial)

#~ 120

## In the above example, lambda will take x & y as arguments and loop x*y for range of numbers from 1 to 5


#^ check if a number is prime

n = 5

is_prime = n > 1 and all(n % i != 0  for i in range(2,int(n**0.5)+1))

# print(is_prime)

n = 6

is_prime = n > 1 and all(n % i != 0  for i in range(2,int(n**0.5)+1))

# print(is_prime)

#~ True
#~ False


#^ check if a list is sorted

my_list = [1,2,3,4.5,6]

is_sorted = all(my_list[i] <= my_list[i+1] for i in range(len(my_list)-1))

# print(is_sorted)

#~ True

my_list = [1,2,5,4.3,6]

is_sorted = all(my_list[i] <= my_list[i+1] for i in range(len(my_list)-1))

# print(is_sorted)

#~ False


#^ Generate a list of squared numbers

n = 5

squared_numbers = [i**2 for i in range(1, n+1)]

# print(squared_numbers)

#~ [1, 4, 9, 16, 25]


#^ Remove white spaces from a string

my_string = 'string with White  spaces'

no_whitespace = my_string.replace(' ','')

# print(no_whitespace)


#^ Filer even numbers from a list

my_list = [1,2,3,4,5,6,7,8,9]

even_numbers = [i for i in my_list if i % 2 == 0]

# print(even_numbers)



#^ Flatten a list of lists

my_list = [[1,2],[3,4],[5,6]]

flattened_list = [item for sublist in my_list for item in sublist]

# print(flattened_list)

#~ [1, 2, 3, 4, 5, 6]



#^ Find the most common element in a list

my_list = [1,1,1,1,1,2,2,2,3,3,3,3]

most_common = max(set(my_list), key=my_list.count)

# print(most_common)

#~ 1

## In the above example, set() function creates a set.
## The set() function removes duplicates from a list.
## The max() function returns the maximum value in a set.
## The key=my_list.count function returns the key with the maximum value.



#^ Remove duplicates from a list while preserving order

my_list = [1,1,1,1,1,3,3,3,3,2,2,2]

no_duplicates = list(dict.fromkeys(my_list))

# print(no_duplicates)

## fromkeys() method in Python creates a new dictionary from a sequence and a specified value.
## each element from the given list becomes key of dict. As no values provided, the default values becomes None.
## The sequence can be a list, a tuple, a string, or a set.

#~ [1, 3, 2]



#^ Find the least common multiple (LCM) of two numbers

a = 4
b = 5

lcm = abs(a*b) // math.gcd(a,b)

# print(lcm)

#~ 20



#^ Anagram

s1 = 'below'
s2 = 'elbow'

# print('anagram') if Counter(s1) == Counter(s2) else print('not an anagram')

## Counter is an unordered collection where elements are stored as Dict keys and their count as dict value.

## #* second method

# print('anagram') if sorted(s1) == sorted(s2) else print('not an anagram')



#^ Binary to decimal

decimal = int('1010',2)
# print(decimal)

#~ 10

# c = s1.encode()
# print(c)


#^ sum of two consecutive numbers

n = 4

# n*(n+1) // 2

squares = [i**2 for i in range(1,11)]

print(squares)