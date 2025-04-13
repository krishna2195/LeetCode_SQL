from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)

        UNVISITED, VISITING, VISITED = 0, 1, 2
        states = [UNVISITED] * numCourses
        order = []

        def dfs(course):
            if states[course] == VISITED:
                return True
            elif states[course] == VISITING:
                return False
            states[course] = VISITING

            for n in graph[course]:
                if not dfs(n):
                    return False
                    
            states[course] = VISITED
            order.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return order