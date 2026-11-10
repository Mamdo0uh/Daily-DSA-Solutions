class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        d = [0] * (n + 1)
        for i in range(1, n + 1):
            d[i] = float('inf')
            for jump in range(1, 4):
                prev = i - jump
                if prev >= 0:
                    cost = costs[i - 1] + jump * jump
                    d[i] = min(d[i], d[prev] + cost)
        return d[n]