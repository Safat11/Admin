#Question:
'''
#Tringle                              t1 = 10, 20
                                     t2= 20,30
. Constructor

    - base
    - height

.Calculate_area()
'''

#Solution:

class Tringle :
    base = ""
    height = ""

    def __init__(self,base,height):
        self.base = base
        self.height = height

    def Calculate_area(self):
        area = 0.5 * self.base * self.height
        print("Area = " ,area)

t1 = Tringle (10,20)
t1.Calculate_area()

t2 = Tringle (20,30)
t2.Calculate_area()


