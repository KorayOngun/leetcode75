from typing import List


# 1493. Longest Subarray of 1's After Deleting One Element
# Solved
# Medium
# Topics
# Companies
# Hint
# Given a binary array nums, you should delete one element from it.

# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

# Example 1:

# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
# Example 2:

# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
# Example 3:

# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.
 

# Constraints:

# 1 <= nums.length <= 105
# nums[i] is either 0 or 1.
        


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start = 0
        zeroCount = 0
        longestWindow = 0
        for i in range(len(nums)):
            
            if nums[i] == 0:
                zeroCount = zeroCount + 1
            
            while zeroCount > 1:
                zeroCount =   zeroCount - 1 if nums[start] == 0 else zeroCount
                start = start + 1 
            
            longestWindow = max(longestWindow,i - start)
        
        return longestWindow

liste = [1,1,1,0,1,1,0,1]
sol = Solution()
print(sol.longestSubarray(liste))


# Accepted
# Koray öngün
# Koray öngün
# submitted at Apr 03, 2024 10:09

# Editorial

# Solution
# Runtime
# 471
# ms
# Beats
# 36.41%
# of users with Python3
# Memory
# 20.21
# MB
# Beats
# 14.51%
# of users with Python3