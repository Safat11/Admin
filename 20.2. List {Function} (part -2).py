'''
#List Of Function :
1- (len)                - (total item calculate)
2- .append()            - (new item add)
3- .insert(n, "")       - (specific number, new item add)
4- .remove(N)           - (mention Name then remove)
5- .sort()              - (Alphabetical order sorting & number small to big)
6- .reverse()           - (number big to small)
7- .pop()               - (last item delete)
8- .clear()             - (all item delete)

# variable (must use)
9- .copy()              - (copy to new variable)

10> .index(n)           - (specific item position calculate)
11> .count(n)           - (specific continuosly item counting)
'''
subjects = ["Bangla", "English", "Math", "Physics", "Chemistry", "Biology"]

# len() :
print(len(subjects))

# append() :
subjects.append("Islam")
print(subjects)

# insert(n, "") :
subjects.insert(2, "Islam")
print(subjects)

# remove(N) :
subjects.remove("Math")
print(subjects)

## sort() :
subjects.sort()
print(subjects)

numbers = [20, 12, 5, 44, 107]

# sort() :
numbers.sort()
print(numbers)

# reverse() :
numbers.reverse()
print(numbers)

# pop() :
numbers.pop()
print(numbers)

#> pop() :
numbers.pop()
numbers.pop()
print(numbers)

# clear() :
numbers.clear()
print(numbers)

## variable (must use)

# copy() :

subjects = ["Bangla", "English", "Math", "Physics", "Chemistry", "Biology"]

Subjects02 = subjects.copy()
print(subjects)

# index(n) :
pos = subjects.index("Math")
print(pos)

# count(n) :
num =[2, 2, 5, 7, 2, 9, 2]

pos= num.count(2)
print(pos)







