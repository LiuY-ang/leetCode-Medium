# -*- coding:utf-8 -*-
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        row,length=0,len(matrix)#从第一行开始
        i,saved=0,[]
        while i<length:#保存下会覆盖掉的元素
            print matrix[i][length-i:length]
            saved.append(matrix[i][length-i:length])
            i=i+1
        print saved
        i=0
        while i<length:
            newRow=matrix[i][0:length-i]+saved[i]#拼接出需要的集合
            print "newRow=",newRow,"matrix=",matrix[i]
            j=0
            while j<length:
                matrix[j][length-i-1]=newRow[j]
                j=j+1
            i=i+1
        return matrix
so=Solution()
print so.rotate([
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
])
