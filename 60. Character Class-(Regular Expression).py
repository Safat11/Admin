'''
[TEXT]

- 1st word check.then Match
'''
#
import re
pattern = r"[aeiou]"

if re.match(pattern,"afkjafggwe"):
    print("Matched")

#
import re
pattern = r"[A-Z]"

if re.match(pattern,"Afkjafggwe"):
    print("Matched")

#
import re
pattern = r"[1-9]"

if re.match(pattern,"5fkjafggwe9"):
    print("Matched")

#
import re
pattern = r"[A-Z][a-z][1-9]"

if re.match(pattern,"Af1afggwe"):
    print("Matched")