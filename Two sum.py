"""This is a solution for LeetCode problem number 167, Titled: Two Sum"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
             hm={}
             for i,j in enumerate(nums):
                 diff=target -j
                 if diff in hm:
                     return [hm[diff],i]
                 hm[j]=i
        



        
