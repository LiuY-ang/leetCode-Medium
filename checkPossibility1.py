# -*- coding:utf-8 -*-
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        N = len(nums)
        l = 0
        cnt = 0
        m = float("-Inf")#m指向当前元素的前一个元素
        while l < N-1:
            if nums[l] <= nums[l+1]:#非降序列，符合要求那么继续指向
                m = nums[l]
                l += 1
            else:#nums[l]>nums[l+1],即前边的元素大，这是大前提
                if cnt == 1:#已经修改过一次了，直接结束
                    return False
                cnt += 1#降修改次数加1
                if nums[l+1] >= m:# nums[l]>nums[l+1]>=m,类似3,5,4，即中间的元素最大，后边的元素次之
                    nums[l] = m#那么将中间的元素修改为前一个元素,执行完语句之后变为3,3,4
                else:#nums[l+1]<m,nums[l]>nums[l+1],即最后一个元素的值是最小的，m次之，nums[l]最大，类似：3,5,2
                    nums[l+1] = nums[l]#执行完这条语句后变为3,5,5
                    m = nums[l]#更新m的值
                l += 1
        return True
