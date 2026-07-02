class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        x=len(s)//2    #x=3

        count=0
        s=s.lower()
        for i in range(len(s)):

            if s[i]=='a' or s[i]=='e' or  s[i]=='i'  or  s[i]=='o' or  s[i]=='u': 

                if i<x:
                    count=count+1
                else:
                    count=count-1
        if count==0:
            return True
        else:
            return False
