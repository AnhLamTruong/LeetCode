#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack=[]
        cur=root
        while cur and stack:
            while cur:
                stack.append(cur)
                cur=cur.left
            cur = stack.pop()
            k-=1
            if k==0:
                return cur.val
            cur=cur.right
        
# @lc code=end

