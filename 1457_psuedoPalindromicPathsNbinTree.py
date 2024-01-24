# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        result = 0

        stack = [(root, 0), ]

        while stack:
            node, path = stack.pop()

            path = path ^ (1 << node.val)

            if node.left is None and node.right is None:
                if path & (path -1) == 0:
                    result += 1
            else:
                if node.left:
                    stack.append((node.left, path))
                if node.right:
                    stack.append((node.right, path))

        return result



# My brain hurts,
# had to use the editorial yet again :[
# however, I added a minor optimization
# --------------------------------------
# class Solution:
#     def pseudoPalindromicPaths (self, root: TreeNode) -> int:
#         count = 0
#         stack = [(root, 0) ]
#         while stack:
#             node, path = stack.pop()
#             if node is not None:
#                 # compute occurences of each digit 
#                 # in the corresponding register
#                 path = path ^ (1 << node.val)
#                 # if it's a leaf, check if the path is pseudo-palindromic
#                 if node.left is None and node.right is None:
#                     # check if at most one digit has an odd frequency
#                     if path & (path - 1) == 0:
#                         count += 1
#                 else:
#                     stack.append((node.right, path))
#                     stack.append((node.left, path))
#         return count
# -------------------------------------
# Instead of blindly adding what might be a huge amount of None nodes to the stack by just appending both left and right,
# I added checks before appending and was then able to remove the check for is None.
# Pretty sure this results in same number of ifs BUT it reduces the number of while loops greatly in some cases
