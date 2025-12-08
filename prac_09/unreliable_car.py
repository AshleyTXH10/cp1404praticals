from car import Car
import random


class UnreliableCar(Car):
    """Represent an unreliable Car object with a parent class of car."""
    def __init__(self, reliability: float, **kwargs):
        """Initialise an unreliable car instance, based on parent class Car."""
        super().__init__(**kwargs)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like parent Car but add in unreliability as well."""
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