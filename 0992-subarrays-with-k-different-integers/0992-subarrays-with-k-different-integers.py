class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def helper(x):
            l,r = 0,0
            dt = dict()
            ans = 0
            while r<len(nums):
                it = nums[r]
                dt[it] = dt.get(it,0)+1

                while len(dt)>x:
                    
                    dt[nums[l]]-=1
                    if dt[nums[l]]==0:
                        del dt[nums[l]]
                    l+=1
                ans+=r-l+1
                r+=1
            return ans
        return helper(k)-helper(k-1)
