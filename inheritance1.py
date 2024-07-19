#parent class
class Animal:
  def __init__(self, name):
    self.name = name
  
  def move(self):
    print("Moving")

#child class
class Dog(Animal):
  def __init__(self, name, breed, age):
    # Initialize attributes of the superclass
    super().__init__(name)
    # Additional attributes specific to Dog
    self.breed = breed
    self.age = age

  def bark(self):
    print("Woof!")


my_dog = Dog("Jax", "Bulldog", 5)
#inherited attribute
print(my_dog.name)

#Additional attributes
print(my_dog.breed)
print(my_dog.age)