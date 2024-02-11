#@ What is Thread?
#! In Python program, if we write a group of statements, then these
#! statements are executed by Python Virtual Machine (PVM) one by one.
#! This execution is called a thread, because PVM uses a thread to
#! execute these statements.

#% Program to find the currently running thread in a Python program.

import threading

print('Let us find the current thread')

## Find the name of the present thread

print('Currently Running thread:',threading.current_thread().name)

## check if it is main thread or not

if threading.current_thread() == threading.main_thread():
    print('The current thread is the main thread')
else:
    print('The current thread is not the main thread')

#% In Python program, there is always a default thread , called
#% 'Main Thread' that executes the program statements