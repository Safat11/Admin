'''
- work at Make a Function
-# Make 2 Function work:

#
-perameter-> (self)

    def display(self):
         print(F"Roll : {self.roll} , GPA : {self.gpa}")

variable.display()
'''
#
class Student:
    roll = ""
    gpa = ""

    def display(self):
         print(F"Roll : {self.roll} , GPA : {self.gpa}")


Safat = Student()

Safat.roll = 101
Safat.gpa = 3.75

Safat.display()

Amran = Student()
Amran.roll = 102
Amran.gpa = 3.70
Amran.display()

## Make 2 Function work:
class Student:
    roll = ""
    gpa = ""

    def set_value(self,roll,gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
         print(F"Roll : {self.roll} , GPA : {self.gpa}")


Safat = Student()

Safat.set_value(101,3.85)

Safat.display()

Amran = Student()
Amran.set_value(102,3.50)
Amran.display()
