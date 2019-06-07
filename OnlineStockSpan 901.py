# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 21:49:58 2019

@author: haimingwd
"""

class StockSpanner:

    def __init__(self):
        self.histPrice = []
        self.lastLarge = []
        self.cur = -1

    def next(self, price: int) -> int:
        self.cur += 1
        if not self.histPrice:
            self.lastLarge.append(-1)
        elif self.histPrice[-1] > price:
            self.lastLarge.append(self.cur-1)
        else:
            k = self.lastLarge[-1]
            while k >= 0 and self.histPrice[k] <= price:
                k = self.lastLarge[k]
            self.lastLarge.append(k)
        self.histPrice.append(price)
        return self.cur - self.lastLarge[self.cur]
                
# obj = StockSpanner()
# param_1 = obj.next(3)
