class Node:
	def __init__(self, value):
		self.value = value
		self.parent = None
		self.left = None
		self.right = None
		
	def findRoot(self):
		if self.parent != None:
			findRoot(self.parent)
		return self 
	
	def insert(self, value):
		if self.value == None:
			self = Node(value)
		elif value < self.value:
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
			return self.left.findMin()
		return self
		
	def findMax(self):
		if self.right != None:
			return self.right.findMax()
		return self
	
	# returns None if no larger found
	def nextLarger(self):
		if self.right != None:
			return self.right.findMin()
		else:
			current = self
			while current.parent != None and current is current.parent.right:
				current = current.parent
			return current.parent
			
	def nextSmaller(self):
		if self.left != None:
			return self.left.findMax()
		else:
			current = self
			while current.parent != None and current is current.parent.left:
				current = current.parent
			return current.parent
	
	def inOrderTraversal(self):
		if self.left != None:
			self.left.inOrderTraversal()
		print self.value
		if self.right != None:
			self.right.inOrderTraversal()
	
	def find(self, value):
		if self.value == None:
			return None
		elif value == self.value:
			return self
		elif value < self.value:
			if self.left == None:
				return None
			else:
				return self.left.find(value)
		elif value > self.value:
			if self.right == None:
				return None
			elif self.right.value == value:
				return self.right
			else:
				return self.right.find(value)
			
tree1 = Node(23)
tree1.insert(8)
tree1.insert(4)
tree1.insert(42)
tree1.insert(16)
tree1.insert(15)
print tree1.find(8).nextSmaller().value