from unittest import TestCase

from merge_sort_2 import add_element, merge_linked_lists

class TestMergeLinkedLists(TestCase):
    def test_merge_linked_lists(self):
        left_list = {'head': None, 'tail': None}
        right_list = {'head': None, 'tail': None}

        add_element(left_list, 5)
        add_element(left_list, 10)
        add_element(right_list, 2)
        add_element(right_list, 6)

        output = merge_linked_lists(left_list, right_list)

        cur_node = output['head']
        count = 0
        prev_val = None
        while cur_node is not None:
            count += 1

            print(f"Cur value: {cur_node['payload']}")
            
            if prev_val is not None:
                assert cur_node['payload'] > prev_val
                prev_val = cur_node['payload']
            cur_node = cur_node['next_node']

        assert count == 4
