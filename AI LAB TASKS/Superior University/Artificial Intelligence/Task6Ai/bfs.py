#bfs without queue and node
def bfs(graph, root):
    visited = set()
    def traverse(node):
        if node not in visited:
            visited.add(node)
            print(node, end=" ")        
            for neighbor in graph.get(node, []):
                traverse(neighbor)    
    traverse(root)
if __name__ == "__main__":
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    print("Breadth First Traversal without queue and node: ")
    bfs(graph, 0)
#bfs with queue and node
from collections import deque
def bfs(graph, root):
    visited = set()  
    queue = deque([root])  
    visited.add(root)  
    while queue:        
        node = queue.popleft()
        print(node, end=" ")  
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
if __name__ == "__main__":
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    print("Breadth First Traversal with queue and node: ")
    bfs(graph, 0)
