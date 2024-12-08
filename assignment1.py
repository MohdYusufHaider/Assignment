#1> Write a code to reverse a string?
def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))

#Q2>Write a code to count the number of vowels in a string?
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

print(count_vowels("hello world"))


#Q3>Write a code to check if a given string is a palindrome or not?
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("racecar"))

#Q4>Write a code to check if two given strings are anagrams of each other?

from collections import Counter

def are_anagrams(s1, s2):
    return Counter(s1) == Counter(s2)

print(are_anagrams("listen", "silent"))

#Q5> Write a code to find all occurrences of a given substring within another string?
def find_all_occurrences(s, sub):
    indices = []
    start = 0
    while start < len(s):
        start = s.find(sub, start)
        if start == -1:
            break
        indices.append(start)
        start += len(sub)
    return indices

print(find_all_occurrences("hello hello world", "hello"))

#Q6>Write a code to perform basic string compression using the counts of repeated characters?

def compress_string(s):
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1
    compressed.append(s[-1] + str(count))
    return "".join(compressed)

print(compress_string("aaabbcddd"))

#Q7> Write a code to determine if a string has all unique characters?
def has_unique_chars(s):
    return len(set(s)) == len(s)

print(has_unique_chars("abcdef"))

#Q8> Write a code to convert a given string to uppercase or lowercase?

def convert_case(s, to_upper=True):
    return s.upper() if to_upper else s.lower()

print(convert_case("hello", to_upper=True))
print(convert_case("HELLO", to_upper=False))

#Q9>Write a code to count the number of words in a string?
def count_words(s):
    return len(s.split())

print(count_words("hello world this is Python"))

#Q10> Write a code to concatenate two strings without using the + operator?
def concatenate_strings(s1, s2):
    return f"{s1}{s2}"

print(concatenate_strings("hello", "world"))

#Q11 Write a code to remove all occurrences of a specific element from a list?
def remove_all_occurrences(lst, elem):
    return [x for x in lst if x != elem]

print(remove_all_occurrences([1, 2, 3, 2, 4], 2))

#Q12 Implement a code to find the second largest number in a given list of integers?
def second_largest(lst):
    unique_numbers = sorted(set(lst), reverse=True)
    return unique_numbers[1] if len(unique_numbers) > 1 else None

print(second_largest([1, 3, 4, 4, 2]))
#Q13  Create a code to count the occurrences of each element in a list and return a dictionary with elements as 
#keys and their counts as values?
from collections import Counter

def count_elements(lst):
    return dict(Counter(lst))

print(count_elements([1, 2, 2, 3, 3, 3]))
#Q14>  Write a code to reverse a list in-place without using any built-in reverse functions?
def reverse_list(lst):
    left, right = 0, len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst

lst = [1, 2, 3, 4]
print(reverse_list(lst))

#Q15>Implement a code to find and remove duplicates from a list while preserving the original order of 
#elements?
def remove_duplicates(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

print(remove_duplicates([1, 2, 2, 3, 4, 3]))
#Q16> Create a code to check if a given list is sorted (either in ascending or descending order) or not?
 def is_sorted(lst):
    return lst == sorted(lst) or lst == sorted(lst, reverse=True)

print(is_sorted([1, 2, 3]))
print(is_sorted([3, 2, 1]))

#Q17 Write a code to merge two sorted lists into a single sorted list?
def merge_sorted_lists(lst1, lst2):
    return sorted(lst1 + lst2)

print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))

#Q18 Implement a code to find the intersection of two given lists?
def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

print(intersection([1, 2, 3], [2, 3, 4]))

#Q19> Create a code to find the union of two lists without duplicates?
def union(lst1, lst2):
    return list(set(lst1) | set(lst2))

print(union([1, 2, 3], [3, 4, 5]))

#Q20> Write a code to shuffle a given list randomly without using any built-in shuffle functions?
import random

def shuffle_list(lst):
    shuffled = lst[:]
    for i in range(len(lst)):
        j = random.randint(0, len(lst) - 1)
        shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
    return shuffled

print(shuffle_list([1, 2, 3, 4, 5]))
#Q21 > Create a code that prompts the user to enter two sets of integers separated by commas. Then, print the 
#intersection of these two sets
def common_elements(tuple1, tuple2):
    return tuple(set(tuple1) & set(tuple2))

# Example usage
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 5, 6, 7)
result = common_elements(tuple1, tuple2)
print(result)  

#Q22> Create a code that prompts the user to enter two sets of integers separated by commas. Then, print the 
#intersection of these two sets
def get_set_input(prompt):
    return set(map(int, input(prompt).split(',')))

def main():
    set1 = get_set_input("Enter the first set of integers separated by commas: ")
    set2 = get_set_input("Enter the second set of integers separated by commas: ")
    
    intersection = set1 & set2
    print(f"The intersection of the two sets is: {intersection}")

if __name__ == "__main__":
    main()

#Q23Write a code to concatenate two tuples. The function should take two tuples as input and return a new 
#tuple containing elements from both input tuples
def concatenate_tuples(tuple1, tuple2):
    return tuple1 + tuple2

# Example usage
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = concatenate_tuples(tuple1, tuple2)
print(result)  

#Q24>Develop a code that prompts the user to input two sets of strings. Then, print the elements that are 
#present in the first set but not in the second set
def difference_of_sets():
    set1 = set(input("Enter the first set of strings separated by commas: ").split(','))
    set2 = set(input("Enter the second set of strings separated by commas: ").split(','))
    result = set1 - set2
    print(f"Elements present in the first set but not in the second set: {result}")

difference_of_sets()
#Q25>Create a code that takes a tuple and two integers as input. The function should return a new tuple 
#containing elements from the original tuple within the specified range of indices?
def slice_tuple(tup, start, end):
    return tup[start:end]

# Example usage
tup = (0, 1, 2, 3, 4, 5)
print(slice_tuple(tup, 1, 4))  # Output: (1, 2, 3)

#Q26> Write a code that prompts the user to input two sets of characters. Then, print the union of these two sets?
def union_of_sets():
    set1 = set(input("Enter the first set of characters separated by commas: ").split(','))
    set2 = set(input("Enter the second set of characters separated by commas: ").split(','))
    result = set1 | set2
    print(f"The union of the two sets is: {result}")

union_of_sets()

#Q27> Develop a code that takes a tuple of integers as input. The function should return the maximum and 
#minimum values from the tuple using tuple unpacking
def min_max_in_tuple(tup):
    return min(tup), max(tup)

# Example usage
tup = (3, 1, 4, 1, 5, 9)
min_val, max_val = min_max_in_tuple(tup)
print(f"Minimum: {min_val}, Maximum: {max_val}")  # Output: Minimum: 1, Maximum: 9

#Q28> Create a code that defines two sets of integers. Then, print the union, intersection, and difference of these 
#two sets?
def set_operations():
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}
    print(f"Union: {set1 | set2}")
    print(f"Intersection: {set1 & set2}")
    print(f"Difference (set1 - set2): {set1 - set2}")

set_operations()

#Q29> Write a code that takes a tuple and an element as input. The function should return the count of 
#occurrences of the given element in the tuple
def count_occurrences(tup, elem):
    return tup.count(elem)

# Example usage
tup = (1, 2, 2, 3, 4, 2)
print(count_occurrences(tup, 2))  # Output: 3

#Q30> Develop a code that prompts the user to input two sets of strings. Then, print the symmetric difference of 
#these two sets?
def symmetric_difference_of_sets():
    set1 = set(input("Enter the first set of strings separated by commas: ").split(','))
    set2 = set(input("Enter the second set of strings separated by commas: ").split(','))
    result = set1 ^ set2
    print(f"The symmetric difference of the two sets is: {result}")

symmetric_difference_of_sets()

#Q31> Write a code that takes a list of words as input and returns a dictionary where the keys are unique words 
#and the values are the frequencies of those words in the input list
from collections import Counter

def word_frequencies(word_list):
    return dict(Counter(word_list))

# Example usage
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
print(word_frequencies(words))  # Output: {'apple': 3, 'banana': 2, 'orange': 1}

#Q32> Write a code that takes two dictionaries as input and merges them into a single dictionary. If there are 
#common keys, the values should be added together
from collections import Counter

def merge_dictionaries(dict1, dict2):
    result = Counter(dict1) + Counter(dict2)
    return dict(result)

# Example usage
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print(merge_dictionaries(dict1, dict2))  # Output: {'a': 1, 'b': 5, 'c': 4}

#Q33> Write a code to access a value in a nested dictionary. The function should take the dictionary and a list of 
#keys as input, and return the corresponding value. If any of the keys do not exist in the dictionary, the 
#function should return None
def access_nested_value(nested_dict, keys):
    current = nested_dict
    for key in keys:
        if key in current:
            current = current[key]
        else:
            return None
    return current

# Example usage
nested_dict = {"a": {"b": {"c": 42}}}
keys = ["a", "b", "c"]
print(access_nested_value(nested_dict, keys))  # Output: 42

#Q34> Write a code that takes a dictionary as input and returns a sorted version of it based on the values. You 
#can choose whether to sort in ascending or descending order

def sort_dict_by_values(d, ascending=True):
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=not ascending))

# Example usage
d = {"apple": 3, "banana": 1, "orange": 2}
print(sort_dict_by_values(d, ascending=True))  # Output: {'banana': 1, 'orange': 2, 'apple': 3}

#Q35> Write a code that inverts a dictionary, swapping keys and values. Ensure that the inverted dictionary 
#correctly handles cases where multiple keys have the same value by storing the keys as a list in the 
#nverted dictionary?
def invert_dictionary(d):
    inverted = {}
    for key, value in d.items():
        if value not in inverted:
            inverted[value] = [key]
        else:
            inverted[value].append(key)
    return inverted

# Example usage
original_dict = {
    "a": 1,
    "b": 2,
    "c": 1,
    "d": 3,
    "e": 2
}

inverted_dict = invert_dictionary(original_dict)
print(inverted_dict)

