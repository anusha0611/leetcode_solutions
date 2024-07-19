"""
Problem Statement

You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
and an integer n, return true if n new flowers can be planted in the flowerbed without violating
the no-adjacent-flowers rule and false otherwise.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: false


Constraints:
1) 1 <= flowerbed.length <= 2 * 104
2) flowerbed[i] is 0 or 1.
3) There are no two adjacent flowers in flowerbed.
4) 0 <= n <= flowerbed.length

"""


def can_place_flowers(flowerbed, n):
    count = 0
    i = 0
    while i < len(flowerbed):
        if flowerbed[i] == 0:
            # Check if this position and its neighbors are empty
            if (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                flowerbed[i] = 1  # Place a flower here
                count += 1
                if count >= n:
                    return True
        i += 1
    return count >= n


# Example usage:
flowerbed1 = [1, 0, 0, 0, 1]
n1 = 1
print(f"Input: flowerbed = {flowerbed1}, n = {n1}")
print(f"Output: {can_place_flowers(flowerbed1, n1)}")  # Output: True

flowerbed2 = [1, 0, 0, 0, 1]
n2 = 2
print(f"Input: flowerbed = {flowerbed2}, n = {n2}")
print(f"Output: {can_place_flowers(flowerbed2, n2)}")  # Output: False
