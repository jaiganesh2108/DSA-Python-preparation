my_str = input("Enter a string: ")

vowels = "aeiou"

count = 0

for i in my_str:
    if i in vowels:
        count += 1
print(count)
