## Thread
#! In Python program, if we write a group of statements, then these
#! statements are executed by Python Virtual Machine (PVM) one by one.
#! This execution is called a thread, because PVM uses a thread to
#! execute these statements.

#% Program to find the currently running thread in a Python program.

# import threading

# print('Let us find the current thread')

# ## Find the name of the present thread

# print('Currently Running thread:',threading.current_thread().name)

## check if it is main thread or not

# if threading.current_thread() == threading.main_thread():
#     print('The current thread is the main thread')
# else:
#     print('The current thread is not the main thread')

#% In Python program, there is always a default thread , called
#% 'Main Thread' that executes the program statement

#! Syntax for the creation of a new thread:

#@ t = Thread(target=function_name, [args=(arg1, arg2,...)])

#! To call a thread:

#@  t.start()

#! Create a thread and use it to run a function

# from threading import Thread

# def display():
#     print('Hello, I am running')
    
# ## create a thread and run the function for 5 times

# for i in range(5):
#     ## create the thread and specify the function as its target
#     t= Thread(target=display)
#     ## Run the Thread.
    
#     t.start()
    
#% Creating a thread without using a class

# from threading import Thread

# def display(str):
#     print(str)

# for i in range(5):
#     t = Thread(target=display, args=('Hello',))
#     t.start()
    
## Observe the comma (,)after the argument 'Hello' mentioned in the
## tuple. We should remember that when a single element is specified
## in a tuple, a comma is needed after that element.

#! Create a thread by making our class as subclass to Thread class.

# from threading import Thread

## Create a class as a subclass to Thread class
# class MyThread(Thread):
    
#     ## override the run() method of Thread class
#     def run(self):
#         for i in range(1,6):
#             print(i)

# ## Create an instance of MyThread class

# t1 = MyThread()

# ## start running the thread t1
# t1.start()

# ## Wait until the thread completes execution
# t1.join()

#! Create a thread that accesses the instance variables of a class

# from threading import Thread

# ## Create a class as subclass to Thread class

# class MyThread(Thread):

#     ## Constructor that calls Thread class constructor
#     def __init__(self, str):
#         Thread.__init__(self) ## calls Thread class constructor
#         self.str = str
        
#     ## Override the run() method of Thread class
#     def run(self):
#         print(self.str)

# t1 = MyThread('Hello')

# t1.start()

# t1.join()

#@ Creating a Thread without creating a sub class to Thread class

#! Create a thread that acts on the object of a class that is not
#! derived from the Thread class

# from threading import Thread

# ## create our own class

# class MyThread:
    
#     def __init__(self, str):
#         self.str = str
        
#     ## a method
#     def display(self, x, y):
#         print(self.str)
#         print('The args are: ',x, y)
    
# obj = MyThread('Hello')

# ## create a thread to run display method of obj

# t1 = Thread(target=obj.display, args=(1,2))

# t1.start()

#@ Single tasking using a thread

#! Show single tasking using a thread that prepares a tea.

# from threading import Thread
# from time import sleep

# ## Create our own class

# class MyThread:
#     ## Write a method that performs 3 tasks one by one
#     def prepare_tea(self):
#         self.task1()
#         self.task2()
#         self.task3()

#     def task1(self):
#         print('Boil milk and tea powder for 5 minutes..', end=' ')
#         sleep(5)
#         print('Done!')

#     def task2(self):
#         print('Add sugar and boil for 3 more minutes..', end=' ')
#         sleep(3)
#         print('Done')

#     def task3(self):
#         print('Filter the tea and serve...', end= ' ')
#         print('Done!')

# obj = MyThread()

# ## Create a thread and run prepare_tea method of obj.
# t = Thread(target=obj.prepare_tea)
# t.start()

#@ Multitasking using multiple threads

#! Perform two tasks using two threads simultaneously

from threading import Thread
from time import sleep

class Theatre:
    ## constructor that accepts a string
    def __init__(self, str):
        self.str = str
    
    ## a method that repeats for 5 tickets
    def movie_show(self):
        for i in range(1,6):
            print(self.str, ' : ', i)
            sleep(0.1)
    
obj1 = Theatre('Issue Tickets')
obj2 = Theatre('Show Chair')

## Create two threads to run movie_show() method
t1 = Thread(target=obj1.movie_show)
t2 = Thread(target=obj2.movie_show)

## Run the threads

t1.start()
t2.start()

#% In this example, chair is shown to the 5th person before issuing him/her a ticket

#% This is called a 'race condition'.

#% race condition is a situation when threads are not acting in an expected sequence, thus
#% leading to unreliable output.

#% race condition can be eliminated using 'thread synchronization'

#! A program where two threads are acting on the same method to allot a berth for the
#! passenger.

