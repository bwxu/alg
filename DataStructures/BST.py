class Node:
	def __init__(self, value):
		self.value = value
		self.parent = None
		self.left = None
		self.right = None
	
	def insert(self, value):
		if value < self.value:
			if self.left != None:
				self.left.insert(value)
			else:
				self.left = Node(value)
				self.left.parent = self
		else:
			if self.right != None:
				self.right.insert(value)
			else:
				self.right = Node(value)
				self.right.parent = self
	
	def findMin(self):
		if self.left != None:
			find_min(self.left)
		return self.value 
	
	def nextLarger(self):
		if self.right != None:
			return find_min(self.right)
		else:
			current = self
			while current.parent != None and current is current.parent.right:
				current = current.parent
			return current.parent
	
	def inOrderTraversal(self):
		if self.left != None:
			self.left.inOrderTraversal()
		print self.value
		if self.right != None:
			self.right.inOrderTraversal()
					
tree1 = Node(1)
tree1.insert(0)
tree1.inOrderTraversal()
