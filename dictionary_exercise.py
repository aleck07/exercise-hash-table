# When do I use a dictionary?
# The program below has a common code smell. If only the author
# knew how to leverage an appropriate data structure!
# (In this situation, we'll use a Python dictionary, which is a
# specific implementation of a hash table.)


def song_lengths(name):
    if name == 'Stairway To Heaven':
        return 480
    elif name == 'Cover Me In Sunshine':
        return 282
    elif name == 'I Wanna Be Sedated':
        return 140
    elif name == 'Seven Nation Army':
        return 238
    elif name == 'Irreplaceable':
        return 484
    elif name == 'Blinding Lights':
        return 272
    elif name == 'Dont Start Now':
        return 181
    elif name == 'Panini':
        return 132
    elif name == 'Bad Guy':
        return 245

print(song_lengths('Panini'))


# Refactor this code using a Python dictionary. Your program
# should print the song_length associated with 'Panini'.
# Hint 0: https://www.w3schools.com/python/python_dictionaries.asp

# Hint 1: Declare a dictionary with all the song names-song length pairs
songs = {
    'Stairway To Heaven': 480,
    'Cover Me In Sunshine': 282,
    'I Wanna Be Sedated': 140,
    'Seven Nation Army': 238,
    'Irreplaceable': 484,
    'Blinding Lights': 272,
    'Dont Start Now': 181,
    'Panini': 132,
    'Bad Guy': 245
}

# Hint 2: Write one line of code that prints the song length of the song Panini (use the dictionary you created).

print(songs['Panini'])


# In this exercise, we're manually seeding the data in the dictionary, and that takes up a few lines of code. 
# In real-world situations, we might be retrieving data from somewhere, to populate the k-v pairs in the dictionary, 
# with very little code.