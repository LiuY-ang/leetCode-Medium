class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m,n=len(matrix),0
        if m==0:
            return False
        else:
            n=len(matrix[0])
        if n==0:
            return False
        row=m-1
        while row>=0:
            if target>=matrix[row][0]:
                break
            row-=1
        i,j=0,n-1
        print row
        while i<=j:
            mid=(i+j)/2
            if matrix[row][mid]==target:
                return True
            elif matrix[row][mid]>target:
                j=mid-1
            elif matrix[row][mid]<target:
                i=mid+1
        return False
so=Solution()
print so.searchMatrix([[]],13)
