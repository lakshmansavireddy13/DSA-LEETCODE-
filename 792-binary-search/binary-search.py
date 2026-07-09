class Solution:
    def search(self, nums: List[int], a: int) -> int:
        i = 0
        j = len(nums) - 1

        while i <= j:
            mid = (i + j) // 2

            if nums[mid] == a:
                return mid
            elif a>nums[mid]:
                i = mid + 1
            else:
                j = mid - 1

        return -1

    #or
    #    if target not in nums:
    #         return -1
    #     a=nums
    #     for i in range(len(nums)):
    #         if nums[i]==target:
    #             return i 
        

        