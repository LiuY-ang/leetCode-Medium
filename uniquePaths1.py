# -*- coding:utf-8 -*-
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ans=[[1]*n for i in range(m)]#建立存储结构
        for row in range(1,m):
            for column in range(1,n):
                #到row，column的路径数为其上边位置的路径数和左边位置的路径数之和
                ans[row][column]=ans[row-1][column]+ans[row][column-1]
        return ans[m-1][n-1]#返回到达m，n的路径数量
so=Solution()
print so.uniquePaths(3,3)
