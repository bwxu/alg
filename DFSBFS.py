class Node:
	def __init__(self, value):
		self.value = value
		self.children = []
		self.parent = None
		
def DFS(start):
	visitedNodes = {start: 0}
	stack = [start]
	path = []
	count = 0
	
	while len(stack) > 0:
		node = stack.pop()
		path.append(node.value)
		
		for child in node.children:
			if child not in visitedNodes:
				stack.append(child)
				count += 1
				visitedNodes[child] = count
	print visitedNodes
	return path
	
def BFS(start):
	visitedNodes = {start: 0}
	queue = [start]
	path = []
	
	while len(queue) > 0:
		node = queue.pop(0)
		path.append(node.value)
		
		for child in node.children:
			if child not in visitedNodes:
				queue.append(child)
				visitedNodes[child] = visitedNodes[node] + 1

	return path
	
def DFSRecursive(start):
	parents = {}
	finish = []
	dfsVisit(start, parents, finish)
	return finish
	
def dfsVisit(start, parents, finish):
	for child in start.children:
		if child not in parents:
			parents[child] = start
			dfsVisit(child, parents, finish)
	finish.append(start.value)
	
def topologicalOrder(start):
	dfsResult = DFSRecursive(start)
	dfsResult.reverse()
	return dfsResult
	
graph = Node(1)
graph.children += [Node(2), Node(3), Node(4)]
graph.children[0].children += [Node(5), Node(6)]

print DFS(graph)

print BFS(graph)

print DFSRecursive(graph)

print topologicalOrder(graph)