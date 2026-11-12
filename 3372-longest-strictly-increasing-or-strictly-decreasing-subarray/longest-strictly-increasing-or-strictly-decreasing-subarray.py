class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
     ans = 1
     count = 0
     for x in range(len(nums)-1):
        if nums[x] < nums[x+1]:
            if count == 0:
                count += 2
            else:
                count += 1
            ans = max(ans, count)
        else:
            count = 0
     ansd = 1
     count = 0
     for x in range(len(nums)-1):
        if nums[x] > nums[x+1]:
            if count == 0:
                count += 2
            else:
                count += 1
            ansd = max(ansd, count)
        else:
            count = 0
     return max(ans, ansd)
        