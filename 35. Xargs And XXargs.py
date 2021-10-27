'''
###Xarguments - Xargs
use- all print >
  *

def FName(*Details):
        print(Details)

FName("Perameter")


#> Notes: Xargs, work in as like 'Tuples'
'''
#normally,
def student(ID , Name) :
    print(ID , Name)

student(101,"Safat")

## *
def student(*Details) :
    print(Details)

student(101,"Safat",3.95)

#
def add(*Numbers) :

    print(Numbers)

add(10 , 20)
add(10 , 20 , 30)
add(10 , 20 , 30 , 40)

#Summation:
def add(*Numbers) :
    sum = 0

    for num in Numbers :
        sum = sum + num
    print(sum)

add(10 , 20)
add(10 , 20 , 30)
add(10 , 20 , 30 , 40)

##...................##
'''
## XXarguments - XXargs

- "Key Value"

use- all print >
  **

def FName(**Details):
        print(Details)

FName("Perameter")

#> Notes: XXargs, work in as like 'Dictionary'
'''
#
def Student(ID , Name) :
    print(ID , Name)

Student(ID = 100 , Name = "Safat")

## **
def Student(**Details) :
    print(Details)

Student(ID = 101 , Name = "Safat")

# key - Value
def Student(**Details) :
    print(Details["ID"])
    print(Details["Name"])

Student(ID = 101 , Name = "Safat")