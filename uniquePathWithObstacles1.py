# -*- coding:utf-8 -*-
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        #下列情况中都是路径条数为0的
        if m==0 or n==0 or obstacleGrid[0][0]==1 or obstacleGrid[m-1][n-1]==1:
            return 0
        rows=[0]*n#用O(n)的存储空间，实现存储O(n*n)个数的功能，长见识了
        rows[0]=1#因为第一个元素肯定不是0
        for row in range(m):
            for column in range(n):
                # print row,column
                if obstacleGrid[row][column]==1:
                    rows[column]=0
                elif column>0:
                    rows[column]+=rows[column-1]#这步就是实现存储空间充分利用的保证
        return rows[-1]

so=Solution()
print so.uniquePathsWithObstacles([[0,0]])
