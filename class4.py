#super keyword

class A:
  def __init__(self,b):
    self.b = b

  def A1(self):
    print("result is", self.b)

class B(A):
  def __init__(self,b):
    super().__init__(b)
    self.x = 2022

obj = B(10)

obj.A1()
print("added attribute", obj.x)