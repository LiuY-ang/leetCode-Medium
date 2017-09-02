# -*- coding:utf-8 -*-
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        i,length,d=0,len(s),{}
        if len(set(s))==1:
            return s
        maxs=""
        while i<length:#首先统计s中的字符出现的位置
            if d.get(s[i])==None:#如果s[i]在之前未出现过
                d[s[i]]=[i]#那么将该位置添加到d中
            else:#s[i]在之前就已经出现过了
                d[s[i]].append(i)#直接添加该位置
            i=i+1#下标加1
        i=0
        while i<length:
            char=s[i]
            for pos in d[char]:#d[char]返回的是list，该list中存储的是char的位置
                temp=s[i:pos+1]#取得[i,pos]之间的元素
                reverse=temp[::-1]#倒置temp
                if reverse==temp and len(temp)>=len(maxs):#temp是回文串，并且长度较长
                    maxs=temp#那么更新maxs
            d[char].pop(0)#删除第一个元素
            i=i+1
        return maxs
so=Solution()
print so.longestPalindrome("aaabaaaa")
