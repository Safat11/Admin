'''
Mode: "r" = Read , "w" = Write ; "r+" = Read & Write Both
function:
"r" = .Readable , "w" = .Writable , "r+" = .Read  ,  #list:- "r+" = .Readlines

###
-> Variable = open("File Name", "Mode")
print(variable.Function())

-> variable.close()

## File Output Check :
text = file.read()
print(text)

variable1.close()

## Length Check :
text = file.read()
Size = len(text)
print(Size)

variable1.close()

## File List :
text = file.readlines()

#> text = file.readlines() [index]                   (index-list, line choose print)

print(text)

variable1.close()

## For Loop:
for line in file :
    print(line)

variable1.close()
'''

#
file = open("41.2. student.txt", "r")
print(file.readable())
file.close()

# False = "w" - readable
Student = open("41.2. student.txt", "r")
print(Student.writable())

Student.close()

# File Output Check :
file = open("41.2. student.txt", "r+")

text = file.read()
print(text)

file.close()

# File length Check :
file = open("41.2. student.txt", "r+")

text = file.read()
size = len(text)
print(size)

file.close()

# File List :
file = open("41.2. student.txt", "r+")
text = file.readlines()
print(text)

file.close()

# list-[index]
file = open("41.2. student.txt", "r+")
text = file.readlines() [2]                      #(index-list, line choose print)
print(text)
file.close()

# For Loop:
file= open("41.2. student.txt", "r+")
for line in file :
    print(line)

file.close()