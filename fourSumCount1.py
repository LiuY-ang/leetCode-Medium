# -*- coding:utf-8 -*-
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        m={}
        for a in A:
            for b in B:
                m[a+b]=m.get(a+b,0)+1
        print m
        count=0
        for c in C:
            for d in D:
                diff=0-(c+d)
                if m.get(diff)!=None and m[diff]!=0:
                    count=count+m[diff]
        return count
so=Solution()
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
print so.fourSumCount([-1,-1],
[-1,1],
[-1,1],
[1,-1])
