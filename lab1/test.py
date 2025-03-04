from task import find_unsorted_subarray
import unittest


class TestFindUnsortedSubarray(unittest.TestCase):
    def test_sorted_array(self):
        self.assertEqual(find_unsorted_subarray([1, 2, 3, 4, 5]), (-1, -1))
    
    def test_full_unsorted_array(self):
        self.assertEqual(find_unsorted_subarray([5, 4, 3, 2, 1]), (0, 4))
    
    def test_single_element_array(self):
        self.assertEqual(find_unsorted_subarray([1]), (-1, -1))
    
    def test_example_case(self):
        self.assertEqual(find_unsorted_subarray([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]), (3, 9))
    
    def test_another_unsorted_case(self):
        self.assertEqual(find_unsorted_subarray([1, 3, 5, 8, 6, 7, 9, 10]), (3, 5))
    

if __name__ == "__main__":
    unittest.main()