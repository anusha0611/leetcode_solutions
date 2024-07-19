"""
Problem Statement

For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t(i.e., t is concatenated
with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example
1:Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example
2: Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example
3: Input: str1 = "LEET", str2 = "CODE"
Output: ""

Constraints:
1) 1 <= str1.length, str2.length <= 1000
2) str1 and str2 consist of English uppercase letters.

"""

import math


def gcd_of_strings(str1, str2):
    # Function to check if s1 can be formed by repeating s2
    def check(s1, s2):
        if len(s1) % len(s2) != 0:
            return False
        repeat_count = len(s1) // len(s2)
        return s2 * repeat_count == s1

    # Compute the GCD of the lengths of str1 and str2
    gcd_length = math.gcd(len(str1), len(str2))

    # Candidate divisor string
    candidate = str1[:gcd_length]

    # Check if candidate divides both strings
    if check(str1, candidate) and check(str2, candidate):
        return candidate
    else:
        return ""


# Example usage
str1 = "ABCABC"
str2 = "ABC"
print(f"Input: str1 = {str1}, str2 = {str2}")
print(f"Output: {gcd_of_strings(str1, str2)}")  # Output: "ABC"

str1 = "ABABAB"
str2 = "ABAB"
print(f"Input: str1 = {str1}, str2 = {str2}")
print(f"Output: {gcd_of_strings(str1, str2)}")  # Output: "AB"

str1 = "LEET"
str2 = "CODE"
print(f"Input: str1 = {str1}, str2 = {str2}")
print(f"Output: {gcd_of_strings(str1, str2)}")  # Output: ""
