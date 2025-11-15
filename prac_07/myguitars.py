from guitar import Guitar

FILENAME = "guitars.csv"
def main():
    """Test program for guitar class"""
    guitars = load_guitars(FILENAME)
    guitars.sort()

    for i, guitar in enumerate(guitars):
        print(f"Guitar {i+1}: {guitar}")

def load_guitars(filename):
    """Load guitars as a list from a csv file"""
    with open(filename, 'r') as in_file:
        guitars = []
        for line in in_file:
            part = line.strip().split(",")
            guitar = Guitar(part[0], int(part[1]), float(part[-1]))
            guitars.append(guitar)
    return guitars


main()