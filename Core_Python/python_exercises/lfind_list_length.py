## Finding list length
#! using loop counter

list = [1,4,3,6,0]

counter = 0

for i in list:
    counter += 1
print('Length of the list: ', counter)

#! or using length_hint method

from operator import length_hint

list = [1,4,3,6,0,2,10,18]

list_len = length_hint(list)

print('Length of the list: ', list_len)

#! or using list comprehension

list = [1,4,3,6,0,2,5]

len = sum(1 for _ in list)

print(len)

#! or using recursion

def count(lst):
    if not lst: ## base case. If list is empty, return 0
        return 0
    return 1 + count(lst[1:]) ## add 1 to the count for the remaining elements in the list

lst = [1,4,3,6,0,2]
print(count(lst))

#! or using enumeration

lst = [1,4,3,6,0,2]

s = 0

for i, a in enumerate(list):
    s += 1
print(s)
