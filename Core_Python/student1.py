
#@ Inheritance

from preacher import Teacher

class Student(Teacher): ## Student class is derived from Teacher class
    def setmarks(self, marks):
        self.marks = marks
    def getmarks(self):
        return self.marks
    
s = Student()

s.setid(100)
s.setname('Aarav')
s.setaddress('A-103, Ramayan, Kanddarpada, Dahisar W, Mumbai 400 068')
s.setmarks(1510)

print('Id= ',s.getid())
print('Name= ',s.getname())
print('Address= ',s.getaddress())
print('Marks= ',s.getmarks())

## Here we have inherited Student Class from Teacher Class.

## Original class i.e. Teacher class is called 'base class' or 'Super Class'

## Newly created class i.e. Student class is called 'sub class' or 'derived class.'

