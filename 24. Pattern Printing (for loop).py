'''
n = 4

*
**
***
****
'''

#
n = 4

for i in range(n+1) :
    print(i * "*")

'''
n = 3

*               #i=1> (2 * i - 1)
***             #i=2> (2 * i - 1)
*****           #i=3> (2 * i - 1)
'''

n = 3
for i in range(n+1) :
    print((2 * i - 1) * "*")

