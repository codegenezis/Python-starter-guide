class car():
     
    # init method or constructor
    def __init__(self, model, color):
        self.model = model
        self.color = color
         
    def show(self):
        print("Model is", self.model )
        print("color is", self.color )
         
# both objects have different self which
# contain their attributes
audi = car("audi a4", "blue")
ferrari = car("ferrari 488", "green")
 
audi.show()     # same output as car.show(audi)
ferrari.show()  # same output as car.show(ferrari)
 
# Behind the scene, in every instance method
# call, python sends the instances also with
# that method call like car.show(audi)

# The __init__  function is called every time an object is created from a class. The __init__ method lets the class initialize the object’s attributes and serves no other purpose. It is only used within classes. 

