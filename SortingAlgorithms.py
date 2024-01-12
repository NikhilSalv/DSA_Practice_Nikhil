# Selection sort algorithm


def SelectionSort(arr):
    n = len(arr)
    i = 0
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] =  arr[min_idx], arr[i]
    return arr
        

array = [50,25,38,44,99,16,11,22]

# results = SelectionSort(array)
# print(results)

# Time complexity of this algorithm is O(n2)

# Bubble sort algorithm >>> 


def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

results = BubbleSort(array)
print(results)