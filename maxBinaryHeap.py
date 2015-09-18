class MaxBinaryHeap:
	def __init__(self):
		self.heapList = []
		self.currentSize = 0
	
	def parent(i):
		return int((i-1)/2)
		
	def left(A, i):
		return 2*(i+1) - 1

	def right(A, i):
		return 2*(i+1)
	