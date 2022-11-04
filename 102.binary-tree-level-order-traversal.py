#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional, List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        list=[]
        
        if not root:
            return []
        if root:
            queue.append(root)
        while queue:
            val=[]
            for i in range(len(queue)):
                node=queue.popleft()
                val.append(node.val)
                if node.left:
                    queue.append(root.left)
                if node.right:
                    queue.append(root.right)
            list.append(val)
        return list
            
# @lc code=end

