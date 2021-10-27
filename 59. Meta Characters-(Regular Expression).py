'''
.(dot) (any character)
^$  (^-1st  $-End)
*(0 or more)                       { * name - Astricts}
+(1 or more)
?(0 or 1)

{and}

'''
# .
import re
pattern = r"colo.r"

if re.match(pattern,"colour"):
    print("Matched")

# ..
import re
pattern = r"colo..r"

if re.match(pattern,"colouBr"):
    print("Matched")

## ^ . $  (^-1st . $-End)
import re
pattern = r"^colo.r$"

if re.match(pattern,"colour"):
    print("Matched")


## *(0 or more)           { * name - Astricts}
import re
pattern = r"a*"

if re.match(pattern,"aaaacolour"):
    print("Matched")

# multiple: ("ab*")
import re
pattern = r"(ab*)"

if re.match(pattern,"abaaaacolour"):
    print("Matched")

## +(1 or more)
import re
pattern = r"(a+)"

if re.match(pattern,"abaaaacolour"):
    print("Matched")

#
import re
pattern = r"(a+b)"

if re.match(pattern,"abcolour"):
    print("Matched")

# +(1 or more) {Not Matched}
import re
pattern = r"(a+)"

if re.match(pattern,"colour"):
    print("Matched")
else:
    print("Not Matched")

## ?(0 or 1)
import re
pattern = r"ice(-)?cream"

if re.match(pattern,"ice-cream"):
    print("Matched")

# ?(0 or 1) {Not Matched}
import re
pattern = r"ice(-)?cream"

if re.match(pattern,"ice---cream"):
    print("Matched")
else:
    print("Not Matched")
