class MaxBinaryHeap:
	def __init__(self):
		self.heapList = []
		self.currentSize = 0
	
	def parent(i):
		return int((i-1)/2)
		
	## corrects error assuming children trees of i are heaps
	def max_heapify(self, i):
		left = 2*i + 1
		right = 2*i + 2
		numElements = len(self.heapList)
		
		if (left < numElements and right < numElements):
			largerIndex = -1
			if (self.heapList[left] < self.heapList[right]):
				largerIndex = right
			else:
				largerIndex = left
			if (self.heapList[i] < self.heapList[largerIndex]):
				## swap values
				temp = self.heapList[i]
				self.heapList[i] = self.heapList[largerIndex]
				self.heapList[largerIndex] = temp
				self.max_heapify(largerIndex)
				
		elif (left >= numElements and right < numElements):
			if (self.heapList[i] < self.heapList[right]):
				## swap values
				temp = self.heapList[i]
				self.heapList[i] = self.heapList[right]
				self.heapList[right] = temp
				self.max_heapify(right)
				
		elif (left < numElements and right >= numElements):
			if (self.heapList[i] < self.heapList[left]):
				## swap values
				temp = self.heapList[i]
				self.heapList[i] = self.heapList[left]
				self.heapList[left] = temp
				self.max_heapify(left)
		
	def build_max_heap(self):
		for i in range(0, len(self.heapList)/2 + 2, -1):
			self.max_heapify(i)
	
	def extract_max(self):
		if (len(self.heapList) == 1):
			self.heapList = []
			return self.heapList[0]
			
		## swap top element with last leaf
		largest = self.heapList[0]
		self.heapList[0] = self.heapList[len(self.heapList)-1]
		self.heapList[len(self.heapList)-1] = largest
		self.heapList.pop()
		self.max_heapify(0)
		return largest
		
	def trickle_up(self, i):
		parent = int((i-1)/2)
		if (i > 0):		
			if (self.heapList[parent] < self.heapList[i]):
				temp = self.heapList[parent]
				self.heapList[parent] = self.heapList[i]
				self.heapList[i] = temp
				self.trickle_up(parent)
		
	def insert(self, value):
		self.heapList.append(value)
		self.trickle_up(len(self.heapList)-1)