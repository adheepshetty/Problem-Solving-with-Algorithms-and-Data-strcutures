def binary_search(arr ,low, high, x):
    if high >= low:
        mid = low + high//2
        if arr[mid] == x:
            return mid
        elif arr[mid]>x:
            return binary_search(arr,low,mid-1,x)
        elif arr[mid]<x:
            return binary_search(arr,mid+1,high,x)
    else:
        return -1

def exponential_search(arr, x):
    if arr[0] == x:
        return 0
    i = 1
    while i<len(arr) and arr[i]<x:
        i = i*2
    
    return binary_search(arr, i/2, min(i, len(arr)), x)


arr = [1,2,5,4,11,23,43,12,45]
target = 11
print("Position of "+str(target)+" is "+str(exponential_search(arr, target)))
