'''
- Must Use Square Bracket : []

#Map:
variable = [Expression for Item in list]

#Filter:
variable = [Item for Item in list if Expression]


'''
# map :
num = [1, 2, 3, 4, 5]

Result = [X*X for X in num]
print(Result)

#
Result = list(map(lambda X : X*X , num))
print(Result)

#
Result = [X %2 == 0 for X in num]
print(Result)

## filter:
num = [1, 2, 3, 4, 5]

Result = [X for X in num if X%2 ==0]
print(Result)

#
Result = list(filter(lambda X : X%2 == 0 , num))
print(Result)