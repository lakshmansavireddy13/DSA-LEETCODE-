class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s=0
        for i in range(k):
            s=s+nums[i]

        ans=s

        for i in range(k,len(nums)):

            s=s-nums[i-k]

            s=s+nums[i]
            
            ans=max(s,ans)

        return ans/k