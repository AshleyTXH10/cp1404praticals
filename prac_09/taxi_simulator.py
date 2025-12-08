from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi
MENU = "q)uit, c)hoose taxi, d)rive"
MENU_OPTIONS = "qcd"


def main():
    """Runs the taxi simulator program."""
    current_taxi = None
    taxis = [Taxi(name="Prius", fuel=100), SilverServiceTaxi(name="Limo", fuel=100, fanciness=2), SilverServiceTaxi(name="Hummer", fuel=200, fanciness=4)]
    bill = 0.0

    print("Let's drive!")
    option = get_option()
    while option != "q":
       if option == "d":
           if current_taxi is None: # If taxi is empty
               print("You need to choose a taxi before you can drive")
           else:
               current_taxi.start_fare()
               distance = get_valid_distance()
               current_taxi.drive(distance)
               trip_cost = current_taxi.get_fare()
               print(f"Your {current_taxi.name} trip cost you ${trip_cost}")
               bill += trip_cost

       if option == "c":
           print("Available taxis:")
           print_taxis(taxis)
           taxi_choice = int(input(">>> "))
           if 0 <= taxi_choice < len(taxis):
               current_taxi = taxis[taxi_choice]
           else:
               print("Invalid taxi choice")

       print(f"Bill to date: ${bill}")
       option = get_option()
    print(f"Total trip cost: ${bill}")
    print("Taxis are now:")
    print_taxis(taxis)

def get_option():
    """Prompt an option from the user until they enter a valid option, then return it."""
    print(MENU)
    option = input(">>> ").lower()
    while option not in MENU_OPTIONS:
        print("Invalid option")
        print(MENU)
        option = input(">>> ").lower()
    return option

def get_valid_distance():
    """Prompt the user for a distance until they enter a valid distance, then return it."""
    distance = int(input("Drive how far? "))
    while distance < 0:
        distance = int(input("Drive how far? "))
    return distance

def print_taxis(taxis):
    """Print a list of all taxis available"""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

main()