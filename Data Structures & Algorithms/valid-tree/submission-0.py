class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n: return True

        adj = {i:[] for i in range(n)}
        for src, dst in edges: 
            adj[src].append(dst)
            adj[dst].append(src)
        
        visited = set()

        def dfs(v, prev):
            if v in visited: return False
        
            visited.add(v)
            for neighbors in adj[v]:
                if neighbors == prev: continue
                if not dfs(neighbors, v): return False
            
            return True
        
        return dfs(0, -1) and len(visited) == n



        