#! A program to create a stack class that can perform some important operations
class Stack:
    def __init__(self):
        self.st = []
        
    def isempty(self):
        return self.st == []
    
    def push(self, element):
        self.st.append(element)
        
    def pop(self):
        if self.isempty():
            return -1
        else:
            return self.st.pop()
        
    def peep(self):
        n = len(self.st)
        return self.st[n-1] ## n-1 will give the topmost position
    
    def search(self, element):
        if self.isempty():
            return -1
        else:
            try:
                n =self.st.index(element)
                return len(self.st)-n
            except ValueError:
                return -2
            
    def Display(self):
           return self.st