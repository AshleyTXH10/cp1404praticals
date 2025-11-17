from car import Car
import random

class UnreliableCar(Car):
    def __init__(self, reliability: float, **kwargs):
        super().__init__(**kwargs)
        self.reliability = reliability

    def drive(self, distance):
        if random.randint(1,100) < self.reliability:
            self.fuel -= distance
        self._odometer += distance