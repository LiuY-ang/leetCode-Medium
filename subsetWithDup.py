# -*- coding:utf-8 -*-
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length=len(nums)
        mapping={}
        self.ans=[]
        for i in range(length):#对nums中元素进行统计，key为nums中出现的元素，value为一个list，为nums中元素，每重复一次就添加一次
            if mapping.get(nums[i])==None:
                mapping[nums[i]]=[nums[i]]
            else:
                mapping[nums[i]].append(nums[i])
        nums=list(set(nums))#对nums中重复出现的元素进行去重
        for i in range(1,length+1):#依次求得只有1元素的子集，只有2个元素的子集，只有3个元素的子集......
            self.generateSubset(mapping,nums,0,i,[])
        return self.ans+[[]]#结果集添加进空集并返回
    def generateSubset(self,mapping,nums,start,k,path):
        if k==0:#递归到k==0，说明path中的元素正好为i个
            self.ans.append(path)#将path添加到self.ans中
            return
        while start<len(nums):
            length=len(mapping[nums[start]])
            for i in range(1,length+1):##mapping[nums[start]]中的元素不一定全部取得，还有可能只取1个，2个，3个......一个一个的试探
                if i>=k:#如果循环到i>=k,即mapping[nums[start]]中的元素大于k（k为还需要添加的元素个数），
                    self.ans.append(path+mapping[nums[start]][:k])#那么添加k个元素
                    break#结束循环
                else:#i<k
                    self.generateSubset(mapping,nums,start+1,k-i,path+mapping[nums[start]][:i])
            start+=1#依次探测下一个元素
so=Solution()
print so.subsetsWithDup([1,1,2,2])
