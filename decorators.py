#decorators:
def decorator(func):
  def wrapper():
    print("before")
    func()
    print("after")
  return wrapper

@decorator
def func():
  print("hey there")

func()