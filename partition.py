# -*- coding:utf-8 -*-
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        saved=[];temp=head
        while head and head.val>=x:#将开始大于等于x的元素全部保存到saved中
            saved.append(head.val)
            head=head.next
        #经过上述处理步骤之后，head所在的位置为第一个小于x的位置
        if head==None:#head为空的话，索命所有的元素都大于等于x
            return temp#那么直接将原链表返回
        p=head
        while p.next:#在最后一个元素的位置上终止循环。在本位置，访问下一个位置的值
            if p.next.val>=x:
                saved.append(p.next.val)
                p.next=p.next.next#将下一个位置“删除”
                continue
            p=p.next#p.next.val<x
        print saved
        #顺序建表
        tail=p
        for e in saved:
            temp=ListNode(e)
            tail.next=temp
            tail=temp
        return head
l0=ListNode(1)
so=Solution()
print so.partition(l0,0)
