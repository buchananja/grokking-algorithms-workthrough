# 1.1
- For a sorted list of 128 names, binary search would take 7 steps to find the target in a worst-case scenario.

# 1.2
- For a sorted list of 256 names, binary search would take 8 steps to find the target in a worst-case scenario.

# 1.3
- Searching for a person's name in a phonebook using simple search will take O(n) time.
- Searching for a person's name in a phonebook using binary search will take O(log n) time

# 1.4
- Searching for a person's phone number in a phonebook using simple search will take O(n) time.
- Searching for a person's phone numberin a phonebook using binary search will take O(log n) time

# 1.5
- Searching every phone number in a phone book will take O(n) time.

# 1.6
- Finding the phone numbers of all people who's names begin with "A" could be done by finding the last and first names beginning with A O(log n). Names could then be iterated through and their numbers extracted O(n).
- Alternatively, all names could be iterated through using a simple search and their numbers extracted, this would be more efficient on a sorted list as the first value not to begin with an "A" would terminate the search O(n).
