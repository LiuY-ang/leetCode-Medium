# -*- coding:utf-8 -*-
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        pathList=path.split("/")
        length=len(pathList)
        stack=[]
        print pathList
        for i in range(length):
            if pathList[i]=="" or pathList[i]==".":
                continue
            elif pathList[i]=="..":
                if len(stack)!=0:
                    stack.pop()#删除最后一个元素
            else:
                stack.append(pathList[i])
        print stack
        return "/"+"/".join(stack)
so=Solution()
print so.simplifyPath("/home/")
