'''
- Recursion is a process where a function can call itself.
- To stop calling we need a base case.

# 2 important points in case of Recursion :
1 . Recursion call
2. Base case

# !(fact - factorial)
#Factorial Example:
5! = 5 * 4 * 3 * 2 * 1
4! = 4 * 3 * 2 * 1
3! = 3 * 2 * 1
2! = 2 * 1
1! = 1

# n! = n * (n-1)!

####
def fact(n) :
    if n==1 :
        return 1

    else :
        return n * fact (n-1)

print(fact(N Value))
'''

#
def fact(n) :
    if n==1 :
        return 1

    else :
        return n * fact (n-1)

print(fact(5))

#
def fact(n) :
    if n==1 :
        return 1

    else :
        return n * fact (n-1)

print(fact(4))
