def ternary_search(arr,low, high, x):
    mid1 = (low+high)//3
    mid2 = 2*int((low+high)/3)
    print(mid2)
    if high>=low:
        if arr[mid1] == x:
            return mid1
        elif arr[mid2] == x:
            return mid2
        elif arr[mid1]>x:
            return ternary_search(arr, low, mid1-1, x)
        elif arr[mid1]<x & arr[mid2]>x:
            return ternary_search(arr, mid1+1, mid2-1, x)
        elif arr[mid2]<x:
            return ternary_search(arr, mid2+1, high, x)
    else:
        return -1

arr = [1,2,5,4,7,9,10,3,11]
target = 5
print("Position of "+str(target)+" is "+str(ternary_search(arr, 0, len(arr)-1, target)))