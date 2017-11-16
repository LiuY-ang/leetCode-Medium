# -*- coding:utf-8 -*-
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n=len(grid),len(grid[0])
        ans=[[l for l in r] for r in grid]
        for row in range(1,m):#处理第一列
            ans[row][0]=ans[row-1][0]+ans[row][0]
        for column in range(1,n):#处理第一行
            ans[0][column]=ans[0][column-1]+ans[0][column]
        row,column=1,1
        for row in range(1,m):
            for column in range(1,n):
                ans[row][column]=min(ans[row-1][column],ans[row][column-1])+ans[row][column]
        return ans[m-1][n-1]
so=Solution()
print so.minPathSum([[1,2,3],[1,8,1],[3,2,1]])
