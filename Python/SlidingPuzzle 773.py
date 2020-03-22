class Solution:
    def getNeighbors(self, board):
        res = []
        for i in range(2):
            for j in range(3):
                if board[i][j] == 0:
                    for k, l in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                        if 0<=k<2 and 0<=l<3:
                            n = [ [board[x][y] for y in range(3)] for x in range(2) ]
                            n[k][l], n[i][j] = n[i][j], n[k][l]
                            res.append(n)
        return res
    
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        d = 0
        prev = [board]
        target = [[1,2,3],[4,5,0]]
        dist = {tuple((tuple(ea) for ea in board)): 0}
        while (tuple((tuple(ea) for ea in target)) not in dist) and prev:
            new = []
            d += 1
            for b in prev:
                for b0 in self.getNeighbors(b):
                    if tuple((tuple(ea) for ea in b0)) not in dist:
                        dist[tuple((tuple(ea) for ea in b0))] = d
                        new.append(b0)
            prev = new
        return dist.get(tuple((tuple(ea) for ea in target)), -1)
