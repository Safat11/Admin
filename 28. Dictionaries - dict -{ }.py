'''
{ }
key -> Value pair

{
Name : "Amran Safat",
Email : safat36222@gmail.com,
age : 21,
}
print(Variable["*"])
#
print(Variable.get("*"))
'''

#
studentId = {
    "101" : "Amran Safat",
    "102" : "Rafid Ridita",
    "103" : "Sayed Hossain",
    "104" : "Nahid Alam",
}

print(studentId["102"])

## .get(*)

studentId = {
    "101" : "Amran Safat",
    "102" : "Rafid Ridita",
    "103" : "Sayed Hossain",
    "104" : "Nahid Alam",
}

print(studentId.get("102"))

print(studentId.get("101", "Not valid key"))

print(studentId.get("107", "Not valid key"))