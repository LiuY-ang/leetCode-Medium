# -*- coding:utf-8 -*-
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        listNodes=[]
        p=head
        while p!=None:
            listNodes.append(p)
            p=p.next
        length=len(listNodes)
        if length==1:#如果只有一个元素
            return []
        elif n==1 :#如果要删掉最后一个节点且节点个数大于1个
            listNodes[-2].next=None
            return listNodes[0]
        elif n==length:
            return listNodes[1]
        else:
            listNodes[length-n-1].next=listNodes[length-n+1]#得到前一个节点
            return listNodes[0]
