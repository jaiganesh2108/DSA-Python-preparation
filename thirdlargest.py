def thirdlargest(arr):
    n = len(arr)
    arr.sort()
    print(arr)
    for i in range(n-3,-1,-1):
        if arr[i] != arr[n-1]:
            return arr[i]

if __name__ == "__main__":
    arr = [12, 35, 1, 10, 34, 1]
    print(thirdlargest(arr))
    