## Find a peak in a 1D array with distinct elements
## O(logn) time
## returns a peak in the array

def peakFinding(A):
	length = len(A)
	middle = length//2
	if length == 1:
		return A[0]
	elif length == 2:
		return max(A[1], A[0])
	else:
		if length <= middle + 1 or middle - 1 < 0:
			return A[middle]
		elif A[middle + 1] > A[middle]:
			return peakFinding(A[middle+1:])
		elif A[middle - 1] > A[middle]:
			return peakFinding(A[:middle])
		else:
			return A[middle]
		
A = [1, 3, 2, 4, 5]
print "A peak is " + str(peakFinding(A))