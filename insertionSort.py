## insertion sort for an array

def swap(A, i, j):
	a, b = A[i], A[j]
	A[i] = b
	A[j] = a

def insertionSort(A):
	for i in range(1, len(A)):
		j = i
		while A[j] < A[j-1]:
			swap(A, j, j-1)
			j-=1
			if j == 0:
				break
	return A
	
A = [3, 6, 2, 4, 7, 8, 10]
print insertionSort(A)
