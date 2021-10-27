'''
###Stack : (LIFO = Last In The First Out)

Variable = []     (Empty List)
push > Variable.append("N")     (Data add in Stack)
pop > Variable.pop()     (Data remove in Stack) - (LIFO = Last In The First Out)
'''

#
Book = []
Book.append("Learn C")
Book.append("Learn C++")
Book.append("Learn Java")

print(Book)

#
Book.pop()
print(Book)

#
Book.pop()
print("Now the top book is : ",Book[-1])

#Empty List :
Book.pop()
if not Book :
    print("No Book Left")