from typing import List, Dict, Set, Tuple

def find_second_largest(numbers: List[int]) -> int:
    """
    Q1: Implement a function to find the second largest number in a list.
    Example: [5, 2, 8, 1, 9, 3] → 8
    """
    numbers.sort()
    return numbers[-2]

def count_vowels(text: str) -> int:
    """
    Q2: Implement a function to count the number of vowels (a,e,i,o,u) in a string.
    Example: "Hello World" → 3
    """
    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1
    return count

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    Q3: Implement a function to remove duplicates from a list while maintaining order.
    Example: [1, 2, 2, 3, 4, 4, 5] → [1, 2, 3, 4, 5]
    """
    return list(set(numbers))

def dict_keys_to_sorted_list(d: Dict) -> List[str]:
    """
    Q4: Implement a function to convert dictionary keys to a sorted list.
    Example: {"z": 1, "a": 2, "b": 3} → ["a", "b", "z"]
    """
    return sorted(list(d))

def tuple_sum(numbers: Tuple[int, ...]) -> int:
    """
    Q5: Implement a function to calculate the sum of all numbers in a tuple.
    Example: (1, 2, 3, 4, 5) → 15
    """
    return sum(numbers)

def rotate_list(numbers: List[int], k: int) -> List[int]:
    """
    Q6: Implement a function to rotate a list by k positions.
    Example: ([1, 2, 3, 4, 5], 2) → [4, 5, 1, 2, 3]
    """
    pass

def is_palindrome(text: str) -> bool:
    """
    Q7: Implement a function to check if a string is a palindrome (ignoring spaces and case).
    Example: "A man a plan a canal Panama" → True
    """
    pass

def merge_dicts(dict1: Dict[str, int], dict2: Dict[str, int]) -> Dict[str, int]:
    """
    Q8: Implement a function to merge two dictionaries with sum of values for common keys.
    Example: {"a": 1, "b": 2}, {"b": 3, "c": 4} → {"a": 1, "b": 5, "c": 4}
    """
    pass

def symmetric_diff(set1: Set[int], set2: Set[int]) -> Set[int]:
    """
    Q9: Implement a function to find symmetric difference between two sets.
    Example: {1, 2, 3, 4}, {3, 4, 5, 6} → {1, 2, 5, 6}
    """
    pass

def flatten_list(nested_list: List) -> List:
    """
    Q10: Implement a function to flatten a nested list.
    Example: [1, [2, 3, [4, 5]], 6] → [1, 2, 3, 4, 5, 6]
    """
    pass

def deep_get(d: Dict, path: str) -> any:
    """
    Q11: Implement a function to get value from nested dictionary using path string.
    Example: {"user": {"address": {"city": "Boston"}}}, "user.address.city" → "Boston"
    """
    pass

def custom_sort(words: List[str]) -> List[str]:
    """
    Q12: Implement a function to sort list of strings by length and lexicographically.
    Example: ["banana", "apple", "cherry", "date"] → ["date", "apple", "banana", "cherry"]
    """
    pass

def count_overlapping_patterns(text: str, pattern: str) -> int:
    """
    Q13: Implement a function to count overlapping occurrences of a pattern in a string.
    Example: "aaaaa", "aa" → 4
    """
    pass

def process_tuple_of_tuples(data: Tuple[Tuple]) -> Dict:
    """
    Q14: Implement a function to convert tuple of tuples to dictionary.
    Example: ((1, "a"), (2, "b"), (3, "c")) → {1: "a", 2: "b", 3: "c"}
    """
    pass

def longest_consecutive_sequence(numbers: Set[int]) -> int:
    """
    Q15: Implement a function to find length of longest consecutive sequence in a set.
    Example: {100, 4, 200, 1, 3, 2, 5} → 5 (sequence: 1,2,3,4,5)
    """
    pass
