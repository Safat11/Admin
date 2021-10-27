'''
- Make 2 class work:

#Constructor -    def __init__(self):

- work at Inheritance but Override

##super class Call :
        super().__init__()

'''
#
class Phone :
    def __init__(self):
        print("I'm in Phone class.")

class Samsung(Phone) :
    # init
    pass

s= Samsung()


## Override :
class Phone :
    def __init__(self):
        print("I'm in Phone class.")

class Samsung(Phone) :
    def __init__(self):
        print("I'm in Sumsung class.")


s= Samsung()

##super class Call :
class Phone :
    def __init__(self):
        print("I'm in Phone class.")

class Samsung(Phone) :
    def __init__(self):
        super().__init__()
        print("I'm in Sumsung class.")


s= Samsung()