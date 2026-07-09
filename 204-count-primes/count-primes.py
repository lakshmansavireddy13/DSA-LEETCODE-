class Solution:
    def countPrimes(self, n: int) -> int:
        if n==0 or n==1:
            return 0
        
        a=[0 for i in range(n)]
        for i in range(2,n+1):
            for j in range(i+i,n,i):
                a[j]=1
        count=0
        for i in range(2,n):
            if a[i]==0:
                count+=1
        return count
