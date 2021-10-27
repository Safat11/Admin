'''
- Function: sub(pattern,replace,string)
#
import re
pattern = r"word"
text="string"
re.sub(pattern,replace,string)
'''
#Search & Replace:
import re
pattern = r"colour"
text1 = "My favourite colour is red. I love blue colour as well."

text2 = re.sub(pattern,"color",text1)
print(text2)

## Replace - count= n:
text2 = re.sub(pattern,"color",text1 , count=1)
print(text2)
