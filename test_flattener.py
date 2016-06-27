from flattener import flattener
import unittest


class TestFlattener(unittest.TestCase):

    def test_none_returns_none(self):
        self.assertEqual(None, flattener.Flattener.flatten(None))

    def test_empty_list(self):
        self.assertEqual([], flattener.Flattener.flatten([]))

    def test_flat_list(self):
        sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(sample_list, flattener.Flattener.flatten(sample_list))

    def test_nested_list(self):
        expected_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        sample_list = [1, 2, 3, 4, [5, 6, 7, 8], 9, 10]
        self.assertEqual(expected_list, flattener.Flattener.flatten(sample_list))

    def test_multiple_nested_lists(self):
        expected_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        sample_list = [1, 2, 3, 4, [5, [6, 7], 8], 9, 10]
        self.assertEqual(expected_list, flattener.Flattener.flatten(sample_list))

    def test_throws_exception_for_none_in_list(self):
        with self.assertRaises(TypeError):
            flattener.Flattener.flatten([3, None])

    def test_throws_exception_for_none_in_nested_list(self):
        with self.assertRaises(TypeError):
            flattener.Flattener.flatten([1, 2, [3, None]])

    def test_throws_exception_for_non_integer_value_in_list(self):
        with self.assertRaises(TypeError):
            flattener.Flattener.flatten([3, "text"])

    def test_throws_exception_for_non_integer_value_in_nested_list(self):
        with self.assertRaises(TypeError):
            flattener.Flattener.flatten([1, 2, [3, "text"]])
            
