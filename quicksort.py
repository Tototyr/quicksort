def quicksort(arr):
    if not arr:
        return []
    else:
        return quicksort([x for x in arr if x < arr[0]]) \
        + [x for x in arr if x == arr[0]] \
        + quicksort([x for x in arr if x > arr[0]])

print(quicksort([10,123,512,552,66]))