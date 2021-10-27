'''
1. Hierarchical inheritance
2. Multi-Level Inheritance       = A > B(A) > C(B)
3. Muliple Inheritance           = C(A , B) / C(B , A)   #Use same Method,   # pass
'''

#2. Multi-Level Inheritance

class A :
    def display1(self):
        print("I am inside A class")

class B (A):
    #display1

    def display2(self):
        print("I am inside B class")

class C (B) :
    #display1
    #display2

    def display3(self):
        super().display1()
        super().display2()
        print("I am inside C class")


Object1 = C()
Object1.display3()
#Object1.display2()
#Object1.display1()


#
##3. Muliple Inheritance : C (A , B)
class A :
    def display(self):
        print("I am inside A class")

class B :
    def display(self):
        print("I am inside B class")

class C (A , B) :
    # A-> display
    # B-> display
    pass



Object1 = C()
Object1.display()


#3. Muliple Inheritance :C (B , A)
class A :
    def display(self):
        print("I am inside A class")

class B :
    def display(self):
        print("I am inside B class")

class C (B , A) :
    pass

Object1 = C()
Object1.display()