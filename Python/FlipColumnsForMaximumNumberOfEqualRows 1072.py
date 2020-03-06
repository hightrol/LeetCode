class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        counter = {}
        for vec in matrix:
            n = len(vec)
            num = 0
            for j in vec:
                num *= 2
                num += j
            if num >= 2**(n-1):
                num = 2**n - num - 1
            counter[num] = counter.get(num, 0) + 1
        return max(counter.values())
