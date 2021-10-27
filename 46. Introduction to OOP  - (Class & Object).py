'''
> OOP = Object Oriented Program: Class, Object, Inheritance, Abstraction, Encapsulation, Polymorphism

#class : class is a keyword
#work at .dot Operator

class Name :
    variable = ""                                    {Must Use}
Safat = Student()                                    { object> Safat = Class> Student() }
print(isinstance(Safat, Student))                    { object Check> isinstance(N,N) }
##
print(F"{N1} , {N2}")
'''
#Object Check :
class Student:
    roll = ""

Safat = Student()
print(isinstance(Safat, Student))

#
class Student:
    roll = ""
    gpa = ""


Safat = Student()
Safat.roll = 101
Safat.gpa = 3.75

print(F"Roll : {Safat.roll} , GPA : {Safat.gpa}")

Amran = Student()
Amran.roll = 102
Amran.gpa = 3.70

print(F"Roll : {Amran.roll} , GPA : {Amran.gpa}")


