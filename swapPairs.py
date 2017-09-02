# -*- coding:utf-8 -*-
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p=head
        if head==None:#链表为空
            return head
        elif head.next==None:#只有一个节点
            return head
        head=p.next
        ans=ListNode(0)
        preNode=ans
        while p!=None:
            pp=p.next
            if pp!=None:
                p.next=pp.next
                pp.next=p
                preNode.next=pp
            preNode=p
            p=p.next
        return ans.next #需要返回头节点
