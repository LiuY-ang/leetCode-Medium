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
        row,column,i=m-1,n-1,0#rowlimit和columnlimit用来存储行，列访问的上限，i存储访问的下界
        while i<=column and i<=row:#访问的下限不能超过上限
            while row>=i:#探测“行首”元素，并一定是真正的行首元素
                if target>=matrix[row][i]:#如果某行的“行首”，大于等于target
                    break#到这个地方停止
                row-=1
            while column>=i:#探测”列首”元素，同样的不一定为真正的列首元素
                if target>=matrix[i][column]:#如果某一列的列首语速小于等于target
                    break#到这个地方停止
                column-=1
            if row<i and column<i:#不存在这个元素
                return False
            if matrix[row][i]==target or matrix[i][column]==target:#探测'行首'和‘列首’处位置，等于target
                return True#则返回true
            i=i+1#访问下限加1
        return matrix[rowlimit][columnlimit]==target
so=Solution()
print so.searchMatrix([
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
],6)
