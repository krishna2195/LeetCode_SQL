# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getresult(self, root, result, tempresult):
        if root is None:
            return
        tempresult = tempresult * 10 + root.val
        if root.left is None and root.right is None:
            result[0] += tempresult
            return
        self.getresult(root.left, result, tempresult)
        self.getresult(root.right, result, tempresult)

    def sumNumbers(self, root):
        result = [0]  # Using a list to hold the result as a mutable object
        tempresult = 0
        self.getresult(root, result, tempresult)
        return result[0]