'''
ABC = Abstract Base Class

-
from abc import ABC, abstractmethod
Class Shape:
        def __init__(self):

    @ abstractmethod
    def area(self):
        pass
'''
from abc import ABC, abstractmethod

class Shape :
    def __init__(self,dim1,dim2):                               #dim = dimension
        self.dim1 = dim1
        self.dim2 = dim2

    @ abstractmethod
    def area(self):
        pass

class Triangle(Shape) :
    # init
    def area(self):
        area= 0.5 * self.dim1 * self.dim2
        print("Area of Triangle = " , area)



class Rectangle(Shape) :
     def area(self):
        area = self.dim1 * self.dim2
        print("Area of Rectangle = " ,area)

t1= Triangle(20,30)
t1.area()

r1= Rectangle(25,40)
r1.area()
