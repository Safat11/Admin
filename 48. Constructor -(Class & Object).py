'''
-perameter-> (self)
-methood-> init
#
class Student :
roll = ""
gpa = ""


    def __init__(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
         print(F"Roll : {self.roll} , GPA : {self.gpa}")

variable.display()
'''
## Make 2 Function work:
class Student:
    roll = ""
    gpa = ""

    def __init__(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
         print(F"Roll : {self.roll} , GPA : {self.gpa}")


Safat = Student(101,3.85)

Safat.display()

Amran = Student(102,3.50)
Amran.display()
