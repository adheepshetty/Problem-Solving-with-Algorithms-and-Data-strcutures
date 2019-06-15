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

arr = [1,2,5,4]
target = 2
print("Position of "+str(target)+" is "+str(binary_search(arr, 0, len(arr)-1, target)))
