# import time
# initial = time.time()
def maxArea(height):
    area, left, right = 0, 0, (len(height) - 1)
    while left < right:
        if(height[left] <= height[right]):
            h = height[left]
            hd = True
        else:
            h = height[right]
            hd = False
        area = max(area, h*(right-left))
        if (hd):
            while (h >= height[left+1]) and (left+1 < right):
                left += 1
            left += 1
        else:
            while (h >= height[right-1]) and (right-1 > left):
                right -= 1
            right -= 1
    return area

print(maxArea(list(range(1,500))))
# end = time.time()
# print(end-initial)