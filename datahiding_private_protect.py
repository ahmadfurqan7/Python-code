class Car:
  def __init__(self, model, year, odometer):
    self.model = model
    self.year = year
    # Making the odometer attribute 'private'
    self.__odometer = odometer  

  def _describe_car(self):  # Making the describe_car method 'protected'
    print(self.year, self.model)

  def __read_odometer(self):  # Making the read_odometer method 'private'
    print("Odometer:", self.__odometer, "miles")


my_car = Car('Audi', 2020, 15000)

#accessing protected method
my_car._describe_car()

#error when accessing a privet method
my_car.__read_odometer()