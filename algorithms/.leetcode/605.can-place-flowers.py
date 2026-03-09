from operator import ne
from typing import List
#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#

# @lc code=start


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        
        size = len(flowerbed)

        for i in range(size):
            previous_pos = flowerbed[i-1] if i-1 >= 0 else 0
            current_pos = flowerbed[i]
            next_pos = flowerbed[i+1] if i+1 <= size-1 else 0
            if previous_pos == 0 and current_pos == 0 and next_pos == 0:
                flowerbed[i] = 1
                n = n - 1

            if n == 0:
                return True
        
        return False
# @lc code=end
