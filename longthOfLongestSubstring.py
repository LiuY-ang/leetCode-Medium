#-*- coding:utf-8 -*-
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i,j,length=0,0,len(s)
        maxLength,pos,d=0,{},{}
        start,m=0,-1
        while i<length:
            if pos.get(s[i])==None:#如果s[i]没有出现过
                pos[s[i]]=i #添加到d中
            else:#s[i]已经在d中了
                start=pos[s[i]]+1#获得上一次出现s[i]的位置
                pos[s[i]]=i#更新s[i]出现的位置
                if start<m:#m存储无重复元素的可能子串的最大下标，如果start<m
                    start=m#那么s[start:i+1]肯定有重复元素
                elif start>m:#如果start>m
                    m=start  #更新s
            dis=i-start+1#求出这次无重复元素子串的长度，start为子串的开始位置
            if dis>maxLength:#如果dis较大
                maxLength=dis#那么更新最大长度的值
            i=i+1
        return maxLength
so=Solution()
print so.lengthOfLongestSubstring("pwwkew")
