"""
Problem Statement

Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower
and upper cases, more than once.

Example 1:
Input: s = "hello"
Output: "holle"

Example 2:
Input: s = "leetcode"
Output: "leotcede"

Constraints:
1) 1 <= s.length <= 3 * 105
2) s consist of printable ASCII characters.

"""


def reverse_vowels(s):
    vowels = set("aeiouAEIOU")
    s = list(s)
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and s[left] not in vowels:
            left += 1
        while left < right and s[right] not in vowels:
            right -= 1

        if left < right:
            # Swap vowels
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    return ''.join(s)


# Example usage:
s1 = "hello"
print(f"Input: s = {s1}")
print(f"Output: {reverse_vowels(s1)}")  # Output: "holle"

s2 = "leetcode"
print(f"Input: s = {s2}")
print(f"Output: {reverse_vowels(s2)}")  # Output: "leotcede"
