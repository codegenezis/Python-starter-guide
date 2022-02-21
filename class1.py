#class

class Person:
    # "Kiran is here"
    '''kiran is the best
        of all the students
    '''
    age = 10

    def greet(self):
        print('Hello')

x=Person()
print(x.age)
x.greet()
print(x.__doc__)

#__doc__  --> is the doc string to tell info abt the class

#self is the must keyword to access the attributes/methods of a class. It refers to the current object


