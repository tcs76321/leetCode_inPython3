# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.DFS(root.left, root.right, 0)
        return root

    def DFS(self, left, right, level):
        level += 1
        if left is None:
            return
        elif level % 2 == 1:
            swap = left.val
            left.val = right.val
            right.val = swap
        self.DFS(left.left, right.right, level)
        self.DFS(left.right, right.left, level)
