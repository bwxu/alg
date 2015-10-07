class Node:
	def __init__(self, value):
		self.value = value
		self.children = []
		self.parent = None
		
def DFS(start):
	visitedNodes = set()
	stack = [start]
	path = []
	topoPath = []
	t = 0
	
	while len(stack) > 0:
		node = stack.pop()
		if node in visitedNodes:
			continue
		
		path.append(node.value)
		visitedNodes.add(node)
		
		numChildren = 0
		for child in node.children:
			if child not in visitedNodes:
				stack.append(child)
				numChildren += 1
				
		if numChildren == 0:
			topoPath.append(node.value)	
		t += 1
		
	print topoPath[::-1]
	return path, t
	
def BFS(start):
	visitedNodes = set()
	queue = [start]
	path = []
	
	while len(queue) > 0:
		node = queue.pop(0)
		if node in visitedNodes:
			continue
		
		path.append(node.value)
		visitedNodes.add(node)
		
		for child in node.children:
			if child not in visitedNodes:
				queue.append(child)
	return path
	
graph = Node(1)
graph.children += [Node(2), Node(3), Node(4)]
graph.children[0].children += [Node(5), Node(6)]

print DFS(graph)

print BFS(graph)