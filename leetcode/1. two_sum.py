from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, v in enumerate(nums):
            if (target - v) in num_map:
                return i, num_map[target - v]
            else:
                num_map[v] = i
                
        