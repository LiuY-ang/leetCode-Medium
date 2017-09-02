# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1,p2=l1,l2
        ans=ListNode(-1)
        p,carry=ans,0
        while p1 and p2:
            s=p1.val+p2.val+carry
            t=ListNode(s%10)
            carry=s/10
            p.next=t
            p,p1,p2=p.next,p1.next,p2.next
        while p1:
            s=p1.val+carry
            t=ListNode(s%10)
            p.next=t
            carry=s/10
            p,p1=p.next,p1.next
        while p2:
            s=p2.val+varry
            t=ListNode(s%10)
            p.next=t
            carry=s/10
            p,p2=p.next,p2.next
        if carry==1:
            t=ListNode(1)
            p.next=t
        return ans.next
