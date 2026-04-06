class Solution:
    def minWindow(self, s: str, t: str) -> str:   
        
        l,r = 0,0
        dt = Counter(t)
        ds = dict()
        valid = 0
        i,j = -1,-1
        min_len = float('inf')
        
        while r<len(s):
            ch = s[r]
            if ch in dt:
                ds[ch] = ds.get(ch,0)+1
                if ds[ch] == dt[ch]:
                    valid+=1
            
            while valid == len(dt):
                if (r-l+1)<min_len:
                    min_len = r-l+1
                    i=l
                    j=r
                if s[l] in ds:
                    ds[s[l]]-=1
                    if ds[s[l]]<dt[s[l]]:
                        valid-=1
                l+=1
                            
            r+=1

        return s[i:j+1] if i != -1 else ""

            


