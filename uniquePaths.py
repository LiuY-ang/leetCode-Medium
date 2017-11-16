# -*- coding:utf-8 -*-
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.count=0
        self.detectPath(1,1,m,n)
        return self.count
    def detectPath(self,down,right,m,n):
        if down==m and right==n:#如果已经走到了m，n的位置
            self.count+=1#将路径数量加1
            return
        elif down>m or right>n:#如果down大于行数或者right大于列数
            return#那么直接返回，因为肯定不能到达m，n位置
        self.detectPath(down+1,right,m,n)#向下走
        self.detectPath(down,right+1,m,n)#向右走
so=Solution()
print so.uniquePaths(12,23)
