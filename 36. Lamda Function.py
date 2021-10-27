'''
- A function without name (Anonymous Function)
- Not Powerful as Named Function
- If can work with, single expression / single line of code

#
Lambda Parameter : expression

print((lambda Parameter : expression) (value))

'''
# Named Function :
def calculate(a , b):
    return a*a + 2*a*b + b*b

print(calculate(2 , 3))

# lambda Function:
print((lambda a , b : a*a + 2*a*b + b*b) (2,3))


# Use Variable:

A = (lambda a , b : a*a + 2*a*b + b*b) (2,3)
print(A)

##
def cube(X) :
    return X*X*X
print(cube(2))

#
A = (lambda X : X * X * X) (2)
print(A)



