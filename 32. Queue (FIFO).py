'''
### Queue : (FIFO = First In The First Out)

#use Function:
from collection import deque

Variable = deque(["N"])
Variable.pop()
print(Variable)
'''

#
from collections import deque

Bank = deque(["Safat", "Siam", "Rahat"])
print(Bank)

Bank.popleft()
print(Bank)

#Enpty Check : DO all pop()
Bank = deque(["Safat", "Siam", "Rahat"])
Bank.popleft()
Bank.popleft()
Bank.popleft()

if not Bank :
    print("No person left")