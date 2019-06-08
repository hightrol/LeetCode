# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 11:50:29 2019

@author: haimingwd
"""

## Dijkstra's

def networkDelayTime(times, N, K):
    
    mtx = [ [ 0 if i == j else float('inf') for j in range(N) ] for i in range(N) ]
    for edge in times:
        i, j, t = edge[0], edge[1], edge[2]
        mtx[i-1][j-1] = t
    S, T = {K-1}, { j for j in range(N) if j != K-1 } 
    dist = [ mtx[K-1][j] for j in range(N) ]
    while T:
        i = min(T, key = lambda l:dist[l])
        if dist[i] == float('inf'):
            return -1
        S.add(i)
        T.remove(i)
        for j in T:
            dist[j] = min( dist[j], dist[i] + mtx[i][j] )
    return max(dist)

networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)