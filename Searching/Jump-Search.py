import math

def jump_search(arr, x):
    step = math.sqrt(len(arr))

    prev = 0

    # finding in which block the element might be present
    while arr[int(min(step,x)-1)] < x:
        prev = step
        step += math.sqrt(len(arr))
        if prev >= len(arr):
            return -1
    
    # searching elementwise in that block
    while arr[int(prev)] < x:
        prev +=1
        
        # element isn't present if the block size is reached
        if prev == min(step, len(arr)):
            return -1
        
    if arr[int(prev)] == x:
        return int(prev)
    
    return -1

arr = [1,2,5,4,11,23,43,12,45]
target = 11
print("Position of "+str(target)+" is "+str(jump_search(arr, target)))
