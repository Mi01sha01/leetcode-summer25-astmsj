class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = sorted(nums1 + nums2)
        N = len(a)
           

        if N % 2 != 0:
          return a[N // 2  ] / 1
                   
        else:
          return (a[N // 2 - 1] + a[N // 2]) / 2