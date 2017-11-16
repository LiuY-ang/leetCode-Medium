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
        print m,n
        low,high=0,m*n-1
        while low<=high:
            mid=(low+high)/2
            row,column=mid/n,mid%n
            print row,column
            if matrix[row][column]==target:
                return True
            elif matrix[row][column]>target:
                high=mid-1
            else:#matrix[row][column]<target:
                low=mid+1
        return False
so=Solution()
print so.searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
],16)
