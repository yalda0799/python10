#[yalda mohasseli][hw10][gp2]
a = (int)(input("Enter first number: "))
b = (int)(input("Enter second number: "))

max = a
min = b
if (a > b):
    pass
else:
    max, min = min, max

for i in range(1, (max // 2)+1):
    if (max % i == 0):
        if (min % i == 0):
            print(i)
