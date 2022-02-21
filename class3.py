class A:
  "kiran is here"
  def __init__(self,b):
    self.b = b

  def kiran(self):
    print("the number is", self.b)

class B(A):
  # pass
  def __init__(self,b):
    A.__init__(self,b)  
    # super().__init__(b)

a=A(10)
b=B(10)

print(a.__doc__)
print(a.b)

a.kiran()
b.kiran()

# The child's __init__() function overrides the inheritance of the parent's __init__() function.