from typing import List

#[1,2,3,4,5]

#[1,1,2,6,24]

#[120,60,40,30,24]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = 1
        right = 1
        result = [1] * len(nums)
        for i in range(len(nums)):
            result[i] = left
            left*=nums[i]

        for i in range(len(nums)-1,-1,-1):
            result[i]*=right
            right*=nums[i]
        
        return result



s= [1,2,3,4]
solution = Solution()
solution.productExceptSelf(s)


"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)




Koray öngün
Nov 21, 2023 21:47

Details
Solution
Python3
Runtime
188 ms
Beats
80.56%
Memory
24.2 MB
Beats
40.79%
"""