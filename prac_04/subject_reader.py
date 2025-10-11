"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Print subject data in a formatted way"""
    subject_data = load_data(FILENAME)
    print(subject_data)
    for i in range(len(subject_data)):
        print(f"{subject_data[i][0]} is taught by {subject_data[i][1]:12} and has {subject_data[i][2]:3}")


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)
    subject_data = []
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        subject_data.append(parts)
        # print(line)  # See what a line looks like
        # print(repr(line))  # See what a line really looks like
        # line = line.strip()  # Remove the \n
        # parts = line.split(',')  # Separate the data into its parts
        # print(parts)  # See what the parts look like (notice the integer is a string)
        # parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        # print(parts)  # See if that worked
        # print("----------")

    input_file.close()
    return subject_data


main()