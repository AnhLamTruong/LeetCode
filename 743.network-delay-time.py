#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#
from typing import List
import heapq
# @lc code=start
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj={}
        for i in range(1,n+1):
            adj[i]=[]
        for s, d, w in times:
            adj[s].append([d,w])
        minHeap=[[0,k]]
        visit=set()
        t=0
        while minHeap:
            w1,n1=heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t=w1
            for n2, w2 in adj[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        return t if len(visit) == n else -1
            
            
# @lc code=end

