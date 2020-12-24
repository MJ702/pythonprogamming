class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 50
        self.amount = 50

    def get_describe_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + str(self.model)
        return long_name.title()

    def read_odommeter(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back  an odometer")

    def incement_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self, amount):
        print("The gas inject in  gas tank amount of " + str(self.amount))


class Battery():

    def __int__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has " + str(self.battery_size) + " -kwh battery")


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        print('The car has ' + str(self.battery_size) + ' -kwh battery')

    def fill_gas_tank(self):
        print("This car dosen't need a gas tank")


my_tesla = ElectricCar("BMW", 'xg', 2016)
my_tesla.battery.describe_battery()
