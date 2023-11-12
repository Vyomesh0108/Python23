# Hybrid Inheritance

# Define a class 'Car' with properties
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        print(f"{self.brand} is starting.")


# Define a class 'AirCondition' with properties
class AirCondition:
    def __init__(self, model):
        self.model = model

    def turn_on(self):
        print(f"{self.model} air condition is turning on.")


# Define a class 'HybridCar' with hybrid inheritance
class HybridCar(Car, AirCondition):
    def __init__(self, brand, model):
        Car.__init__(self, brand)
        AirCondition.__init__(self, model)


# Create an instance of the 'HybridCar' class
hybrid_car = HybridCar("Toyota", "RQ232SA")

# Call methods on the instance to demonstrate hybrid inheritance
hybrid_car.start_engine()
hybrid_car.turn_on()