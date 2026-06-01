class Solution:
    """
    @param n: the number of vertices
    @param edges: the edges of undirected graph
    @return: the number of connected components
    """
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        par = [i for i in range(n)] #[0,1,2,3,4]
        rank = [1] * n

        def findroot(node):
            root = node

            while root != par[root]: # if the root is not the parent itself.
                par[root] = par[par[root]] # Optimization
                root = par[root] 

            return root
        
        def union(n1, n2):
            p1, p2 = findroot(n1), findroot(n2)

            if p1 == p2: return 0 # didn't perform the union.

            if rank[p1] > rank[p2]: # p1's gonna be parent
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            
            return 1
        
        res = n
        for src, dst in edges:
            res -= union(src, dst)
        return res
                