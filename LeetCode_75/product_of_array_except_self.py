"""
Problem Statement

Given an integer array nums, return an array answer such that answer[i] is equal
to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:
1) 2 <= nums.length <= 105
2) -30 <= nums[i] <= 30
3) The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

"""


def product_except_self(nums):
    n = len(nums)

    # Step 1: Initialize the arrays
    left_products = [1] * n
    right_products = [1] * n

    # Step 2: Calculate left products
    for i in range(1, n):
        left_products[i] = left_products[i - 1] * nums[i - 1]

    # Step 3: Calculate right products
    for i in range(n - 2, -1, -1):
        right_products[i] = right_products[i + 1] * nums[i + 1]

    # Step 4: Calculate the result array
    result = [1] * n
    for i in range(n):
        result[i] = left_products[i] * right_products[i]

    return result


# Example usage:
nums1 = [1, 2, 3, 4]
nums2 = [-1, 1, 0, -3, 3]

print(product_except_self(nums1))  # Output: [24, 12, 8, 6]
print(product_except_self(nums2))  # Output: [0, 0, 9, 0, 0]
