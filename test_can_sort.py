import importlib

unittest = importlib.import_module('unittest')
bubble_sort = importlib.import_module('bubble_sort')
insertion_sort = importlib.import_module('insertion_sort')
merge_sort = importlib.import_module('merge_sort')
quick_sort = importlib.import_module('quick_sort')
radix_sort = importlib.import_module('radix_sort')
shell_sort = importlib.import_module('shell_sort')


class CanSort(unittest.TestCase):
    midSizeTestCase = [8, 9, 17, 16, 10, 4, 12, 5, 19, 3, 2, 11, 1, 18, 15, 7, 13, 6, 20, 14]
    midSizeSorted = sorted(midSizeTestCase)

    def test_can_sort_all_algorithms(self):
        for algorithm in [bubble_sort, insertion_sort, merge_sort, quick_sort, radix_sort, shell_sort]:
            self.can_sort(algorithm, algorithm.__name__)

    def can_sort(self, algorithm, algorithm_name):
        self.assertEqual([], algorithm([]), algorithm_name)
        self.assertEqual([1], algorithm([1]), algorithm_name)
        self.assertEqual([1, 2], algorithm([2, 1]), algorithm_name)
        if algorithm_name != "radix_sort":  # Radix sort doesn't work with negative numbers
            self.assertEqual([-1, 1, 3], algorithm([1, -1, 3]), algorithm_name)
        self.assertEqual([1, 2, 3, 6], algorithm([6, 3, 1, 2]), algorithm_name)
        self.assertEqual(self.midSizeSorted, algorithm(self.midSizeTestCase), algorithm_name)
