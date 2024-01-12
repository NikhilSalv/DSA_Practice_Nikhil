# Merge sort algorithm

def MergeSort(arr):

    if len(arr) > 1:

        mid = len(arr) // 2

        L = arr[:mid]

        R = arr[mid:]

        MergeSort(L)

        MergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def printarray(arr):
    for i in range(len(arr)):
        print(arr[i], end="\n")
    print()

# Driver code 
if __name__ == '__main__':
    arr = [50,20,40,90,88,11,13]
    print("Given array is :", end="\n")
    printarray(arr)
    MergeSort(arr)
    print("Sorted array is :", end = "\n")
    printarray(arr)