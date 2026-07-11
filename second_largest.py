def getsecondlargest(my_arr):
    n = len(my_arr)
    my_arr.sort()
    print(my_arr)
    for i in range(n -2, -1, -1):
        if my_arr[i] != my_arr[n-1]:
            return my_arr[i]
    return -1

if __name__ == "__main__":
    my_arr=[12, 35, 1, 10, 34, 1]
    print(getsecondlargest(my_arr))