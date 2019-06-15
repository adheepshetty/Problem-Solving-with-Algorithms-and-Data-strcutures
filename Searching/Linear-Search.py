def linear_search(arr , x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


arr = []

while True:
    num = raw_input('Enter a digit: ')
    if not num.isdigit():
        break
    arr.append(int(num))

target = input('Enter number you want to find: ')
print("Position of number "+ str(target) +" is "+str(linear_search(arr, target)))