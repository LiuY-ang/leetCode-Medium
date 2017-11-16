# -*- coding:utf-8 -*-
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m=len(obstacleGrid)
        n=0
        if m==0:
            return 0
        else:#m!=0,即行数不为0
            n=len(obstacleGrid[0])
        #该条语句中1-l主要是为了把障碍物变成0,把非障碍物0变成1。第一行和第一列要单独处理
        ans=[ [1-l for l in r] for r in obstacleGrid]
        r=0
        obstacle=1-obstacleGrid[0][0]
        while r<m:#一行一行的处理每行的行首元素，即处理第一列中元素
            if obstacleGrid[r][0]==1:#如果遇到1，即障碍物，则到达该行下边的行首元素的路径条数为0，即都不可到达
                obstacle=0
            ans[r][0]=obstacle
            r+=1
        l=1
        obstacle=1-obstacleGrid[0][0]
        while l<n:#处理第一行中的元素
            if obstacleGrid[0][l]==1:#如果在第一行中有1，即有障碍物，那么到达该元素以右的路径条数为0条
                obstacle=0
            ans[0][l]=obstacle
            l=l+1
        row,column=1,1
        # print ans
        while row<m:
            column=1#每一行从第二元素开始进行
            while column<n:
                if ans[row][column]!=0:#不处理0元素，使其保持为0。只处理非0元素。因为这里的0为有障碍物，无法到达
                    ans[row][column]=ans[row-1][column]+ans[row][column-1]
                column+=1
            row+=1
        return ans[m-1][n-1]
so=Solution()
print so.uniquePathsWithObstacles([[1]])
