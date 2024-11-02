from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing_number = sum(range(len(nums)+1)) - sum(nums)
        return missing_number