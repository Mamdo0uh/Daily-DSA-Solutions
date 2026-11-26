class Solution:
    def canAliceWin(self, n: int) -> bool:
        for i in range(10, 0, -1):
            if n < i:
                return i % 2 == 1
            n -= i