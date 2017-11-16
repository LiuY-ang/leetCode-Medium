# -*- coding:utf-8 -*-
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        factorial=[1,1,2,6,24,120,720,5040,40320]
        nums=range(1,n+1)
        k=k-1
        permutation=""
        while n>0:
            n=n-1
            i,k=divmod(k,factorial[n])#分别取得商和余数
            # print i,k,n,permutation,nums[i]
            permutation=permutation+str(nums[i])
            nums.remove(nums[i])
        return permutation
so=Solution()
print so.getPermutation(1,1)
