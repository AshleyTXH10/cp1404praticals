from taxi import Taxi

class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, fanciness: float, **kwargs):
        """Initialise a Silver Service Taxi instance, based on parent class Taxi."""
        super().__init__(**kwargs)
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """Return a string like a Taxi but with flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall}"

    def get_fare(self):
        """Return the price for the taxi trip."""
        return round(super().get_fare() + self.flagfall, 2)

    def start_fare(self):
        """Begin a new fare."""
        self.current_fare_distance = 0