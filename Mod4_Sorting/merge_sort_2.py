
## Define a merge function
## Takes in 2 singly linked lists, represented as Python dictionaries
## Assume each input linked list is in sorted (increasing) order
## Output new linked list, such that the output linked list contains
## elements in both inputs, in sorted order.

def add_element(list, value):
    new_node = {'payload': value, 'next_node': None}

    if list['head'] is None:
        list['head'] = new_node

    if list['tail'] is not None:
        list['tail']['next_node'] = new_node
    list['tail'] = new_node

def merge_linked_lists(left_list, right_list):
    out_list = {'head': None, 'tail': None}

    left_pointer = left_list['head']
    right_pointer = right_list['head']

    while left_pointer is not None and right_pointer is not None:

        if left_pointer['payload'] < right_pointer['payload']:
            add_element(out_list, left_pointer['payload'])
            left_pointer = left_pointer['next_node']
        else:
            add_element(out_list, right_pointer['payload'])
            right_pointer = right_pointer['next_node']

    if left_pointer is not None:
        while left_pointer is not None:
            add_element(out_list, left_pointer['payload'])
            left_pointer = left_pointer['next_node']

    if right_pointer is not None:
        while right_pointer is not None:
            add_element(out_list, right_pointer['payload'])
            right_pointer = right_pointer['next_node']

    return out_list

