from typing import List

# 33. Search in Rotated Sorted Array
# Solved
# Medium
# Topics
# Companies
# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1
 

# Constraints:

# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -104 <= target <= 104

# Seen this question in a real interview before?
# 1/4
# Yes
# No
# Accepted
# 2.7M
# Submissions
# 6.5M
# Acceptance Rate
# 40.6%

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) < 4:
            if target in nums:
                return nums.index(target)
            else:
                return -1

        leftIndex = 0
        rightIndex = len(nums) - 1
        pivotIndex = int((leftIndex+rightIndex)/2)  
        while leftIndex < rightIndex - 1:
            if nums[pivotIndex] > nums[rightIndex]:
                leftIndex = pivotIndex
                pivotIndex = int((leftIndex+rightIndex)/2)
            else:
                rightIndex = pivotIndex
                pivotIndex = int((leftIndex+rightIndex)/2)        

        pivotIndex = pivotIndex
        
        if nums[0] <= target and target <= nums[pivotIndex]:
            leftIndex = 0
            rightIndex = pivotIndex
        elif nums[pivotIndex+1] <=target and target <= nums[len(nums)-1]:
            leftIndex = pivotIndex
            rightIndex = len(nums)-1
        else:
            return -1
        midIndex = int((leftIndex+rightIndex)/2)

        while leftIndex < rightIndex - 1:
            if target < nums[midIndex]:
                rightIndex = midIndex
                midIndex = int((leftIndex+rightIndex)/2)
            elif target > nums[midIndex]:
                leftIndex = midIndex
                midIndex = int((leftIndex+rightIndex)/2)
            else:
                return midIndex
        
        if target == nums[leftIndex]:
            return leftIndex
        elif target == nums[rightIndex]:
            return rightIndex

        return -1



nums = [4,5,6,7,0,1,2]

sol = Solution()

print(sol.search(nums,2))

# Accepted
# Koray öngün
# Koray öngün
# submitted at Apr 05, 2024 20:46

# Editorial

# Solution
# Runtime
# 42
# ms
# Beats
# 67.68%
# of users with Python3
# Memory
# 17.10
# MB
# Beats
# 15.64%
# of users with Python3