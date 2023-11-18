class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        counter = 0
        l = len(flowerbed)
        while(i < l):
            if flowerbed[i] == 0 and flowerbed[i-1 if i-1 > 0 else 0] == 0 and flowerbed[i+1 if i+1 < l else l-1] == 0:
                counter+=1
                i+=2
                if counter == n: return True
            else:
                i+=1
        return counter >= n
    

"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length



Koray öngün
Nov 18, 2023 07:31

Details
Solution
Python3
Runtime
138 ms
Beats
95.99%
Memory
16.6 MB
Beats
92.6%

"""