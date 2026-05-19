def counting_sort(arr):
    if not arr:
        return arr
    
    max_val = max(arr)
    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1
    arr[:] = []

    for num, freq in enumerate(count):
        arr.extend([num] * freq)
    return arr

unsorted_arr = [4, 2, 2, 8, 3, 3, 1]
sorted_arr = counting_sort(unsorted_arr)
print("Sorted array:", sorted_arr)
print("array sorted successfully!")
print("this is the array sorted using counting sort algorithm",sorted_arr[1:5])
print(sorted_arr[-1:1:-1])
print(sorted_arr[-3])