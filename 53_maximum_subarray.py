"""Given an integer array nums, find the contiguous subarray (containing at
least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Constraints:
    1 <= nums.length <= 105
    -104 <= nums[i] <= 104

TC: O(n)
SC: O(1)
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max_sum = None
        final_max_sum = None

        for i in range(len(nums)):
            curr_max_sum = nums[i] if curr_max_sum is None else max(nums[i], nums[i] + curr_max_sum)

            if final_max_sum is None:
                final_max_sum = curr_max_sum

            if curr_max_sum > final_max_sum:
                final_max_sum = curr_max_sum

        return final_max_sum
