from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        d = {}
        for i, v in enumerate(temp):
            if v not in d:
                d[v] = i
        output = []
        for num in nums:
            output.append(d[num])
        return output