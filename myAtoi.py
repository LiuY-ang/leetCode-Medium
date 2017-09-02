# -*- coding:utf-8 -*-
class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        '''
        从第一个非空格的字符开始，注意空格，注意正负，只计算第一个字符串中的数字。
        如果第一个非空格序列并不是一个有效的数字序列，或者是因为字符串为空或者仅有空格，那么直接
        '''
        if len(set(s))==0:#仅有空格
            return 0#返回0
        slist=s.split()[0]#取得第一个非空序列
        isNegative=False
        print "slist=",slist
        #处理正负号
        if slist.find('-')==0:#判断是否为负数
            isNegative=True
            slist=slist[1:]#把负号去掉
        elif slist.find('+')==0:
            slist=slist[1:]
        nums,i="",0
        #处理非数字字符
        while i<len(slist):
            if slist[i]<'0' or slist[i]>'9':
                break
            nums=nums+slist[i]
            i=i+1
        print "nums=",nums,"-"
        if nums=="":#过滤之后有可能可为空字符串，所以判断
            return 0
        nums=int(nums)#非空并且仅有数字字符
        if isNegative==True:
            nums=-nums
        if nums>2147483647:
            return 2147483647
        if nums<-2147483648:
            return -2147483648
        return nums
so=Solution()
print so.myAtoi("010")
