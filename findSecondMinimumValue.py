# -*- coding:utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inOrder(self,root):
        if root:
            self.inOrder(root.left)
            self.inSeq.append(root.val)
            self.inOrder(root.right)

    def findSecondMinimumValue(self, root):#暴力破解
        """
        :type root: TreeNode
        :rtype: int
        """
        self.insqe=[]
        self.inOrder(root)
        self.insqe.sort()
        first=self.seq[0]
        for e in self.insqe:
            if first!=e:
                return e
        return -1
