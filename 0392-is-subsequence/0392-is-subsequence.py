class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if len(s) == len(t) == 0:
            return True
        if len(s) == 0:
            return True
        i = 0
        n = len(s)
        for j in range(len(t)):
            if t[j] == s[i]:
                i+=1
            if i==n:
                return True
        return True if i==n else False

