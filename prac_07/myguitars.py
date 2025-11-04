from prac_07.guitar import Guitar

FILENAME = "guitars.csv"
def main():
    guitars = load_guitars(FILENAME)
    for i, guitar in enumerate(guitars):
        print(f"Guitar {i}: {guitar}")

def load_guitars(filename):
    with open(filename, 'r') as in_file:
        guitars = []
        for line in in_file:
            guitar = Guitar(line.strip().split(","))
            guitars.append(guitar)
    return guitars


main()