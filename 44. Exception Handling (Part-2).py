'''
Multiple Exception:
except (ExceptionError , ExceptionError) :

#
def
    if
        raise ExceptionError
    return

try :
    print("")
except ExceptionError as X :
    print(X)
'''
#
try :
    num1 = int(input("Enter First Number :" ))
    num2 = int(input("Enter Second Number :" ))

    result= num1 / num2
    print(result)

except (ValueError , ZeroDivisionError):
    print("you have entered incorrect input.")

finally :
    print("Thanks !!!")

#
def voter(age) :
    if age < 18 :
        raise ValueError("Invalid Voter")
    return "You are allowed to vote"

print(voter(19))

##
def voter(age) :
    if age < 18 :
        raise ValueError("Invalid Voter")
    return "You are allowed to vote"

try :
    print(voter(17))

except ValueError as E :
    print(E)



