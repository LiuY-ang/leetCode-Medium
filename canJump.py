# -*- coding:utf-8 -*-
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return self.canReachLast(0,nums)
    def canReachLast(self,index,nums):
        if index>=len(nums)-1:#如果大于等于最后一个元素的位置
            return True#
        i=nums[index]#从最大的开始
        while i>0:
            if self.canReachLast(index+i,nums)==True:#如果能够到达最后的话
                return True
            i=i-1
        return False#循环结束后，执行到此说明不能到达最后
so=Solution()
print so.canJump([2,0,0])
