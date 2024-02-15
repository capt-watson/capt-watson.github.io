## find max of two numbers
#! Using max()method

a = 5
b = 9

maximum = max(a, b)
print(maximum)


#! Using Ternary operator

# a = 12
# b = 8

# print(a if a > b else b)

a = 11
b = 17

#! using lambda method

maximum = lambda a,b: a if a > b else b

print(f'{maximum(a,b)} is a maximum number.')


#! Using list comprehension

a = 7
b = 11

x = [a if a > b else b]
print('Maximum number is: ',x)
