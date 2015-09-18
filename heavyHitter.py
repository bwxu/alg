## Find an value, if it exists, in array A such that more than half of A's elements are that value
## F(n) = 2F(n/2) + n -> O(nlogn) time
## either returns heavy hitter or returns None if no heavy hitter

def heavyHitter(A):
	length = len(A)
	if length == 1:
		return A[0]
	else:
		value1 = heavyHitter(A[:length//2])
		value2 = heavyHitter(A[length//2:])
		occur1 = 0;
		occur2 = 0;
		for element in A:
			if element == value1:
				occur1 += 1
			if element == value2:
				occur2 += 1
		if occur1 > length//2:
			return value1
		elif occur2 > length//2:
			return value2
		else:
			return None