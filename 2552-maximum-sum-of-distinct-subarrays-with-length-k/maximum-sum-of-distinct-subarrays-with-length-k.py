class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        s=0
        h={}
        for i in range(k):
            s=s+ nums[i]
            if nums[i] not in h:
                h[nums[i]]=1
            else:
                h[nums[i]]+=1
        ans=0
        if len(h)==k:
            ans=max(ans,s)
        for i in range(k,len(nums)):
            s=s-nums[i-k]     ##remove old element from s

            h[nums[i-k]] -= 1
            if h[nums[i-k]] == 0:
                del h[nums[i-k]]

            s=s+nums[i]

            if nums[i] not in h:
                h[nums[i]]=1
            else:
                h[nums[i]]+=1

            if len(h)==k:
                ans=max(ans,s)

        return ans

                



