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
        row=m-1
        while row>=0:#检查每一行
            if target>=matrix[row][0]:#如果列首元素小于等于target
                break#那么停止循环，因为target所在的行只可能小于等于row
            row-=1
        column=n-1
        while column>=0:#检查每一列
            if target>=matrix[0][column]:#如果列首元素小于等于target
                break#停止循环，target所在的列只可能小于等于column
            column-=1
        #以上两个循环为找target的大体范围
        if matrix[row][0]==target or matrix[0][column]==target:#检查行首和列首元素，因为不检查第一行和第一列
            return True
        i,j=1,1#行，列从(1,1)开始
        #以下为开始循环，行循环的范围为(1,row),列循环的范围为(1,column)
        while i<=row:
            j=1
            while j<=column:
                if matrix[i][j]==target:
                    return True
                j+=1
            i+=1
        return False
so=Solution()
print so.searchMatrix([[]],20)
