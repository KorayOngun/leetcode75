class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        r = []
        for i in candies:
            if i+extraCandies>=maxCandies:
                r.append(True)
            else:
                r.append(False)
        