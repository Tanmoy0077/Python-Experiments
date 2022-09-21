import time
initial = time.time()
def maxwater(heights):
	maxarea = 0
	left = 0
	right = len(heights) - 1
	while right > left:
		maxarea = max(maxarea, min(heights[right],heights[left])*(right-left))
		if heights[right] < heights[left]:
			right -=1
		else:
			left += 1
	return maxarea

print(maxwater(list(range(1,5000000))))
end = time.time()
print(end-initial)