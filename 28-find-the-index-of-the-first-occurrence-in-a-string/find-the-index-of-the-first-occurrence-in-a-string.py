class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        haystack=haystack.replace(needle,'+')

        s=0
        for i in haystack:
            if i=='+':
                return s
            s=s+1
        return -1