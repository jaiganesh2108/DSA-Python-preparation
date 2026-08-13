x = 50
print("x =", x, "\t", "type:", type(x))

x = 50.0
print("x =", x, "\t", "type:", type(x))

def add(x: int, y: int) -> float:
    return x / y

output = add(5, 10)
print("Output:", output, "\t", "type:", type(output))

name = "jaiganesh"
print(name[0], name[8])

list = ["jai", 100, "python", "programmer"]

for i in list:
    print(i)

