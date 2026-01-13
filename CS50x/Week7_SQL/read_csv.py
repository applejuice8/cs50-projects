import csv

with open('favorites.csv', 'r') as file:
    reader = csv.DictReader(file)
    counts = {}

    for row in reader:
        favourites = row['language']
        if favourites in count:
            counts[favourites] += 1
        else:
            counts[favourites] = 1

# Sort by counts
for favourite in sorted(counts, key=counts.get, reverse=True):
    print(f'{favourite}: {counts[favourite]}')