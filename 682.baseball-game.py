#
# @lc app=leetcode id=682 lang=python3
#
# [682] Baseball Game
#
from typing import List
# @lc code=start
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        total=0
        for n in operations:
            if n == 'x':
                stack=[];
            elif n== '+':
                total+=stack.pop()
                total+=stack.pop()
            elif n=='D':
                total+=stack.pop()
                
# @lc code=end

