# -*- coding:utf-8 -*-
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        '''
        重复元素的最前或者最后的情况
        '''
        if not head:
            return None
        if head.next==None:
            return head
        first,p=ListNode(-1),head
        tail=first
        while p:
            if p.next:#p不是最后一个位置
                if p.next.val==p.val:#p位置和下一个位置的值相等
                    pre=p
                    while p and pre.val==p.val:#循环直到遇到不等于该位置的值停止
                        p=p.next
                    continue#不执行最后的p=p.next语句
                elif p.val!=p.next.val:#如果和下一个位置的值不相等，那么将该位置的添加到tail中
                    tail.next=p
                    tail=p
            else:#p是最后一个元素，并且和前边位置的元素不等，那么将该元素添加到tail中
                tail.next=p
                tail=p
            p=p.next
        tail.next=None#将下一个指向为空
        return first.next
l1=ListNode(1)
l2=ListNode(2)
l3=ListNode(3)
l4=ListNode(3)
l5=ListNode(5)
l6=ListNode(5)
l1.next=l2
l2.next=l3
l3.next=l4
l4.next=l5
l5.next=l6
so=Solution()
result=so.deleteDuplicates(l1)
while result:
    print result.val,
    result=result.next
