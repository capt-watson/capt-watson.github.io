import math
# r = float(input('Enter a number'))
# area = math.pi*r**2

# print('Area of the circle is: {:.2f}'.format(area))

# print(f'Area of the circle is {area}')

# print('Area of the circle is %.2f '% area)

#! Check if number if between 1 and 10

# n = int(input('Enter a number: '))

# if n >=1 and n <= 10:
#     print('Number is between 1 and 10')
# else:
#     print('Number is not between 1 and 10')

#! check if given number is zero or +ve or -ve

# num = int(input('Enter a number: '))

# if num < 0:
#     print('Number',num,'is negative number')
# elif num == 0:
#     print('Number',num,'is Zero')
# elif num > 0:
#     print('Number',num,'is a positive number' )
# else:
#     [print(num,'is not a number')]

#! Display numbers from 0 to 10 using while loop.

# n = 1

# while n <= 10:
#     print(n, end=' ')
#     n += 1    


#! Display even numbers from 100 to 200

# n = 100
# while n <= 200:
#     if n % 2 == 0:
#         print(n)
#     n += 1

#! Display even numbers between m and n

# m,n = [int(i) for i in input('Enter minimum and maximum range: ').split(',')]

# x = m
# if x % 2 != 0:
#     x= x+1
# while x >= m and x <=n:
#     print(x)
#     x += 2

#! Display characters of a strings using for loop

# str = 'Hello'

# for i in str:
#     print(i, end=' ')

#! Display each character from a string using sequence index

# str = 'Hello'

# n = len(str)

# for i in range(n):
#     print(str[i], end=' ')


#! Display odd numbers from 1 to 10 using range object

# for i in range(1,10,2):
#     print(i)

#! Display numbers from 10 to 1 in descending order

# for i in range(10,0,-1):
#     print(i, end=' ')
    
#! Display elements of a list using for loop

# lst = [10, 20.5, 'B', 'Argentina']
# for i in lst:
#     print(i, end=' ')
    
#! Display and find the sum of a list of numbers using for loop

# lst = [10,20,30,40,50]

# sum = 0

# for i in lst:
#     sum += i
#     print(i)
# print('The sum of the numbers is: ',sum)

#! Display and sum of a list of numbers using while loop

# lst = [10, 20, 30, 40, 50]

# sum = 0

# i = 0

# n = len(lst)

# while i < n:
#     print(lst[i])
#     sum += lst[i]
#     i += 1
# print('Sum is: ',sum)

#! Display stars in right angle triangular form using nested loops
# for i in range(1, 11):
#     for j in range(1, i+1):
#         print('* ', end=' ')
#     print()

#! Display stars in right angle triangular form using single loop
# for i in range(1,11):
#     print('* '*i)

primes = []

#! Display prime number series

# max = int(input('Upto which number? '))

# for num in range(2,max+1):
#     for i in range(2, num):
#         if num % i == 0:
#             break
#     else:
#         print(num)

