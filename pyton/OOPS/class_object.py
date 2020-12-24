# declare a class
class car:

    def __init__(self, model_name, year, price):
        self._model_name = model_name
        self._year = year
        self._price = price

    def price_inc(self):
        self._price = int(self._price * 1.17)


honda = car("City", 2015, 650000)
tat = car("Blot", 2018, 785000)

# Instant of class
# honda.cc = 1500

# print whole think of honda
# print(honda.__dict__)

# Inheritance

"""
class super_car(car):
    pass

a = super_car('bmw' , 2012, 871000)
print(a.__dict__)

"""



