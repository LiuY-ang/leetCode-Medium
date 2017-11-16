# -*- coding:utf-8 -*-
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mapping={}
        ans=[]
        for s in strs:
            ss="".join(sorted(s))
            if mapping.get(ss)==None:#是一种全新的同字母异序
                mapping[ss]=[s]
            else:#该同字母异序词已经存在了
                mapping[ss].append(s)
        return [v for v in mapping.itervalues()]
so=Solution()
print so.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
