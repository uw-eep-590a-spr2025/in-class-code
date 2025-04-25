from unittest import TestCase

from merge_sort_2 import add_element, merge_linked_lists, combine_linear


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


class Test(TestCase):
    def test_combine_linear(self):
        left = [1, 3, 5, 7, 9]
        right = [2, 4, 6, 8]

        actual_output = combine_linear(left, right)

        desired_out = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        assert actual_output == desired_out


    def test_combine_linear_left_is_longer(self):
        left = [1, 3, 5, 7, 9, 11, 13]
        right = [2, 4, 6, 8]

        actual_output = combine_linear(left, right)

        desired_out = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13]
        assert actual_output == desired_out

    def test_combine_linear_right_is_longer(self):
        left = [1, 3, 5]
        right = [2, 4, 6, 8, 10, 12, 14]

        actual_output = combine_linear(left, right)

        desired_out = [1, 2, 3, 4, 5, 6, 8, 10, 12, 14]
        assert actual_output == desired_out

    def test_combine_linear_empty_lists(self):
        left = []
        right = []

        actual_output = combine_linear(left, right)

        desired_out = []
        assert actual_output == desired_out

    def test_combine_linear_left_is_empty(self):
        left = []
        right = [2, 4, 6, 8]

        actual_output = combine_linear(left, right)

        desired_out = [2, 4, 6, 8]
        assert actual_output == desired_out