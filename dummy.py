print("2+3",end="=")
print(2+3)
print("laptop", "desktop", "tablet", "smartphone", sep=".")
print("jai", "ganesh", end=" ")
print(73*39+47%3)

print("Hi", "Hi", sep="...", end="...")
print("Hi")

sum = 0
for i in range(0, 11):
    sum += i
    print(sum)

def main(a,b):
    for i in range(1,11,1):
        print(i,a,b)

main(10,20)