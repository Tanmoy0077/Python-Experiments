def rotate(arr, n, d):
	temp = arr[d:] + arr[:d]
	for i in range(n):
		arr[i] = temp[i]
arr = [1,2,3,4,5,6,7,8]
rotate(arr,8,2)
print(arr)