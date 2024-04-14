# while loop example
# - continues to search boxes iteratively while unsearched boxes exist
# - searches boxes using a flattened approach, loses hierarchical structure
# - recursion can lead to stack overflows as they are memory intensive
# - often less readable than recursion
def find_key(main_box):
    '''finds a key in a box iteratively'''

    pile = main_box.get_search_pile()
    while pile:
        box = pile.get_box()
        for item in box:
            if item.is_box():
                pile.append(item)
            elif item.is_key():
                print('key found!')


# recursive example
# - calls itself recursively when elements in parent boxes are also boxes
# - searches boxes using a nested approach, maintains hierarchical structure
# - iterative approaches efficiently handle memory when compared with recursion
# - often more readable than iteration
def find_key(box):
    '''finds a key in a box recursively'''

    for item in box:
        if item.is_a_box():
            find_key()
        elif item.is_a_key():
            print('key found!')


# countdown example
# - this code will reach maximum recursion depth as no base case is specified
# - recursive funtions require a 'recursive case' and a 'base case'
def errenous_countdown(i):
    '''prints a countdown from i'''

    print(i)
    errenous_countdown(i - 1)

# this code contains a base case and recursive case; it will run correctly
def countdown(i):
    '''prints a countdown from i'''

    print(i)
    if i <= 1:
        return
    else:
        countdown(i - 1)


# call stack example
def greet(name):
    '''prints hello name'''

    def greet_2(name):
        print(f'How are you {name}?')
    
    def bye():
        print('Okay bye!')

    print(f'Hello {name}!')
    greet_2(name)
    print('Getting ready to say bye...')
    bye()


# recursive call stack example
def fact(val):
    '''returns val factorial'''

    if val == 1:
        return 1
    else:
        return val*fact(val - 1)