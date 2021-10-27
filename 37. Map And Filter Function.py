### Map Function :
'''
# map Function work in, list[] & lambda both
- Value : True / False
#
def FName(Parameter) :
    return Expression

variable = [value List]

Result = list(map(FName ,Variable))

print(Result)
'''
# map(Fname) :
def square(X) :
    return X*X

num = [1, 2, 3, 4, 5]

Result = list(map(square ,num ))

print(Result)


# map(lambda Function) :
num = [1, 2, 3, 4, 5]

Result = list(map(lambda X : X * X , num))
print(Result)

### Filter Function :
'''
# Filter Function work in, list & lambda both
- Value : count 


variable = [value List]

Result = list(filter(lambda Parameter : expression , variable))
print(Result)
'''
#
num = [1, 2, 3, 4, 5]

Result = list(filter(lambda X : X % 2 == 0 , num))
print(Result)

## map :
#
num = [1, 2, 3, 4, 5]

Result = list(map(lambda X : X % 2 == 0 , num))
print(Result)
