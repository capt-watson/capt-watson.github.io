#@ linked Lists

## linked list contains a group of elements in the form of nodes.

## Each node has three fields

#! A program to create a linked list and perform operations on the list.

#% Create an empty list

# ll = []

# #% add some string type elements to ll

# ll.append('America')
# ll.append('Norway')
# ll.append('Japan')
# ll.append('Chile')
# ll.append('Israel')

# #% Display the list

# print('The existing list: ',ll)

# #% Display menu

# choice = 0
# while choice < 5:
#     print('LINKED LIST OPERATIONS')
#     print(' 1 - Add element')
#     print(' 2 - Remove element')
#     print(' 3 - Replace element')
#     print(' 4 - Search for element')
#     print(' 5 - Exit')
#     choice = int(input('Enter your choice: '))
    
# #% Perform a task depending on user choice:

#     if choice == 1:
#         element = input('Enter an element: ')
#         pos = int(input('At which position? '))
#         ll.insert(pos+1, element)

#     elif choice == 2:
#         try:
#             element = input('Enter element to be removed: ')
#             ll.remove(element)
#         except ValueError:
#             print('Element not found')

#     elif choice == 3:
#         element = input('Enter new element: ')
#         pos = int(input('At which position? '))
#         ll.pop(pos-1)
#         ll.insert(pos-1, element)
        
#     elif choice == 4:
#         element = input('Enter element to search: ')
#         try:
#             pos = ll.index(element)
#             print('Element found at position: ',pos+1)
#         except ValueError:
#             print('Element not found')
            
#     else:
#         break

# #% Display the list elements

#     print('List = ',ll)


#@ Stacks

## A stack represents a group of elements stored in LIFO order.

## Inserting elements (objects) into a stack is called 'push operation'.

## Removing elements from stack is called 'pop operation'.

## Searching for an element and returning it without removing it from the stack is
## called 'peep operation'

## Insertion and deletion of elements take place from only one side of the stack,
## called 'top' of the stack.

#% Elements stored in the memory similar to CD being stored in the CD holder are called
#% a stack.

#! A program to perform various operations on a stack using Stack Class

# from stack import Stack

# #~ Create an empty stack Object

# s = Stack()

# #~ Display menu

# choice = 0
# while choice < 5:
#     print('Stack Operations')
#     print('1 Push Element')
#     print('2 Pop Element')
#     print('3 Peep Element')
#     print('4 Search Element')
#     print('5 Exit')
#     choice = int(input('Enter your choice: '))
    
#     #~ Perform task depending upon user choice
    
#     if choice == 1:
#         element = input('Enter an element: ')
#         s.push(element)
    
#     elif choice == 2:
#         element = s.pop()
#         if element == -1:
#             print('The stack is empty')
#         else:
#             print('Popped element = ',element)
        
#     elif choice == 3:
#         element = s.peep()
#         print('Topmost element = ',element)
        
#     elif choice == 4:
#         element = input('Enter element to search: ')
#         pos = s.search(element)
#         if pos == -1:
#             print('The stack is empty')
#         elif pos == -2:
#             print('Element not found in the stack')
#         else:
#             print('Element found at position: ',pos)
            
#     else:
#         break
    
#     #~ Display the content of the stack object
#     print('Stack = ',s.Display())
    
## In choice 4, the search will count from the top of the stack


#@ Queues

#! A program to perform some operations on a queue

# from que1 import Queue

# #% create empty queue object

# q = Queue()

# choice = 0
# while choice < 4:
#     print('Queue Operations')
#     print('1 Add Element')
#     print('2 Delete Element')
#     print('3 Search for Element')
#     print('4 Exit')
#     choice = int(input('Enter your choice: '))
    
#     if choice == 1:
#         element = float(input('Enter an element: '))
#         q.add(element)
        
#     elif choice ==2:
#         element = q.delete()
#         if element == -1:
#             print('The queue is empty')
#         else:
#             print('Removed element = ',element)
            
#     elif choice == 3:
#         element = float(input('Enter element to search: '))
#         pos = q.search(element)
#         if pos == -1:
#             print('Queue is empty')
#         elif pos == -2:
#             print('Element not found in the queue')
#         else:
#             print('Element found at position: ',pos)
#     else:
#         break
    
#     print('Queue = ',q.Display())


#@ Deques

## Allowing insertions and deletion at both end of the queue is called
## double ended queue or 'deque'.

#! A program to create and use deque

from collections import deque

## create an empty deque

d = deque()

choice = 0
while choice < 7:
    print('DEQUE OPERATIONS')
    print(' 1 Add Element at the front')
    print(' 2 Remove Element from the front')
    print(' 3 Add Element at the rear')
    print(' 4 Remove Element from the rear')
    print(' 5 Remove Element from the middle')
    print(' 6 Search for Element')
    print(' 7 Exit')
    choice = int(input('Enter Your Choice = '))
    
    if choice == 1:
        element = input('Enter element to be added: ')
        d.appendleft(element)
        
    elif choice == 2:
        if len(d) == 0:
            print('Deque is empty')
        else:
            d.popleft()
    
    elif choice == 3:
        element = input('Enter element to be added at the end: ')
        d.append(element)
        
    elif choice == 4:
        if len(d) == 0:
            print('Deque is empty')
        else:
            d.pop()
            
    elif choice == 5:
        element = input('Enter the element to be removed from middle: ')
        try:
            d.remove(element)
        except ValueError:
            print('Element not found')
    
    elif choice == 6:
        element = input('Enter the element to be searched: ')
        c = d.count(element)
        print('No. of times element found: ',c)
    else:
        break
    
    print('Deque = ', end=' ')
    for i in d:
        print(i, ' ', end=' ')
    print()         ## Move the cursor to the next line
    