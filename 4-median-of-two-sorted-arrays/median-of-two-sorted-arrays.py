class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        a=a+b
        a.sort()
        
        i=0
        j=len(a)-1

        while i<j:
            i=i+1
            j=j-1

        if i==j:              ##this is even condition so just return that number
            return a[i]*1.0   ###here we want decimals so we use that 1.0
        else:   
                           ##this is odd condition so we can add both and divide 
            x=a[i]+a[j]
            x=x*1.0
            return x/2
            