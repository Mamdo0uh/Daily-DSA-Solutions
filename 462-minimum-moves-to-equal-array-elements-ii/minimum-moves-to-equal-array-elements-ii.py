class Solution:
    def minMoves2(self, nums: list[int]) -> int:
       l=len(nums)
       if l==1:
            return 0
       nums.sort()
       mid=nums[l//2]
       r=0
       for i in nums:
            r+=abs(i-mid)
       return r