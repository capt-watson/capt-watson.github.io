## Thread
#! In Python program, if we write a group of statements, then these
#! statements are executed by Python Virtual Machine (PVM) one by one.
#! This execution is called a thread, because PVM uses a thread to
#! execute these statements.

#% Concurrent programming and global interpreter lock (GIL)
#% GIL does not allow more than one thread to run at a time.

#& Uses of Threads

#& Threads are useful when we want to perform multiple tasks simultaneously.
#& This is called concurrent programming.

#! Threads are mostly used in server side programs to serve the needs
#! of clients on a network or internet. 

#! Threads are also used in games and animations.

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

# from threading import Thread
# from time import sleep

# class Theatre:
#     ## constructor that accepts a string
#     def __init__(self, str):
#         self.str = str
    
#     ## a method that repeats for 5 tickets
#     def movie_show(self):
#         for i in range(1,6):
#             print(self.str, ' : ', i)
#             sleep(0.1)
    
# obj1 = Theatre('Issue Tickets')
# obj2 = Theatre('Show Chair')

# ## Create two threads to run movie_show() method
# t1 = Thread(target=obj1.movie_show)
# t2 = Thread(target=obj2.movie_show)

# ## Run the threads

# t1.start()
# t2.start()

#% In this example, chair is shown to the 5th person before issuing him/her a ticket

#% This is called a 'race condition'.

#% race condition is a situation when threads are not acting in an expected sequence, thus
#% leading to unreliable output.

#% race condition can be eliminated using 'thread synchronization'

#! A program where two threads are acting on the same method to allot a berth for the
#! passenger.

# from threading import Thread, current_thread
# from time import sleep


# class Railway:
#     ## constructor that accepts no. of available berths
#     def __init__(self, available):
#         self.available = available
        
#     ## A method that reserves berth.
#     def reserve(self, wanted):
#         ## Display no. of available berths
#         print('No. of available berths= ',self.available)
        
#         if self.available >= wanted:
#             ## Find the thread name
#             a = current_thread()
#             ## Display berth is allocated for the person
#             print('%d berth allotted for %s' % (wanted,a.name))
#             ## make time delay so that the ticket is printed
#             self.available -= wanted
#             sleep(1.5)
#             ## Decrease number of available berths
#         else:
#             print('Sorry, no berths available')
            
# obj = Railway(3)  ## here we specify the no. of berth available at the start

# ## create 3 threads and specify no. of berth needed
# t1 = Thread(name='Sita',target=obj.reserve, args=(1,))
# t2 = Thread(name='Ram',target=obj.reserve, args=(1,))

# t1.start()
# t2.start()


#@ Thread Synchronization

#& When a thread is already acting on an object, preventing any other thread from acting
#& on the same object is called 'Thread Synchronization' or 'thread safe'. 

#! Thread Synchronization is done using the following techniques:

#% Using locks
#% Using semaphores

#! mutex = mutually exclusive lock

#! A program achieving thread synchronization using locks

# from threading import Thread, current_thread , Lock
# from time import sleep

# class Railway:
#     ## Constructor that accepts no. of berths available
#     def __init__(self, available):
#         self.available = available
#         ## Create a lock object
#         self.l = Lock()
        
#     ## A method for reserving berths
#     def reserve(self, wanted):
#         ## lock the current object
#         self.l.acquire()
#         ## Display no. of available berths
#         print('Available no. of berths= ',self.available)
        
#         if self.available >= wanted:
#             ## find the thread name
#             a = current_thread()
#             ## Display berth is allotted for this person
#             print('%d berth allotted to %s ' % (wanted, a.name))
#             ## make time delay so that the ticket is printed
#             sleep(1.5)
#             ## Decrease the no. of available berths.
#             self.available -= wanted
#         else:
#             print('Sorry, No berth is available')
#         ## task is completed, release the lock
#         self.l.release()
        
# obj = Railway(2)

# ## Create two threads and specify 2 berth is needed
# t1 = Thread(name='Betty', target=obj.reserve, args=(2,))
# t2 = Thread(name= 'Veronica', target=obj.reserve, args=(1,))

# ## run the threads

# t1.start()
# t2.start()

# #~ Available no. of berths=  2
# #~ 2 berth allotted to Betty 
# #~ Available no. of berths=  0
# #~ Sorry, No berth is available

#@ Deadlock of Threads

#! A program with good logic to avoid deadlocks.

# from threading import Thread, Lock

# ## Take 2 Locks
# l1 = Lock()
# l2 = Lock()

# ## Create a function for booking a ticket
# def book_ticket():
#     l1.acquire()
#     print('Book_Ticket locked a Train')
#     print('Book_Ticket wants to lock a coach')
#     l2.acquire()
#     print('Book_Ticket locked the coach')
#     l2.release()
#     l1.release()
#     print('Booking of tickets done...')
    
# ## create a function for cancelling a ticket
# def cancel_ticket():
#     l2.acquire()
#     print('cancel_ticket locked a coach')
#     print('cancel_ticket wants to lock a train')
#     l1.acquire()
#     print('cancel_ticket locked a train')
#     l1.release()
#     l2.release()
#     print('Cancelling tickets done...')
    
# ## Create two threads and run them
# t1 = Thread(target=book_ticket)
# t2 = Thread(target=cancel_ticket)

# t1.start()
# t2.start()

#@ Communications between Threads

#! A program where Producer and Consumer threads communicate with
#! each other through a boolean type variable.

# from threading import Thread
# from time import sleep

# ## Create a producer class

# class Producer:
#     def __init__(self):
#         self.lst = []
#         self.data_prod_over = False
        
#     def produce(self):
#         ## create 1 to 10 items and add to the list
#         for i in range(1,11):
#             self.lst.append(i)
#             sleep(1)
#             print('Item produced...')
#     ## Inform the consumer that the data production is complete
#         self.data_prod_over = True

# ## Create consumer class
# class Consumer():
#     def __init__(self, prod):
#         self.prod = prod
        
#     def consume(self):
#         ## Sleep for 100ms as long as data_prod_over is False
#         while self.prod.data_prod_over == False:
#             sleep(0.1)
#         ## Display the content of the list when data prod is over.
#         print(self.prod.lst)
            
# ## Create producer object
# p = Producer()

# ## Create Consumer object and pass Producer object.
# c = Consumer(p)

# ## Create producer and consumer threads
# t1 = Thread(target=p.produce)
# t2 = Thread(target=c.consume)

# ## run the thread
# t1.start()
# t2.start()

#@ Thread Communication using notify() and wait() methods

#* The condition class of threading module is useful to improve the
#* speed of communication between threads. The condition class object 
#* is called 'condition variable' and is created as:
#% cv = condition()

#! A program where thread communication is done through notify()
#! and wait() methods of condition object.

# from threading import Condition, Thread
# from time import sleep

# ## create a producer class
# class Producer:
#     def __init__(self):
#         self.lst = []
#         self.cv = Condition()
#     def produce(self):
#         self.cv.acquire()
        
#         for i in range(1,11):
#             self.lst.append(i)
#             sleep(1)
#             print('Items Produced')
            
#         self.cv.notify()
        
#         self.cv.release()
        
# class Consumer:
#     def __init__(self,prod):
#         self.prod = prod
        
#     def consume(self):
#         self.prod.cv.acquire()
#         self.prod.cv.wait(timeout=0)
#         self.prod.cv.release()
#         print(self.prod.lst)
        
# p = Producer()
# c = Consumer(p)

# t1 = Thread(target=p.produce)
# t2 = Thread(target=c.consume)

# t1.start()
# t2.start()

#@ Thread Communication using a Queue

#! A program that uses a Queue in thread communication

# from threading import Thread
# from time import sleep
# from queue import Queue

# class Producer:
#     def __init__(self):
#         self.q = Queue()
        
#     def produce(self):
#         for i in range(1,11):
#             print('Producing item:  ', i)
#             self.q.put(i)
#             sleep(1)
            
# class Consumer:
#     def __init__(self, prod):
#         self.prod = prod
        
#     def consume(self):
#         for i in range(1,11):
#             print('Receiving Item: ',self.prod.q.get(i))
            
# p = Producer()

# c = Consumer(p)

# t1 = Thread(target=p.produce)
# t2 = Thread(target=c.consume)

# t1.start()
# t2.start()


#@ Daemon Threads

#& Threads which run continuously in the background are called Daemon
#& Threads.

#& generally, daemon threads are used for performing some background
#& task.

#! A program to understand the creation of daemon thread.

from threading import Thread
from time import sleep, ctime

## Display numbers from 1 to 5 every second

def display():
    for i in range(5):
        print('Normal Thread: ', end=' ')
        print(i+1)
        sleep(1)
        
## Display date and time once in every 2 seconds
def display_time():
    while True:
        print('daemon thread: ', end=' ')
        print(ctime())
        sleep(2)
        
## Create a normal thread and attach it to display() and run it.
t = Thread(target=display)
t.start()

## Create another thread and attach it to display_time().
d = Thread(target=display_time)

## make the thread daemon
d.daemon = True

## run the daemon thread
d.start()

## to make daemon thread not to terminate, join() method is used.
d.join()
