class Solution:
    def minWindow(self, s: str, t: str) -> str:
        td = Counter(t)
        sd = dict()
        valid = 0 
        l = 0
        i,j = -1,-1
        best_len = float('inf')
        for r in range(len(s)):
            ch = s[r]
            sd[ch] = sd.get(ch,0)+1
            if ch in td and sd[ch] == td[ch]:
                valid+=1
            while valid == len(td):
                c = s[l]
                if (r-l+1) < best_len:
                    best_len = r-l+1
                    i,j = l,r+1
                
                sd[c]-=1
                if c in td and sd[c]<td[c]:
                    valid-=1
                l+=1
        return s[i:j]
