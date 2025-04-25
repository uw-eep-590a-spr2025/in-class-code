## Define a function
## Takes in 2 sorted singly linked lists
## Outputs 1 sorted singly linked list, such that the output has all the input
##   elements, in sorted order (increasing)

def combine(left_list, right_list):
    combined_list = left_list + right_list  ## O(1)
    return combined_list.sort()             ## O(n log n)
## ==> O(n lg n)

## Now make it linear time ( O(n))
def combine_linear(left_list, right_list):
    left_ptr = 0
    right_ptr = 0
    out = []

    while left_ptr < len(left_list) and right_ptr < len(right_list):

        if left_list[left_ptr] < right_list[right_ptr]:
            ## "put this in output"
            out.append(left_list[left_ptr])
            ## inc left_ptr
            left_ptr += 1
            pass
        else:
            ## put right in output
            out.append(right_list[right_ptr])
            ## inc right_ptr
            right_ptr += 1
            pass

    if left_ptr >= len(left_list):
        ## gotta put everything from right in output
        while right_ptr < len(right_list):
            out.append(right_list[right_ptr])
            right_ptr += 1
    else:
        while left_ptr < len(left_list):
            out.append(left_list[left_ptr])
            left_ptr += 1

    return out







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

