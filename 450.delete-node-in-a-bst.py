#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
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
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def minValueNode(root):
            curr =root
            while curr and curr.left:
                curr =curr.left
            return curr
        if not root:
            return
        #Finding the key value to delete
        if key > root.val:
            root.right= self.deleteNode(root.right,key)
        elif key < root.val:
            root.left=self.deleteNode(root.left,key)
        #Found
        else:
            #Case 1: There is 1 or 0 children
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minNode=minValueNode(root.right)
                root.val=minNode.val
                root.right=self.deleteNode(root.right,minNode.val)
        return root
            
            
# @lc code=end

