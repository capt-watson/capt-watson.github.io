
## using Teacher Class

from preacher import Teacher
t = Teacher()

## store data into the instance

t.setid(10)
t.setname('Prakash')
t.setaddress('HNO-001, Dwarka, New Delhi')
t.setsalary(250000.50)

## retrieve data from instance and display

print('id= ', t.getid())
print('name= ',t.getname())
print('address= ', t.getaddress())
print('salary= ', t.getsalary())