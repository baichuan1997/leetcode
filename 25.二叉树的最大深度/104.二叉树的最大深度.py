# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def maxDepth(self, root):
        """
        :param root: TreeNode
        :return:  -> int
        """
        ### 1.深度优先算法
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


        ### 2.广度优先算法
        if not root:
            return 0
        queue = collections.deque([root])
        depth = 0
        while queue:
            n = len(queue)

            for i in range(n):
                node = queue.popleft(queue)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.qppend(node.right)
            depth += 1
        return depth
