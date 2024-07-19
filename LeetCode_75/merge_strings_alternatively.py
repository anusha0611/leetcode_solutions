"""
Problem Statement

You are given two strings word1 and word2.Merge the strings by adding letters in alternating
order, starting with word1.If a string is longer than the other, append the additional letters
onto the end of the merged string.

Return the merged string.

Example
1: Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1: a   b   c
word2:   p   q   r
merged: apbqcr

Example
2: Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1: a  b
word2:   p  q r s
merged: apbqrs

Example
3: Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1: a  b  c  d
word2:   p  q
merged: apbqcd

Constraints:
1) 1 <= word1.length, word2.length <= 100
2) word1 and word2 consists of lowercase English letters.

"""


def merge_alternately(word1, word2):
    # Initialize the merged string
    merged = []
    # Get the lengths of the two words
    len1, len2 = len(word1), len(word2)
    # Iterate over the length of the longer word
    for i in range(max(len1, len2)):
        if i < len1:
            merged.append(word1[i])
        if i < len2:
            merged.append(word2[i])
    # Join the list into a single string and return it
    return ''.join(merged)


# Example usage
word1 = "abc"
word2 = "pqr"
print(f"Input: word1 = {word1}, word2 = {word2}")
print(f"Output: {merge_alternately(word1, word2)}")  # Output: "apbqcr"

word1 = "ab"
word2 = "pqrs"
print(f"Input: word1 = {word1}, word2 = {word2}")
print(f"Output: {merge_alternately(word1, word2)}")  # Output: "apbqrs"

word1 = "abcd"
word2 = "pq"
print(f"Input: word1 = {word1}, word2 = {word2}")
print(f"Output: {merge_alternately(word1, word2)}")  # Output: "apbqcd"
