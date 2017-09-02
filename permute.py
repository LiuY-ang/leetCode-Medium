# -*- coding:utf-8 -*-
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #nums.sort()
        self.ans=[]#用来存储结果
        self.generatePermutations(nums,[],[],len(nums))
        return self.ans
    def generatePermutations(self,nums,indexs,path,length):
        if len(indexs)==length:#如果nums中的所有元素都已经在path中了
            self.ans.append(path)#那么将path添加到self.ans中
            return
        for i in range(length):#如果还有部分元素没有添加到path，那么进行循环
            if i not in indexs:#对没有添加的元素进行递归
                self.generatePermutations(nums,indexs+[i],path+[nums[i]],length)
so=Solution()
print so.permute([1,1,2])
