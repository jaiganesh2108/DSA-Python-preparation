def array_reverse(arr):
    n = len(arr)
    temp = [0] * n
    for i in range(n):
        temp[i] = arr[n-i-1]

    for i in range(n):
        arr[i] = temp[i]



if __name__ == "__main__":
    arr = [1,2,3,4,5]
    array_reverse(arr)
    
    for i in range(len(arr)):
        print(arr[i], end =" ")