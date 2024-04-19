# 5.1
- f(x) = 1 will consistently return 1 for value x.


# 5.2
- f(x) = rand() will consistently return random numbers, but will not
consistently return the same numbers.


# 5.3
- f(x) = next_empty_slot() will consistently return the index of the next empty
slot in a hash table, but will not consistently return the same indexes.


# 5.4
- f(x) = len(x) will consistently return the length of x values. Assuming x
remains constant, the output of the hash function will remain constant.


# 5.5
- def alphabet_hash(string, table_size):
    '''
    returns an index based on summation of string ascii values in input string
    moduli size of hash table
    '''

    return sum(ord(char) for char in string) % table_size


# 5.6
- 
def battery_hash(string, table_size):
    '''
    returns an index based on the modulus of the string length and table_size
    '''

    return len(string) % table_size


# 5.7
- def author_hash(string, table_size):
    '''
    returns an index based on the squared summation of string ascii values in 
    input string modulo size of hash table
    '''

    return sum(ord(char)**2 for char in string) % table_size