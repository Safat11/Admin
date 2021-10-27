'''
Module: Python file - where the Code will be(area_module) > then, Access another file

-
import *  - all function access by module
'''

#normally:
from math import pow,sqrt
print(pow(2,3))

### Make Module(area_module) :

from area_module import Triangle_area,Rectangle_area

Triangle_area(20 , 30)
Rectangle_area(20 , 30)


#
from area_module import *
Triangle_area(10, 15)
Rectangle_area(20, 40)

