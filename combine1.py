# -*- coding:utf-8 -*-
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k==1:#k==1的时候，即只取一个元素作为组合
            return [ [i] for i in range(1,n+1)]
        elif k==n:#如果k==n，即n个数取n个数组成组合
            return [ [i for i in range(1,n+1)]]
        else:#k>1 and k<n的时候
            ans=[]
            ans+=self.combine(n-1,k)
            part=self.combine(n-1,k-1)
            for ls in part:
                ls.append(n)
            ans+=part
            return ans
so=Solution()
print so.combine(4,3)
