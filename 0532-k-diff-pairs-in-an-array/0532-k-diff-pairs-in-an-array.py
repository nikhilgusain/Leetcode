class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        d = Counter(nums)
        count=0
        if k == 0 :
            for v in d.values():
                if v>=2:
                    count+=1
            return count
        for it in d.keys():
            if (it + k) in d:
                count+=1
        return count

