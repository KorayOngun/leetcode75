from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxOnes = 0
        zeroCount = 0
        windowStart = 0
        windowEnd = 0
        while windowEnd < len(nums):
            if nums[windowEnd] == 0:
                zeroCount+=1
            while zeroCount > k:
                if nums[windowStart] == 0:
                    zeroCount-=1
                windowStart+=1
            maxOnes = max(maxOnes,windowEnd-windowStart+1)
            windowEnd+=1
        return maxOnes

nums = [0,0,0,1]
k = 4

sol = Solution()
print(sol.longestOnes(nums,k))

