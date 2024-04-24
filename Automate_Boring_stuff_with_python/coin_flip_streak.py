import random

#^ Coin Flip Streak


list1 = []

numberOfStreaks = 0

HStreaks = 0
TStreaks = 0

for i in range(10000):
    if random.randint(0,1) == 0:
        list1.append('H')
    else:
        list1.append('T')


for i in range(len(list1) -5):
    if (list1[i] == 'H' and list1[i+1] == 'H' and  list1[i+2] == 'H' and list1[i+3] == 'H' and list1[i+4] == 'H' and  list1[i+5] == 'H'):
        HStreaks += 1
        numberOfStreaks += 1
for i in range(len(list1) -5):
    if (list1[i] == 'T' and list1[i+1] == 'T' and  list1[i+2] == 'T' and list1[i+3] == 'T' and list1[i+4] == 'T' and  list1[i+5] == 'T'):
        TStreaks += 1
        numberOfStreaks += 1

print('Total Number of Streaks: ',numberOfStreaks)
print('Total number of Head Streaks',HStreaks)
print('Total number of Tail Streaks',TStreaks)
print('Chance of streak: %s%%' %(numberOfStreaks/100))
