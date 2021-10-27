'''
numOfLetters >  if X >= "a" and X <= "z"    {X= X.lower()}
numOfDigits > elif X >= "0" and X <= "9" :
numOfWords > elif  X == " " :
'''

### My name is 12345

numOfLetters = 0
numOfDigits = 0
numOfWords = 0

text = input("Enter a text of numbers : ")              # My name is 12345

for X in text :

    X= X.lower()
    if X >= "a" and X <= "z" :
        numOfLetters = numOfLetters + 1

    elif X >= "0" and X <= "9" :
        numOfDigits = numOfDigits + 1

    elif X == " " :
        numOfWords = numOfWords + 1

print("Numer Of Letters : ",numOfLetters)
print("Numer Of digits : ",numOfDigits)
print("Numer Of Words : ",numOfWords+1)

#.................................#

#10 20 30 40 = sum                      # search in google : pynative.com >(practicing more)

n = input("Enter a text of numbers : ")

list = n.split()            #10 20 30 40

sum = 0
for num in list :
    sum = sum + int(num)
print(sum)





