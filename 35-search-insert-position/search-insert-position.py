class Solution:
    def searchInsert(self, a: List[int], x: int) -> int:

        i=0
        while i<=len(a)-1:
            if x > a[i]:
                i=i+1
            else:
                return i
    
        return i
        