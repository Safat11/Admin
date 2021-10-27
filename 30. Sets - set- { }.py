'''
A set can be created using :
- Curly braces, > { }
- set Function. > Set([N])

#Use> in, not in == True, False

# Union value: A | B   (Common Number)
#Inter Section: A & B   (Similar Number)
#Difference Value: A - B

# Help Index Number == Item not access
# Duplicate Item not run
'''

#
Num = {1, 2, 3, 4, 5}
print(Num)

#Duplicate Item:

Num = {1, 2, 3, 4, 5, 5, 5,}
print(Num)


# set Function :
Num = {1, 2, 3, 4, 5}
Num2 = set([4, 5, 6])
print(Num2)

#Function :
Num = set([4, 5, 6])
Num.remove(4)
print(Num)

Num = set([4, 5, 6])
Num.add(7)
print(Num)

# in, not in

Num = set([4, 5, 6])
Num.add(7)
print(7 in Num)

Num2 = set([4, 5, 6])
print(7 not in Num2)

## Union value= A | B   (Common Number)
Num1 = {1, 2, 3, 4, 5}
Num2 = set([4, 5, 6])
print(Num1 | Num2)

##Inter Section= A & B   (Similar Number)
Num1 = {1, 2, 3, 4, 5}
Num2 = set([4, 5, 6, 7])
print(Num1 & Num2)

#Difference Number: A - B
print(Num1 - Num2)