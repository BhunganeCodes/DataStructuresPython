import unittest
from typing import List, Dict, Set, Tuple
from collections import defaultdict
from datastructures import *

class DataStructuresTest(unittest.TestCase):
    def setUp(self):
        self.sample_list = [1, 3, 5, 7, 9, 11, 13, 15]
        self.sample_dict = {"apple": 5, "banana": 3, "orange": 7}
        self.sample_string = "Hello World! Python is amazing"
        self.sample_nested_dict = {
            "user": {
                "name": "John",
                "address": {
                    "street": "123 Main St",
                    "city": "Boston"
                }
            }
        }

    def test_list_second_largest(self):
        """Q1: Find the second largest number in a list"""
        numbers = [5, 2, 8, 1, 9, 3]
        result = find_second_largest(numbers)
        self.assertEqual(result, 8)

    def test_string_vowels(self):
        """Q2: Count the number of vowels in a string"""
        text = "Hello World"
        result = count_vowels(text)
        self.assertEqual(result, 3)

    def test_list_duplicates(self):
        """Q3: Remove duplicates from a list while maintaining order"""
        numbers = [1, 2, 2, 3, 4, 4, 5]
        result = remove_duplicates(numbers)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_dict_keys_to_list(self):
        """Q4: Convert dictionary keys to a sorted list"""
        dict_sample = {"z": 1, "a": 2, "b": 3}
        result = dict_keys_to_sorted_list(dict_sample)
        self.assertEqual(result, ["a", "b", "z"])

    def test_tuple_sum(self):
        """Q5: Calculate the sum of all numbers in a tuple"""
        numbers = (1, 2, 3, 4, 5)
        result = tuple_sum(numbers)
        self.assertEqual(result, 15)
        
    def test_list_rotation(self):
        """Q6: Rotate a list by k positions"""
        numbers = [1, 2, 3, 4, 5]
        result = rotate_list(numbers, 2)
        self.assertEqual(result, [4, 5, 1, 2, 3])

    def test_string_palindrome(self):
        """Q7: Check if a string is a palindrome (ignoring spaces and case)"""
        text = "A man a plan a canal Panama"
        result = is_palindrome(text)
        self.assertTrue(result)

    def test_dict_merge(self):
        """Q8: Merge two dictionaries with sum of values for common keys"""
        dict1 = {"a": 1, "b": 2}
        dict2 = {"b": 3, "c": 4}
        result = merge_dicts(dict1, dict2)
        self.assertEqual(result, {"a": 1, "b": 5, "c": 4})

    def test_set_symmetric_difference(self):
        """Q9: Find symmetric difference between two sets"""
        set1 = {1, 2, 3, 4}
        set2 = {3, 4, 5, 6}
        result = symmetric_diff(set1, set2)
        self.assertEqual(result, {1, 2, 5, 6})

    def test_nested_list_flatten(self):
        """Q10: Flatten a nested list"""
        nested = [1, [2, 3, [4, 5]], 6]
        result = flatten_list(nested)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

    def test_dict_deep_get(self):
        """Q11: Get value from nested dictionary using path string"""
        path = "user.address.city"
        result = deep_get(self.sample_nested_dict, path)
        self.assertEqual(result, "Boston")

    def test_list_custom_sort(self):
        """Q12: Sort list of strings by length and lexicographically"""
        words = ["banana", "apple", "cherry", "date", "elderberry"]
        result = custom_sort(words)
        self.assertEqual(result, ["date", "apple", "banana", "cherry", "elderberry"])

    def test_string_pattern_count(self):
        """Q13: Count overlapping occurrences of a pattern in a string"""
        text = "aaaaa"
        pattern = "aa"
        result = count_overlapping_patterns(text, pattern)
        self.assertEqual(result, 4)

    def test_tuple_operations(self):
        """Q14: Perform operations on tuple of tuples"""
        data = ((1, "a"), (2, "b"), (3, "c"))
        result = process_tuple_of_tuples(data)
        self.assertEqual(result, {1: "a", 2: "b", 3: "c"})

    def test_set_consecutive_numbers(self):
        """Q15: Find longest consecutive sequence in a set"""
        numbers = {100, 4, 200, 1, 3, 2, 5}
        result = longest_consecutive_sequence(numbers)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()