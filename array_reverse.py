def array_reverse(arr):
    n = len(arr)
    arr.sort()
    temp = [0] * n
    for i in range(n):
        temp[i] = arr[n-i-1]

    for i in range(n):
        arr[i] = temp[i]

if __name__ == "__main__":
    arr = [11,2,13,4,15]
    array_reverse(arr)
    n = len(arr)
    for i in range(n):
        print(arr[i], end =" ")