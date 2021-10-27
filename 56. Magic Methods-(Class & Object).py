'''
## Magic Methods : __N__()
#Magic methods for comparison :              #Python also provides Magic methods for comparisons :
__eq__(self,other)                            __eq__for ==
__ne__(self,other)                            __ne__for !=
__lt__(self,other)                            __lt__for <
__gt__(self,other)                            __gt__for >
__le__(self,other)                            __le__for <==
__ge__(self,other)                            __ge__for >==

#Magic method for arithmetic calculation :
__add__(self,other)
__sub__(self,other)
__mul__(self,other)
__div__(self,other)
'''

#
class Bike :
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def __eq__(self, other):                                                        #Use Magic
        return self.name == other.name and self.color == other.color

    def __str__(self):                                                              #Use Magic
        return (F"Name : {self.name}, Color : {self.color}")


    def display(self):
        print(F"Name : {self.name}, Color : {self.color}")

bike1 = Bike("Yehma R15" , "Blue")
bike2 = Bike("Yehma FZ" , "Red")
print(bike1)
print(bike2)

print(bike1 == bike2)

#

bike4 = Bike("Yehma FZ" , "Red")
bike5 = Bike("Yehma FZ" , "Red")
print(bike4==bike5)



