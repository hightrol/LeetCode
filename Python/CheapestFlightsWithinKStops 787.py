# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 21:51:50 2019

@author: haimingwd
"""

## Cheapest Flights Within K Stops 787
def findCheapestPrice(n, flights, src, dst, K):
    """
    :type n: int
    :type flights: List[List[int]]
    :type src: int
    :type dst: int
    :type K: int
    :rtype: int
    """
    import collections
    edges = collections.defaultdict(dict)
    for edge in flights:
        s, d, p = edge
        edges[s][d] = p
    cheapest = { i: float('inf') if i != src else 0 for i in range(n) }
    change = {src:0}
    for _ in range(K+1):
        if not change:
            break
        newchange = {}
        for j in change:
            for k in edges[j]:
                newprice = cheapest[j] + edges[j][k]
                if newprice < cheapest[k]:
                    newchange[k] = min(newchange.get(k, float('inf')), newprice)
        cheapest.update(newchange)
        change = newchange
    res = cheapest[dst] 
    return res if res != float('inf') else -1

findCheapestPrice(4, [[0,1,1],[0,2,5],[1,2,1],[2,3,1]], 0, 3, 1)
                    
