class A:

    def __init__(self):
        print("In a Init")
        
    def feature1(self):
        print("Feature 1 is Working")


    def feature2(self):
        print("Feature 2 is Working")


class B(A):   # Class B is inheriting features from A. Class A is parent or Super class and class B is child or Sub class. Single level inheritance
    def feature3(self):
        print("Feature 3 is Working")

    def feature4(self):
        print("Feature 4 is Working")

a1 = B()   # It is read as object of class A is equal to constructor of class A
