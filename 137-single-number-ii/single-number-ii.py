class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        h={}
        for i in nums:
            if i not in h.keys():
                h[i]=1
            else:
                h[i]=h[i]+1
        
        for key,value in h.items():
            if value!=3:
                return key
