# -*- coding:utf-8 -*-
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.ans=[]#用来存储结果
        mapping={}
        for e in nums:#统计元素的个数，这样能够保证重复的元素在一起，在一起出现。比如[1,1,2]
            mapping[e]=mapping.get(e,0)+1#能够连续出现[1,1,2]和[2,1,1]
        self.generatePermutations(mapping,[],len(nums))
        return self.ans
    def generatePermutations(self,mapping,path,length):
        if length==0:#如果nums中的所有元素都已经在path中了
            #print path
            self.ans.append(path)#那么将path添加到self.ans中
            return
        for e in mapping:#对重复的元素只循环一次，无重复的元素也只循环一次了。比如[1,1,2]
            if mapping[e]==0:#这样能保证排列[1,2,1]出现。在循环完[1,1,2]之后，在第二层递归处
                continue#因为已经对1已经递归完成，所以下次进行的递归的元素是2。因为对重复的元素只进行一次递归
            else:
                mapping[e]=mapping[e]-1
                self.generatePermutations(mapping,path+[e],length-1)
                mapping[e]=mapping[e]+1
so=Solution()
print so.permuteUnique([1,1,2])
