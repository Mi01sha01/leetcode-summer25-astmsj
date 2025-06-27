""" Here is my  solution in Python3 for LeetCode problem number 136, Titled: Single Numbeer"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i)==1:
                return i
        
