"""
Problem Statement

Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters.
The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between
two words. The returned string should only have a single space separating the words.
Do not include any extra spaces.

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:
Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.


Constraints:
1) 1 <= s.length <= 104
2) s contains English letters (upper-case and lower-case), digits, and spaces ' '.
3) There is at least one word in s.

"""


def reverse_words(s: str) -> str:
    # Step 1: Trim the string
    trimmed_str = s.strip()

    # Step 2: Split the string into words
    words = trimmed_str.split()

    # Step 3: Reverse the list of words
    reversed_words = words[::-1]

    # Step 4: Join the words with a single space
    result = ' '.join(reversed_words)

    return result


# Example usage:
s1 = "the sky is blue"
s2 = "  hello world  "
s3 = "a good   example"

print(reverse_words(s1))  # Output: "blue is sky the"
print(reverse_words(s2))  # Output: "world hello"
print(reverse_words(s3))  # Output: "example good a"

