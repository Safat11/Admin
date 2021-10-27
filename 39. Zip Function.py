'''
- list
- work as like, Tuples

print(list(zip(Variable1, Variable2)))
'''

Roll = [101, 102, 103, 104, 105]
Name = ["Amran Hossain", "Sayed Hossain", "Nahid Alam", "Semona Akter", "Khurshed Alam"]

print(list(zip(Roll, Name)))



## ADD SINGLE VALUE:
print(list(zip(Roll, Name, "ABCDE")))