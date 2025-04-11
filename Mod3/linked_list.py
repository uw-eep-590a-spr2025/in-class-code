
### LinkedList Node is a dictionary with 2 keys, payload and next_node
def create_node(data):
    return {'payload': data,
            'next_node': None ,
            'prev_node': None}

## LinkedList is dictionary with 1 key, 'first_elem' pointing at the first
## node in the list
def create_list():
    return {'first_elem': None,
            'tail_elem': None}

def add_to_list(list, data):
    ## Create new node
    new_node = create_node(data)

    ## Tell the current head to point back at the new node
    if list['first_elem']:
        list['first_elem']['prev_node'] = new_node

    ## Tell new_node to point at the current head of the list
    new_node['next_node'] = list['first_elem']

    ## Tell the list to make the new_node the new head of the list
    list['first_elem'] = new_node

def add_to_end_of_list(list, data):
    new_node = create_node(data)

    ## Tell the new node to point back at the last item
    new_node['prev_node'] = list['tail_elem']

    ## Tell the old last item to point forward to the new last item
    if list['tail_elem']:
        list['tail_elem']['next_node'] = new_node

    ## Tell the list to point at the new last item
    list['tail_elem'] = new_node

    if not list['first_elem']:
        list['first_elem'] = new_node

def remove_from_list_3(list, data_to_remove):
    cur_node = list['first_elem']

    while cur_node['payload'] != data_to_remove:
        print(f'{cur_node['payload']}')
        cur_node = cur_node['next_node']

    # Tell prev_node to point to next_node
    cur_node['prev_node']['next_node'] = cur_node['next_node']

    # Tell next_node to point back to prev_node
    cur_node['next_node']['prev_node'] = cur_node['prev_node']

def remove_from_list_2(list, data_to_remove):
    cur_node = list['first_elem']
    prev_node = None

    while cur_node['payload'] != data_to_remove:
        print(f'Cur node has data {cur_node['payload']}')
        prev_node = cur_node
        cur_node = cur_node['next_node']

    prev_node['next_node'] = cur_node['next_node']

def remove_from_list(list, index):
    cur_node = list['first_elem']
    cur_index = 0

    while cur_index < (index - 1):
        cur_node = cur_node['next_node']
        cur_index += 1

    node_to_delete = cur_node['next_node']
    cur_node['next_node'] = node_to_delete['next_node']



my_list = create_list()
print(my_list)

add_to_end_of_list(my_list, 'bike')
print(my_list)

add_to_end_of_list(my_list, 'bus')
add_to_end_of_list(my_list, 'car')
add_to_end_of_list(my_list, 'tram')

# add_to_list(my_list, 'bus')
# add_to_list(my_list, 'car')
# add_to_list(my_list, 'tram')

remove_from_list_3(my_list, 'bus')
print(my_list)