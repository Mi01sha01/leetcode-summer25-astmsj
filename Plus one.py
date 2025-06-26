#LeetCode problem 66: Problem Ttile "Plus one"
#Solved by Misha Urgesa during ASTMSJ Summer Bootcamp.
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits=int("".join(map(str,digits)))
        digits+=1
        digits=list(str(digits))
        digits=[int(num) for num in digits ]
        return digits
        
