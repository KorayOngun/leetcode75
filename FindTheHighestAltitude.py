


from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        start = 0
        highestAltitude = 0
        for i in gain:
            start = start + i
            highestAltitude = max(highestAltitude,start)
        return highestAltitude
        

sol = Solution()
liste = [-4,-3,-2,-1,4,3,2]

print(sol.largestAltitude(liste))


