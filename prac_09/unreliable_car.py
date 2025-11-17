from car import Car
import random


class UnreliableCar(Car):
    def __init__(self, reliability: float, **kwargs):
        super().__init__(**kwargs)
        self.reliability = reliability

    def drive(self, distance):
        if random.randint(1,100) < self.reliability:
            if distance > self.fuel:
                distance = self.fuel
                self.fuel = 0
            else:
                self.fuel -= distance
            self._odometer += distance
            return distance
        else:
            return 0