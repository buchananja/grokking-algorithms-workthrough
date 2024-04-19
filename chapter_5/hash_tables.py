voted = dict()
def check_voter(name):
    '''checks whether individual has already voted'''

    if voted.get(name):
        print('This user has already voted.')
    else:
        voted[name] = True
        print('This user may vote.')


def name_hash(string, table_size):
    '''
    returns an index based on summation of string ascii values in input string
    moduli size of hash table
    '''

    return sum(ord(char) for char in string) % table_size


def battery_hash(string, table_size):
    '''
    returns an index based on the modulus of the string length and table_size
    '''

    return len(string) % table_size


def author_hash(string, table_size):
    '''
    returns an index based on the squared summation of string ascii values in 
    input string modulo size of hash table
    '''

    return sum(ord(char)**2 for char in string) % table_size