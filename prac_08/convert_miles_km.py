from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934
MILE_VALUE = 1

class MilesToKmApp(App):
    km_text = StringProperty("0 km")
    def build(self):
        self.title = "Convert miles to km"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def get_miles(self):
        try:
            return int(self.root.ids.input_miles.text)
        except ValueError:
            return 0.0

    def convert_miles_to_km(self):
        miles = self.get_miles()
        km = miles * MILES_TO_KM
        self.km_text = f"{km:.2f} km"

    def increase_miles(self):
        miles = self.get_miles() + MILE_VALUE
        self.root.ids.miles_input.text = str(miles)
        self.convert_miles_to_km()

    def decrease_miles(self):
        miles = self.get_miles() - MILE_VALUE
        self.root.ids.miles_input.text = str(miles)
        self.convert_miles_to_km()

MilesToKmApp().run()