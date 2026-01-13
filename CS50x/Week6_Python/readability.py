from cs50 import get_string

# Prompt
text = get_string('Text: ')

# Initialize
letters = 0
words = 1
sentences = 0

# Iterate every char
for letter in text:
    # Calculate letters
    if letter.upper() >= 'A' and letter.upper() <= 'Z':
        letters += 1

    # Calculate words
    elif letter == ' ':
        words += 1

    # Calculate sentences
    elif letter in ['.', '?', '!']:
        sentences += 1

# Calculate index
# L = Average number of letters per 100 words
# S = Average number of sentences per 100 words
L = letters / words * 100
S = sentences / words * 100
index = round(0.0588 * L - 0.296 * S - 15.8)

# Output
if index < 1:
    print('Before Grade 1')
elif index > 16:
    print('Grade 16+')
else:
    print(f'Grade {index}')