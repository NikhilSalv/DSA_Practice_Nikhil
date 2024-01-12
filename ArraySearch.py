
# Searching an element from an Array with Linear Search

# def LinearSearch(arr,size,element):
#     for i in range(size):
#         if arr[i] == element:
#             var = i
#             return var
#     return -1


# arr = [53,39,32,17,90,12]
# search_element = 12
# n = len(arr)
# results = LinearSearch(arr,n,search_element)
# print(results)

# Time complexity is the O(n)

# Binary search algorithm :

def BinarySearch(arr, i, j, element):
    if i == j :
        if arr[i] == element:
            return i
        else:
            return -1
    else:
        mid = i + (j - i) // 2
        if arr[mid] == element:
            return mid
        elif arr[mid] < element:
            return BinarySearch(arr, mid + 1, j,element)
        else:
            return BinarySearch(arr, i, mid - 1,element)




arr = [10,23,35,67,75,82,86]
search_element = 86
i = 0
j = len(arr) - 1
results = BinarySearch(arr,i,j,search_element)
print(results)

# Time complexity is O(Log n)