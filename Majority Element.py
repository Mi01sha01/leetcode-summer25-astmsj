class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c=0
        e=None
        for i in nums:
            if c==0:
                e=i
            c+=(1 if i==e else -1)
        return e


        
