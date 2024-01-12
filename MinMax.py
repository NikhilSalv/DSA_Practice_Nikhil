def DAC_MinMax(arr,p,q):
    if p == q:
        return arr[p], arr[p]
    
    elif p == q - 1:
        if arr[p] < arr[q]:
            return arr[p],arr[q]

        else:
            return arr[q], arr[p]

    else:
        mid = (p +q) // 2
        left_min, left_max = DAC_MinMax(arr,p,mid)
        right_min, right_max = DAC_MinMax(arr,mid+1,q)

        return min(left_min,right_min), max(left_max,right_max)


array = [50,20,40,90,88,11,13,22]
p = 0
q = len(array) - 1

result = DAC_MinMax(array,p,q)
print(result)
    




