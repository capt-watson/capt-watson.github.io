## Swapping between two elements
def Swap(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

list = [4,8,12,16,20]
pos1, pos2 = 1,3
print(Swap(list, pos1-1, pos2-1))   ## pos1-1 and pos2-1 because list starts at index 0

#! or using pop() & insert() methods

def swap(list, pos1, pos2):
    first = list.pop(pos1)
    second = list.pop(pos2-1)   ## Pop last element
    
    list.insert(pos1, second)
    list.insert(pos2, first)
    
    return list

list = [4,8,12,16,20]

pos1, pos2 = 1,3

print(Swap(list, pos1-1, pos2-1))
