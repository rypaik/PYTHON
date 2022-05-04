# [MapReduce with Python](https://python.plainenglish.io/mapreduce-with-python-8a20113ab98a)

#!/usr/bin/env python
import sys

# Read each line from stdin
for line in sys.stdin:
    # Get the words in each line
    words = line.split()


# Generate the count for each word
for word in words:
    # Write the key-value pair to stdout to be processed by
    # the reducer.
    # The key is anything before the first tab character and the
    # value is anything after the first tab character.
    print('{0}\t{1}'.format(word, 1))





#!/usr/bin/env python
import sys
curr_word = None
curr_count = 0
# Process each key-value pair from the mapper
for line in sys.stdin:
    # Get the key and value from the current line
    word, count = line.split('\t')
    # Convert the count to an int
    count = int(count)
    # If the current word is the same as the previous word,
    # increment its count, otherwise print the words count
    # to stdout
    if word == curr_word:
        curr_count += count
    else:
    # Write word and its number of occurrences as a key-value
    # pair to stdout
        if curr_word:
            print('{0}\t{1}'.format(curr_word, curr_count))
            curr_word = word
            curr_count = count
    # Output the count for the last word
        if curr_word == word:
            print('{0}\t{1}'.format(curr_word, curr_count))
