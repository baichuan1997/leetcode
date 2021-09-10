class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :param l1: ListNode
        :param l2: ListNode
        :return: -> ListNode
        """
        if not l1:
            return l2
        elif not l2:
            return l1
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2