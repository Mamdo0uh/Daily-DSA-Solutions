class Solution:
    def minMoves(self, nums: list[int]) -> int:
      a = min(nums)
      return sum(x - a for x in nums)   