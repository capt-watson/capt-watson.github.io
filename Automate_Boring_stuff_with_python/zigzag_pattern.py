import time

counter = 0
indent = 0
indentInc = True

try:
    num = int(input('Enter a number less than or equal to 5: '))
    assert num <= 5
    while True and counter < num:
        print(' ' *indent, end='')
        print('********')
        time.sleep(0.1)
        if indentInc:
            indent += 1
            if indent == 20:
                indentInc = False
        else:
            indent -= 1
            if indent == 0:
                indentInc = True
                counter += 1
    print('You have reached the end of the program')
except AssertionError:
    print('Entered number must be less than or equal to 5')