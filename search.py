def bsearch(n, arr):
	if len(arr) == 1:
		return n == arr[0]
	if not arr:
		return None
	index = len(arr)/2
	if n == arr[index]:
		return True
	elif n > index:
		return bsearch(n, arr[index:])
	else:
		return bsearch(n, arr[:index])

arr = [1,2,3,5,7,8,22,44,66]
print bsearch(44, arr)

