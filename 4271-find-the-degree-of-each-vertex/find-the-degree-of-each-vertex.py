class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        a= []
        for r in matrix:
            degree = sum(r)
            a.append(degree)
        return a        