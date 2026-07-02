class Solution:
    def removeStars(self, s: str) -> str:
        
        a=[]
        for i in s:
            if i is not '*':
                a.append(i)
            else:
                a.pop()

        s=''
        for i in a:
            s=s+i
        return s