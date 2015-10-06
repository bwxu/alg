class Node:
	def __init__(self, value):
		self.value = value
		self.next = None
		
	def printList(self):
		print self.value
		if self.next != None:
			self.next.printList()
		
	def insert(self, value):
		if self.value == None:
			self.value = value
		elif self.next != None:
			self.next.insert(value)
		else:
			self.next = Node(value)
			
	def delete(self, value):
		previous = None	
		current = self
		next = self.next
		while current != None:
			if current.value == value:
				if previous == None:
					if next != None:
						current.value = next.value
						current.next = next.next
						break
					else:
						current.value = None
						break
				else:
					previous.next = next
					break
			else:
				previous = current
				current = next
				next = current.next
				continue
				
	def size(self):
		current = self
		size = 0
		while (current != None):
			size += 1
			current = current.next
		return size	
		
	def search(self, value):
		current = self
		while (current != None):
			if (current.value == value):
				return current
			else:
				current = current.next
				
	def index(self, value):
		current = self
		index = 0
		while (current != None):
			if (current.value == value):
				return index
			else:
				current = current.next
				index += 1
				
	def reverse(self):
		previous = None
		current = self
		while (current != None):
			next = current.next
			current.next = previous
			previous = current
			current = next
		return previous
		
		
linkedList = Node(1)
linkedList.insert(2)
linkedList.printList()
print "-------"
linkedList.insert(0)	
linkedList.printList()
print "-------"
linkedList.delete(0)
linkedList.delete(1)
linkedList.delete(2)
linkedList.printList()
print "-------"
linkedList.insert(4)
linkedList.printList()
print "-------"
print linkedList.size()
print "-------"
print linkedList.search(4).value
print "-------"
print linkedList.index(4)
print "-------"
linkedList.insert(6)
linkedList.insert(8)
linkedList.printList()
print "-------"
reverse = linkedList.reverse()
reverse.printList()