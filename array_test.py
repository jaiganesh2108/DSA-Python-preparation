my_array = [7,12,9,4,11]
min_val = my_array[0]

for i in my_array:
    if i < min_val:
        min_val = i

print(min_val)

my_arr = [7,12,9,4,11]
target = 4
seen = set()
for i in my_arr:
    if i == target:
        print(True)
        break
    seen.add(i)
    print(seen)
else:
    print(False)