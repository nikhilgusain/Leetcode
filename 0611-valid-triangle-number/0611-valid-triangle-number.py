class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count=0
        for r in range(n-1,1,-1):
            j = r-1
            i = 0
            while i<j:
                if (nums[i]+nums[j]) > nums[r]:
                    count+= (j-i)
                    j-=1
                    
                else:
                    i+=1
        return count
