
#! This file must be saved separately as a module in the same directory as the file that imports it.

def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name"""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

#~ C:\Users\shekh\Projects\Python_Tutorials\Python_Crash_Course.py>pytest
#~ ============================================================= test session starts ==============================================================
#~ platform win32 -- Python 3.12.2, pytest-8.1.1, pluggy-1.4.0
#~ rootdir: C:\Users\shekh\Projects\Python_Tutorials\Python_Crash_Course.py
#~ plugins: anyio-4.3.0
#~ collected 1 item
#~ 
#~ test_name_function.py .      [100%]  A single dot after test name indicates currently first test being run.
#~ ============================================================== 1 passed in 0.03s ======

#% The output of the above test indicates that the function get_formatted_names will always work for names that have a first and last name, unless we modify the function.

#% The test is a good indicator that the function is working as expected.

#* When the pytest fails, the single dot after the test name gets replaced by 'F' which means one test failed.

