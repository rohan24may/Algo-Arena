#Largest Rectangle in Histogram 👉 Max area from bars

def largest_rect(arr):
    stack = []
    max_area = 0

    for i in range(len(arr)+1):
        while stack and (i == len(arr) or arr[stack[-1]] > arr[i]):
            h = arr[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h*w)
        stack.append(i)

    return max_area