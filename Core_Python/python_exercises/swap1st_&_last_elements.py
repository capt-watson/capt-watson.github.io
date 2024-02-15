## Swapping between firs and last elements in a list
#! Interchange the 1st & last elements  of the given list

x = [24,35,9,56]

temp = x[0]

x[0] = x[-1]
x[-1] = temp

print(x)

#! Or

def swap_list(lst):    
    lst[0], lst[-1] = lst[-1], lst[0]    
    return lst

lst = [15,58,47,65,12,26]

print(swap_list(lst))

#! or

def swap_list(list):
    get = list[-1], list[0]
    list[0], list[-1] = get

    return list

list = [15,58,47,65,12,26]

print(swap_list(list))

#! or

def swap_list(list):
    start, *middle, end = list
    list = [end, *middle, start]
    return list
    
list = [5,10,15,20,25,30]

print(swap_list(list))


#! or

def swap_list(list):

    first = list.pop(0)
    last = list.pop(-1)

    list.insert(0, last)
    list.append(first)

    return list

list = [7,14,21,28,35,42,49]

print(swap_list(list))

