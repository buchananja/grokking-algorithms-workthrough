from collections import deque


graph = dict()
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = list()
graph['peggy'] = list()
graph['thom'] = list()
graph['jonny'] = list()


def breadth_first_search(graph, name, target):
    '''performs breadth-first search on a graph'''

    search_queue = deque()
    search_queue += graph[name]
    searched = list()
    step_counter = 0
    
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            step_counter += 1
            if person == target:
                print(f'{target} was found {step_counter} steps from {name}!')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
               
    print(f'{target} was not found!')
    return False


breadth_first_search(graph, 'you', 'bob')