# class A:
    
#     def feature1(self):
#         print("Feature 1 is Working")
        
        
#     def feature2(self):
#         print("Feature 2 is Working")
        
        
# class B(A):   # Class B is inheriting features from A. Class A is parent or Super class and class B is child or Sub class. Single level inheritance
    
#     def feature3(self):
#     def feature3(self):
#         print("Feature 3 is Working")
        
#     def feature4(self):
#         print("Feature 4 is Working")
        
        
# class C(B):     # Class C is inheriting features from B. Class B is parent or Super class and class C is child or Sub class. Multi level inheritance
        
#     def feature5(self):
#         print("Feature 5 is Working")
        

# a1 = A()

# b1 = B()

# a1.feature1()
# a1.feature2()


class A:
    
    def feature1(self):
        print("Feature 1 is Working")
        
        
    def feature2(self):
        print("Feature 2 is Working")
        
        
class B:   # Class B is inheriting features from A. Class A is parent or Super class and class B is child or Sub class. Single level inheritance
    def feature3(self):
        print("Feature 3 is Working")
        
    def feature4(self):
        print("Feature 4 is Working")
        
        
class C(A,B):     # Class C is inheriting features from B & A. Class A & B are parent or Super classes and class C is child or Sub class. Multiple inheritance
        
    def feature5(self):
        print("Feature 5 is Working")
    
    
a1 = A()
b1 = B()
c1 = C()

# a1 will only have features 1 and features 2. b1 will have only features 3 and features 4. c1 will inherit features of both classes A and B

