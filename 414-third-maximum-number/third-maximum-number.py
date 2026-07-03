class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a=set(nums)
        if len(a)<3:
            return max(a)
        else:
            a=list(a)
            a.sort()
            return a[-3]