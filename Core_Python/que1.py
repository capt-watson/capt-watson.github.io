class Queue:
    def __init__(self):
        self.qu = []        
    def isempty(self):
        return self.qu == []    
    def add(self, element):
        self.qu.append(element)        
    def delete(self):
        if self.isempty():
            return -1
        else:
            return self.qu.pop(0)  ## Will remove 0th element
    def search(self,element):
        if self.isempty():
            return -1
        else:
            try:
                n = self.qu.index(element)
                return n+1
            except ValueError:
                return -2            
    def Display(self):
        return self.qu
