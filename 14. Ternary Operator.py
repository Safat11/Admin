num1 = 40
num2 = 30
'''
if num1>num2 :
    print(num1)

else :
    print(num2)
'''
#
print(num1 if num1>num2 else num2)

print(num1 if num1<num2 else num2)


#
num1 = 40
num2 = 30

max = (num1 if num1>num2 else num2)

print("Maximum = " ,max)

num1 = 40
num2 = 30

min = (num1 if num1<num2 else num2)

print("Minimum = " ,min)

