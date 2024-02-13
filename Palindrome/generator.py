import random
import string

import os
import sys
sys.path.append(os.path.abspath("./"))
from utils.utils import writeProblem

def generate_random_string(length):
    """Generates a random string of given length."""
    return ''.join(random.choices(string.ascii_letters + string.digits + ' ', k=length))

def create_palindrome(max_length):
    """Creates a palindrome string of up to max_length characters."""
    half_length = random.randint(1, max_length // 2)
    first_half = generate_random_string(half_length)
    # Ensure the middle character is not a space for odd-length palindromes
    middle = random.choice(string.ascii_letters + string.digits) if max_length % 2 else ''
    return first_half + middle + first_half[::-1]

def create_non_palindrome(max_length):
    """Creates a non-palindrome string of up to max_length characters."""
    while True:
        s = generate_random_string(max_length)
        if s != s[::-1]:
            return s

def generate_test_cases(num_cases, max_length):
    """Generates palindrome and non-palindrome test cases."""
    test_cases = []
    for _ in range(num_cases // 2):
        test_cases.append((create_palindrome(max_length), "YES"))
    for _ in range(num_cases // 2, num_cases):
        test_cases.append((create_non_palindrome(max_length), "NO"))
    return test_cases

# Example of generating 10 test cases with a maximum length of 100 characters each
num_cases = 10
max_length = 100000
test_cases = generate_test_cases(num_cases, max_length)

input_data = []
output_data = []

for i, (test_case, expected) in enumerate(test_cases, 1):
    input_data.append([test_case])
    output_data.append(expected)

writeProblem(os.getcwd() + "/Palindrome", input_data, output_data)
    # print(f"Test Case {i}: Input: '{test_case}' | Expected Output: '{expected}'")
