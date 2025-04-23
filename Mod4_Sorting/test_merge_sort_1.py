from unittest import TestCase

from merge_sort_1 import merge, mergesort


class TestMerge(TestCase):

    def test_merge_small(self):
        data = [5, 1]
        low = 0
        high = 1
        mid = 0

        merge(data, low, mid, high)

        print(data)
        assert data[0] == 1
        assert data[1] == 5

    def test_merge(self):
        data = [5, 6, 7, 1, 2, 3]
        low = 0
        high = len(data) - 1
        mid = 2

        merge(data, low, mid, high)

        print(data)
        assert data == [1, 2, 3, 5, 6, 7]


class TestMergeSort(TestCase):
    def test_mergesort(self):
        data = [5, 2, 8, 1]

        mergesort(data, 0, len(data) - 1)

        assert data == [1, 2, 5, 8]

    def test_mergesort_small(self):
        data = [5]
        mergesort(data, 0, 0)
        assert data == [5]

    def test_mergesort_empty(self):
        data = []
        mergesort(data, 0, len(data) - 1)
        assert data == []

    def test_mergesort_two(self):
        data = [2, 1]
        mergesort(data, 0, len(data) - 1)
        assert data == [1, 2]

    def test_mergesort_sorted(self):
        data = [1, 5, 7, 13, 34, 46, 78]
        mergesort(data, 0, len(data) - 1)

        assert data ==  [1, 5, 7, 13, 34, 46, 78]