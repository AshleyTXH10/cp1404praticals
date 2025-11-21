from unreliable_car import UnreliableCar

def main():
    """Run test to see if UnreliableCar class method is working"""
    c1 = UnreliableCar(name="Prius", fuel=10000, reliability=30.0)
    drives = 0
    for i in range(100):
        distance_driven = c1.drive(50)
        if distance_driven > 0:
            drives += 1
        print(c1)

    print(f"Car successfully drove {drives}/100 drives")

main()