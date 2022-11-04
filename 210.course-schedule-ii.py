#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#
from typing import List
# @lc code=start
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #Set up the adjlist for the course and the prerequisites
        adjList={c:[] for c in range(numCourses)}
        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        
        list=[]
        visit, cycle = set(),set()
        def dfs(crs):
            if crs in visit:
                return True
            if crs in cycle:
                return False
            cycle.add(crs)
            for pre in adjList[crs]:
                if dfs(pre)==False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            list.append(crs)
            return True
        for crs in range(numCourses):
            if dfs(crs) == False:
                return []
        return list
                
# @lc code=end

