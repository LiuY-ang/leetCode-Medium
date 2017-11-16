class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        gray=[0]
        for i in range(1,n+1):
            length=len(gray)-1;base=1<<(i-1)
            while length>=0:
                gray.append(gray[length]+base)
                length-=1
        return gray
so=Solution()
print so.grayCode(4)
