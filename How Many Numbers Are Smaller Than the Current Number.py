from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        rank = {}
        for idx, val in enumerate(sorted_nums):
            if val not in rank:
                rank[val] = idx
        return [rank[val] for val in nums]