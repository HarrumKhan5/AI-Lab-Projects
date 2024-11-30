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
#Post pre in order
class Node:
	def __init__(self, x):
		self.data = x
		self.left = None
		self.right = None
def allTraversal(root):
	pre = []
	post = []
	inn = []
	s = []
	s.append([root, 1])
	while (len(s) > 0):
		p = s[-1]
		if (p[1] == 1):
			s[-1][1] += 1
			pre.append(p[0].data)
			if (p[0].left):
				s.append([p[0].left, 1])
		elif (p[1] == 2):
			s[-1][1] += 1
			inn.append(p[0].data);
			if (p[0].right):
				s.append([p[0].right, 1])
		else:
			post.append(p[0].data);
			del s[-1]

	print("Preorder Traversal: ",end=" ")
	for i in pre:
		print(i,end=" ")
	print()

	# Printing Inorder
	print("Inorder Traversal: ",end=" ")

	for i in inn:
		print(i,end=" ")
	print()

	# Printing Postorder
	print("Postorder Traversal: ",end=" ")

	for i in post:
		print(i,end=" ")
	print()
if __name__ == '__main__':
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.right.left = Node(6)
	root.right.right = Node(7)
	allTraversal(root)
