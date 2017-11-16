# -*- coding:utf-8 -*-
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length=len(nums)
        if 0 not in nums:#如果nums中没有0元素
            return True#那么可能能够到达最后的位置
        if nums[0]==0 and length>1:#如果第一个数为0的话那么无法到达最后，万一只有一个元素呢？
            return False
        elif nums[0]==0 and length==1:#只有一个元素0
            return True
        #以下的代码用以处理有0的情况
        i=0
        while i<length-1:#如果i>=length-1说明可以到达最后一个位置
            if nums[i]!=0:#如果nums[i]不等于0
                i=i+nums[i]#将i赋值为位置i能达到的最远距离
            else:#如果nums[i]==0
                j=i-1#
                while j>=0 and j+nums[j]<=i:#找到能跨过位置i的位置
                    j=j-1
                if j==-1:#j==-1代表没有找到能跨过位置i的元素
                    return False
                i=j
        return True#执行到这里，说明能够到达最后一个元素
so=Solution()
print so.canJump([3,2,1,0,4])
#[2,3,1,1,4],[3,0,8,2,0,0,1],[2,0,0],[3,2,1,0,4]
