class Animal:
  def __init__(self, name):
    self.name = name
  
  def move(self):
    print("Moving")

# Inherits from Animal class
class Dog(Animal):
  # Specific behavior
  def bark(self):
    print("Woof!")
    
# Creating an instance
my_dog = Dog("Bob")

# Inherited attribute and behavior
print(my_dog.name)
my_dog.move()

# Specific behavior
my_dog.bark()