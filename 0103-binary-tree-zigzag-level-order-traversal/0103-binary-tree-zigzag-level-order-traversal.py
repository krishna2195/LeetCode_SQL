# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue = collections.deque([root])
        res = []
        even_level = False
        while queue:
            n = len(queue)
            level = [0] * n # initalize the array since we know the length
            for i in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if even_level:
                    level[n-1-i] = node.val
                else:
                    level[i] = node.val
            res.append(level)
            even_level = not even_level

        return res