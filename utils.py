def findMax(arr):
    max = arr[0]
    for num in arr:
        if num > max:
            max = num
    return max