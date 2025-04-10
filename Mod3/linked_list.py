
### LinkedList Node is a dictionary with 2 keys, payload and next_node
def create_node(data):
    return {'payload': data,
            'next_node': None }

## LinkedList is dictionary with 1 key, 'first_elem' pointing at the first
## node in the list
def create_list():
    return {'first_elem': None}

def add_to_list(list, data):
    ## Create new node
    new_node = create_node(data)
    ## Tell new_node to point at the current head of the list
    new_node['next_node'] = list['first_elem']

    ## Tell the list to make the new_node the new head of the list
    list['first_elem'] = new_node

my_list = create_list()
print(my_list)

add_to_list(my_list, 'bike')
print(my_list)

add_to_list(my_list, 'bus')
print(my_list)