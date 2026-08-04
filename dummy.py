for i in range(1,21):
    for j in range(1,21):
        if i == j:
            print(i,j)

for i in range(1,21):
    for j in range(-21,-1):
        print(i,j)

for i,j in zip(range(1,21), range(-21,-1)):
    print(i,j)

#print("this is the \n new line")
#print("this is the\ttab space")
#print("this is the backslash \\")

#a = int(23)
#b = float(74.3)
#print(a,b, sep=",")

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#print('this is shiva\'s code')
#print(" He says, \"this is my phone\"")
#print(" this is the backslash: \\")
#print("It's Hero Time! \n\t - Ben 10")

import keyword

print(keyword.kwlist)
print(type(i))
