class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # construct adjacency list
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            if u not in adj:
                adj[u] = []
            if v not in adj:
                adj[v] = []
            # undirected edges
            adj[u].append(v)
            adj[v].append(u)

        # in order to handle infinite loops
        visited = set()
        
        # does the graph starting from this node form a valid tree?
        def dfs(current_node: int, parent_node: int) -> bool:
            # We can detect cycles by checking if we visit a node again from a path other than its parent
            # Base case (cycle detection)
            if current_node in visited:
                return False

            # Choose (Mark the current node as visited)
            visited.add(current_node)

            # Explore
            for neighbor in adj[current_node]:
                if neighbor == parent_node:
                    continue
                if not dfs(neighbor, current_node):
                    return False
            
            return True

        return dfs(0, -1) and len(visited) == n

