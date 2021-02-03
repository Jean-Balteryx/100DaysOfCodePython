# *args
def add(*args):
    total = 0
    for n in args:
        total += n

    return total


print(add(1, 2, 3, 4, 5, 6))


# **kwargs
def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


# **kwargs.get()
class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan")
print(my_car.model)