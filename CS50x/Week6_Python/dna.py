import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print('Usage: python dna.py [database csv file] [sequence txt file]')
        sys.exit(1)
    database_file = sys.argv[1]  # Assign filenames
    sequence_file = sys.argv[2]

    # TODO: Read database file into a variable
    rows = []
    with open(database_file) as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)

    # TODO: Read DNA sequence file into a variable
    with open(sequence_file) as file:
        sequence = file.read()

    # TODO: Find longest match of each STR in DNA sequence
    longest = {}
    keys = rows[0].keys()  # Get sequence names

    for key in keys:
        if key == 'name':  # Skip name col
            continue
        longest[key] = longest_match(sequence, key)  # Get longest match for each sequence

    # TODO: Check database for matching profiles
    keys = longest.keys()

    for row in rows:
        is_match = True

        # Compare all 3 sequences
        for key in keys:
            if int(row[key]) != longest[key]:
                is_match = False
                break

        # If match all 3
        if is_match:
            print(row['name'])
            sys.exit(0)

    # If no matches
    print('No match')
