def array_reverse(arr):
    n = len(arr)
    arr.sort()
    temp = [0] * n
    for i in range(n):
        temp[i] = arr[n-i-1]

    for i in range(n):
        arr[i] = temp[i]

def array_reverse_two(arr1):
    n = len(arr1)
    temp = [0] * n
    for i in range(n):
        temp[i] = arr1[n-i-1]

    for i in range(n):
        arr1[i] = temp[i]

if __name__ == "__main__":
    arr = [1,2,1,4,5]
    arr1 = [11,2,13,4,15]

    array_reverse(arr)
    n = len(arr)
    for i in range(n):
        print(arr[i], end =" ")
    print("\n")
    array_reverse_two(arr1)
    n = len(arr1)
    for i in range(n):
        print(arr1[i], end =" ")






