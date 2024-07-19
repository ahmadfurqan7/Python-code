# Parent class
class Animal:
  def __init__(self, name):
    self.name = name

  # Generic sound method for any animal
  def sound(self):
    print("Making a sound")

# Child class Dog
class Dog(Animal):
  def __init__(self, name, breed, age):
    super().__init__(name)
    self.breed = breed
    self.age = age
  
  # Overridden sound method for Dog
  def sound(self):
    # Call the sound method from Animal
    super().sound()
    # Additional functionality for Dog
    print("Woof!")

# Creating an instance of Dog
my_dog = Dog("Jax", "Bulldog", 5)

# Calling the overridden sound method
my_dog.sound()