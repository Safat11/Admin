'''
- Runtime Error/ Incorrect Input/ Incorrect Code

# keyword :
try :
except :
finally :   (This Under print must run)

#
try :
    list = [20, 0, 30]
    result = list[0] / list[1]                   (index)
    print(result)
    print("Done")

except ExceptionError :
    print("Dividing by zero is not possible")

finally :
    print("Must Run Program")
'''
#
try :
    list = [20, 0, 30]
    result = list[0] / list[1]
    print(result)
    print("Done")

except ZeroDivisionError :
    print("Dividing by zero is not possible")

finally :
    print("Successful")

#
try :
    list = [20, 0, 30]
    result = list[0] / list[3]
    print(result)
    print("Done")

except IndexError :
    print("Dividing by zero is not possible")

#
try :
    list = [20, 0, 30]
    result = list[0] / list[5]
    print(result)
    print("work")

except  :
    print("Dividing by zero is not possible")

finally :
    print("Successful")

# 'try' & 'except' Error But 'finally' must Work:
try :
    list = [20, 0, 30]
    result = list[0] / list[3]
    print(result)
    print("Done")

except ZeroDivisionError :
    print("Dividing by zero is not possible")

finally:
    print("Amran Safat")