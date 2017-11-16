# -*- coding:utf-8 -*-
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        temp=[[l for l in r] for r in matrix]
        # print temp,matrix
        m,n=len(matrix),len(matrix[0])
        for row in range(m):
            for column in range(n):
                if temp[row][column]==0:
                    print row,column
                    i=0
                    while i<n:#设置行元素为0,改变列元素
                        matrix[row][i]=0
                        i+=1
                    i=0
                    while i<m:#改变行元素
                        matrix[i][column]=0
                        i+=1
        print matrix
so=Solution()
print so.setZeroes([[1,0,2],[1,2,3,],[4,5,6]])
