# -*- coding:utf-8 -*-
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans=[]
        i=0
        m=len(matrix)#得到矩阵的行数
        if m==0:#如果没有行元素,即没有元素
            return []#那么直接返回
        n=len(matrix[0])#得到矩阵的列数。m*n
        row,column=0,0
        while len(ans)<m*n:
            while column<=n-1-i:#访问最上边未访问过的行，并且一直访问到最后一个元素为止
                ans.append(matrix[row][column])
                column=column+1
            if len(ans)==m*n:#如果访问了这一行之后正好将矩阵中的元素全部访问完
                break#那么直接返回
            row,column=row+1,column-1#如果没有访问完，那么为访问最右边未访问的列做准备
            while row<=m-1-i:#访问最右边未访问过的列并且一直访问到右列的最后一个元素
                ans.append(matrix[row][column])
                row=row+1
            if len(ans)==m*n:
                break
            row,column=row-1,column-1#为访问元素做准备
            while column>=i:#访问最下边未访问过的行并一直访问最后一个元素
                ans.append(matrix[row][column])
                column=column-1
            if len(ans)==m*n:
                break
            row,column=row-1,column+1#为访问元素做准备
            while row>i:#访问最左边未访问过的列
                ans.append(matrix[row][column])
                row=row-1
            if len(ans)==m*n:
                break
            row,column=row+1,column+1#为访问下一个元素做准备
            i=i+1
        return ans
so=Solution()
print so.spiralOrder([ ])
#[1,2,3],[4,5,6],[7,8,9]
