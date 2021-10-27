'''
#Regular Expression -> re

Q: What is Regular Expression?
- Regular expressions are tools for manipulating string.

Q: Why do we need regular expression?
- Verifying that strings match a pattern.
- Performing substitutions in a string.

. Regular expressions can be accessed using the ## 're' module.
- match() : matches at the beginning of a string .
- search() : finds a match of a pattern anywhere in the string.
- findall() : returns a list of all substrings that match a pattern.

##search & match:

import re
pattern = r"String"

if re.match(pattern,"String") :
    print("Match")
else :
    print("Not Matched")


## findall:
import re
pattern = r"String"

print(re.findall(pattern,"String"))

### index check Pattern:
import re
pattern = r"colour"
text= "My favourite colour is Red."
match = re.search(pattern,text)

print(match.start())
print(match.end())
print(match.span())
'''
#re.match
import re
pattern = r"Colour"

if re.match(pattern,"red is a Colour , I love red colour.") :
    print("Match")

else :
    print("Not Matched")
#
import re
pattern = r"Colour"

if re.match(pattern,"Colour is a red , I love red colour.") :
    print("Match")

else :
    print("Not Matched")

## re.search
import re

pattern = r"Colour"

if re.search(pattern, "Colour is a red , I love red colour."):
     print("Match")

else:
    print("Not Matched")

##re.findall
import re

pattern = r"Col"

print(re.findall(pattern, "Colour is a red , I love red Colour."))


### index check Pattern:
import re
pattern = r"colour"
text= "My favourite colour is Red."
match = re.search(pattern,text)

print(match.start())
print(match.end())
print(match.span())