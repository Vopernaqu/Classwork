import math
x = float(input())
y = float(input())


if x > y :
    z = math.sqrt(x * y)

else :
    z = math.log(x + y, math.e)

print(z)
