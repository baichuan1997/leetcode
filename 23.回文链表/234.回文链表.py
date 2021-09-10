# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head):
        """
        :param head: ListNode
        :return:  -> bool
        """
        cur = head
        cur_list = []
        while cur:
            cur_list.append(cur.val)
            cur  = cur.next
        return cur_list == cur_list[::-1]


