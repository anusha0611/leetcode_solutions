"""
Problem Statement

Given an integer array nums, return true if there exists
a triple of indices (i, j, k) such that i < j < k and
nums[i] < nums[j] < nums[k]. If no such indices exists, return false.


Example 1:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.


Constraints:
1) 1 <= nums.length <= 5 * 10pow(5)
2) 2pow(31) <= nums[i] <= 2pow(31) - 1

"""


def increasing_triplet(nums):
    if len(nums) < 3:
        return False

    # Initialize the smallest and second smallest numbers to infinity
    first_min = float('inf')
    second_min = float('inf')

    for num in nums:
        if num <= first_min:
            first_min = num  # Update first_min to the smallest number so far
        elif num <= second_min:
            second_min = num  # Update second_min to the second smallest number so far
        else:
            # If we find a number greater than both first_min and second_min
            return True

    return False


# Example usage:
nums1 = [1, 2, 3, 4, 5]
nums2 = [5, 4, 3, 2, 1]
nums3 = [2, 1, 5, 0, 4, 6]

print(increasing_triplet(nums1))  # Output: True
print(increasing_triplet(nums2))  # Output: False
print(increasing_triplet(nums3))  # Output: True
