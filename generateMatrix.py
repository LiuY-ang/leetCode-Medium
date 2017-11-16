# -*- coding:utf-8 -*-
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans=[[0]*n for i in range(n)]#构造存储
        # print ans
        count,i=0,0
        row,column=0,0
        while count<n*n:
            while column<=n-1-i:#访问最上边未访问过的行，并且一直访问到最后一个元素为止
                count=count+1
                ans[row][column]=count
                column=column+1
            if count==n*n:#如果访问了这一行之后正好将矩阵中的元素全部访问完
                break#那么直接返回
            print row,column,ans
            row,column=row+1,column-1#如果没有访问完，那么为访问最右边未访问的列做准备
            while row<=n-1-i:#访问最右边未访问过的列并且一直访问到右列的最后一个元素
                count=count+1
                ans[row][column]=count
                row=row+1
            if count==n*n:
                break
            print row,column,ans
            row,column=row-1,column-1#为访问元素做准备
            while column>=i:#访问最下边未访问过的行并一直访问最后一个元素
                count=count+1
                ans[row][column]=count
                column=column-1
            if count==n*n:
                break
            print row,column,ans
            row,column=row-1,column+1#为访问元素做准备
            while row>i:#访问最左边未访问过的列
                count=count+1
                ans[row][column]=count
                row=row-1
            if count==n*n:
                break
            print row,column,ans
            row,column=row+1,column+1#为访问下一个元素做准备
            i=i+1
        return ans
so=Solution()
print so.generateMatrix(3)
