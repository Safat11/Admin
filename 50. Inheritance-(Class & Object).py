'''
- Make 2 class work:

class phone :                              # phone- super/parent/base class
class samsung (phone) :                    #samsung- sub/child/derived class


## subclass check:
print(issubclass(Samsung , phone))
'''
## Make 2 class work:

class phone :
    def call(self):
        print("you can call.")
    def massage(self):
        print("you can massage.")

class Samsung :
    def call(self):
        print("you can call.")
    def massage(self):
        print("you can massage.")
    def photo(self):
        print("you can take photo.")


p = phone()                     #(object)

p.call()
p.massage()
#
s = Samsung()                  #(object)

s.call()
s.massage()
s.photo()

## Inheritance :
class phone :
    def call(self):
        print("you can call.")
    def massage(self):
        print("you can massage.")

class Samsung (phone) :
    # call , massage
    def photo(self):
        print("you can take photo.")

s = Samsung()                  #(object)

s.call()
s.massage()
s.photo()

## subclass check:

print(issubclass(Samsung , phone))
