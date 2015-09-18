## merge sort for an array
## O(nlogn) time

def merge(left, right):
	totalLength = len(left) + len(right)
	result = []
	left.append(float("inf"))
	right.append(float("inf"))
	l = 0
	r = 0
	while len(result) < totalLength:
		if left[l] <= right[r]:
			result.append(left[l])
			l += 1
		else:
			result.append(right[r])
			r += 1
	return result
	
def mergeSort(A):
	length = len(A)
	if length <= 1:
		return A
	else:
		return merge(mergeSort(A[:length//2]), mergeSort(A[length//2:]))
			
A = [2, 4, 5, 6, 1, 4, 2, 7]
print mergeSort(A)