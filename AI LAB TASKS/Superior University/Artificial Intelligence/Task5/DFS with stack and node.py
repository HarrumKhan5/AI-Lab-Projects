def dfs_with_stack(graph, start):
    visited = set()
    stack = [start]      
    while stack:
        node = stack.pop()  
        if node not in visited:
            print(node)  
            visited.add(node)                  
            for neighbor in sorted(graph[node] - visited, reverse=True):
                stack.append(neighbor)    
    return visited
graph = {
    '0': set(['1', '2']),
    '1': set(['0', '3', '4']),
    '2': set(['0']),
    '3': set(['1']),
    '4': set(['2', '3'])
}
dfs_with_stack(graph, '0')
