# -*- coding:utf-8 -*-
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m,n=len(matrix),len(matrix[0])
        if n==0:
            return False
        row,column=0,n-1
        while row<m and column>=0:
            if matrix[row][column]==target:#等于target则直接返回
                return True
            elif matrix[row][column]<target:#某一行的最后一个元素，其实也不一定是真正的最后一个元素，小于target
                row+=1#那么需要增大matrix[row][column]的值，故将row加1，因为此时的matrix[row][column]已经是最后一个元素了
            else:#matrix[row][column]>target，需要减小matrix[row][column]的值
                column-=1#将column减1
        return False#执行到这，说明没有找到
so=Solution()
print so.searchMatrix([
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
],22)
