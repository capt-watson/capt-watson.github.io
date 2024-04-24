#^ Project # 1


str = 'and'
try:
    def test(str, ind):
        lst = input('Enter names separated by space: ').split()
        assert lst != []
        lst.insert(ind, str)                ## inserts string into list
        str1 = ', '.join(lst)               ## converts list into string
        str2 = str1.replace(str+',',str)    ## replaces string with string
        return str2
    print(test(str, -1))
except AssertionError:
    print('Please enter valid names and/or numbers')



#^ Project # 2

