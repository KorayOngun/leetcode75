from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxOnes = 0
        zeroCount = 0
        i = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                zeroCount+=1
            while zeroCount > k:
                if nums[i]==0:
                    zeroCount-=1
                i+=1 
            maxOnes = max(maxOnes,j-i+1)
        return maxOnes
nums = [0,0,0,1]
k = 4

sol = Solution()
print(sol.longestOnes(nums,k))

