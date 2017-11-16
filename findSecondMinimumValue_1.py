# -*- coding:utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#和左右子树相同的时候才需要递归
#只要有一个不相同的时候就不需要递归
class Solution(object):
    def findSecond(self,root,first):
        if root.left and root.right:#左右子树都存在的情况
            if root.left.val != first and root.right.val != first: #值都不相同的情况
                return min(root.left.val,root.right.val)
            else: #值至少有一个相同的情况,无法确定第二小的值在哪，需要继续递归
            #递归，去哪递归？
                leftValue=self.findSecond(root.left,first)#递归的时候应该在某个条件下终止
                rightValue=self.findSecond(root.right,first)
                if leftValue<rightValue and leftValue!=first and leftValue!=-1:
                    return leftValue
                elif rightValue!=first  and rightValue!=-1:
                    return rightValue
                else:
                    return -1
            #执行到这，说明左右子树至少有一个是和first不同的,则second一定在这.不一定在这，应该继续递归
            #只有左右两个节点都不同的时候才能确定
        return root.val#左右子树都为空的时候，则返回本节点的值
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root.left==None:#只有一个节点
            return -1;
        return self.findSecond(root,root.val)
