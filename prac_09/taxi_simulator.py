from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi
MENU = "q)uit, c)hoose taxi, d)rive"
MENU_OPTIONS = "qcd"


def main():
    current_taxi = None
    taxis = [Taxi(name="Prius", fuel=100), SilverServiceTaxi(name="Limo", fuel=100, fanciness=2), SilverServiceTaxi(name="Hummer", fuel=200, fanciness=4)]
    bill = 0.0

    print("Let's drive!")
    option = get_option()
    while option != "q":
       if option == "d":

       if option == "c":

       print(f"Bill to date: ${bill}")

def get_option():
    print(MENU)
    option = input(">>> ").lower()
    while option not in MENU_OPTIONS:
        print("Invalid option")
        print(MENU)
        option = input(">>> ").lower()
    return option

main()