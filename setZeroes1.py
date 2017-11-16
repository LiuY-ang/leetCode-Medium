# -*- coding:utf-8 -*-
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        def setColumnZero(column):
            for i in range(0,m):
                matrix[i][column]=0#将该列中所有元素都设置为0
        def setRowZero(row):
            for j in range(0,n):
                matrix[row][j]=0#将该行中的所有元素都设置为0
        m,n=len(matrix),len(matrix[0])
        rowHasZero=False
        columnHasZero=False
        i=0
        while i<n:
            if matrix[0][i]==0:
                rowHasZero=True
                break
            i=i+1
        j=0
        while j<m:
            if matrix[j][0]==0:
                columnHasZero=True
                break
            j=j+1
        #从(1,1)处开始
        for row in range(1,m):
            for column in range(1,n):
                if matrix[row][column]==0:
                    matrix[0][column]=0#将列首元素设置为0
                    matrix[row][0]=0#将行首元素设置为0
        for i in range(1,m):
            if matrix[i][0]==0:#在某一行的行首处的元素为0
                setRowZero(i)#那么将行中的所有元素都设置为0
        for j in range(1,n):
            if matrix[0][j]==0:#在列首的某一元素为0
                setColumnZero(j)#那么将该列的所有元素都设置为0
        if rowHasZero:
            setRowZero(0)#把第一行中的所有元素都设置为0
        if columnHasZero:
            setColumnZero(0)#把第一列中所有元素都设置为0
        print matrix
so=Solution()
print so.setZeroes([[1,0,1],[1,0,1],[1,1,1]])
