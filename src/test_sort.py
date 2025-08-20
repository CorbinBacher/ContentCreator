import unittest
from basic_sort import bubble_sort   # replace with your filename

class TestBubbleSort(unittest.TestCase):

    def test_sorted_list(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4]), [1, 2, 3, 4])

    def test_reverse_list(self):
        self.assertEqual(bubble_sort([4, 3, 2, 1]), [1, 2, 3, 4])

    def test_unsorted_list(self):
        self.assertEqual(bubble_sort([5, 2, 9, 1, 3]), [1, 2, 3, 5, 9])

    def test_with_duplicates(self):
        self.assertEqual(bubble_sort([4, 2, 2, 1]), [1, 2, 2, 4])

    def test_with_negatives(self):
        self.assertEqual(bubble_sort([3, -1, -7, 4]), [-7, -1, 3, 4])

if __name__ == "__main__":
    unittest.main()
