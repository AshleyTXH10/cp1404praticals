"""
wimbledon
Estimate: 25 minutes
Actual: 32 minutes
"""
FILE_NAME = "wimbledon.csv"

def main():
    """Read wimbledon data, print wimbledon champions, amount of their wins and winning countries"""
    champion_country, champion_to_wins = display_wimbledon_data()
    for champion in champion_to_wins:
        print(f"{champion} {champion_to_wins[champion]}")
    print("These 12 countries have won Wimbledon:")
    print(", ".join(sorted(champion_country)))


def display_wimbledon_data():
    wimbledon_data = read_wimbledon_data()
    champion_to_wins = get_champions(wimbledon_data)
    champion_country = get_champion_countries(wimbledon_data)
    print("Wimbledon Champions:")
    return champion_country, champion_to_wins


def read_wimbledon_data():
    """Read and extract the data from wimbledon.csv"""
    with open(FILE_NAME, "r", encoding="utf-8-sig") as in_file:
        lines = in_file.readlines()
        wimbledon_data = [line.strip().split(",") for line in lines[1:]]
    return wimbledon_data

def get_champions(wimbledon_data):
    """Get the wimbledon champions and their amount of wins"""
    champion_to_win = {}
    for line in wimbledon_data:
        champion = line[2]
        if champion in champion_to_win:
            champion_to_win[champion] += 1
        else:
            champion_to_win[champion] = 1
    return champion_to_win

def get_champion_countries(wimbledon_data):
    """Get winning countries from wimbledon data"""
    winning_countries = {line[1] for line in wimbledon_data}
    return winning_countries

main()