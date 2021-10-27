'''
initial number , last number + 1 , difference
'''

# 1 + 2 + 3 + .....+ n

n = int(input("Enter the last number : "))
sum = 0

for X in range(1, n+1, 1) :
    sum = sum + X
print(sum)



## Even (sum) :
# 2 + 4 + 6 + .......+ n

n = int(input("Enter the last number : "))
sum = 0

for X in range(2, n+1, 2) :
    sum = sum + X

print(sum)

# 4 + 8 + 12 + .......+ n

n = int(input("Enter the last number : "))
sum = 0

for X in range(4, n+1, 4) :
    sum = sum + X

print(sum)

## Odd (sum) :

# 1 + 3 + 5 + 7 .......+ n
n = int(input("Enter the last number : "))
sum = 0

for X in range(1, n+1, 2) :
    sum = sum + X

print(sum)

# 3 + 6 + 9 + 12 .......+ n
n = int(input("Enter the last number : "))
sum = 0

for X in range(3, n+1, 3) :
    sum = sum + X

print(sum)

####
# * (sum) : {condition, sum = 1 }

# 1 * 2 * 3 * 4 .....* n

n = int(input("Enter the last number : "))
sum = 1

for X in range(1, n+1, 1) :
    sum = sum * X
print(sum)

## Square (sum) :
# 1*1 + 2*2 + 3*3 + 4*4 .....+ n*n

n = int(input("Enter the last number : "))
sum = 0

for X in range(1, n+1, 1) :
    sum = sum + X*X
print(sum)

# 2*2 + 4*4 + 6*6.....+ n*n

n = int(input("Enter the last number : "))
sum = 0

for X in range(2, n+1, 2) :
    sum = sum + X*X
print(sum)






