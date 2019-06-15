# needs sorted array
def interpolation_search(arr, x):
    arr = sorted(arr)
    print(arr)
    low = 0
    high = len(arr)-1
    while low <=high and x >= arr[low] and x <= arr[high]:
        if low == high:
            if arr[low] ==x:
                return low
            return -1

    # finding the position 
        position = low + int(((float(high - low) / 
            ( arr[high] - arr[low])) * ( x - arr[low]))) 
        # print(position)

        if arr[position] == x:
            return position
    
        if arr[position] < x:
            low = position + 1

        else:
            high = position - 1

    return -1


arr = [1,2,5,4,11,23,43,12,45]
target = 11
print("Position of "+str(target)+" is "+str(interpolation_search(arr, target)))