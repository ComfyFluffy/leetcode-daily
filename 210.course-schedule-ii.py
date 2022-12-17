#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
from collections import defaultdict


class Solution:

    def findOrder(self, numCourses: int,
                  prerequisites: list[list[int]]) -> list[int]:
        self.graph = defaultdict(list)  # a graph for all courses
        self.res = []  # start from empty
        for a, b in prerequisites:
            self.graph[a].append(b)
        self.visited = [0] * numCourses  # DAG detection
        for x in range(numCourses):
            if not self.dfs(x):
                return []
            # continue to search the whole graph
        return self.res

    def dfs(self, node):
        if self.visited[node] == -1:  # cycle detected
            return False
        if self.visited[node] == 1:
            return True  # has been finished, and been added to self.res
        self.visited[node] = -1  # mark as visited
        for x in self.graph[node]:
            if not self.dfs(x):
                return False
        self.visited[node] = 1  # mark as finished
        # add to solution as the course depenedent on previous ones
        self.res.append(node)

        return True


# @lc code=end
print(Solution().findOrder(3, [[0, 1], [0, 2], [1, 2]]))
