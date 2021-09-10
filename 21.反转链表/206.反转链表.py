# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        """
        :param head:: ListNode
        :return: -> ListNode
        """
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            ### 最重要一步，改变链表的方向
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
