import math
x = float(input())

if x > 0 :
    y = 2*x - 10

if x == 0 :
    y=0

if x < 0 :
    y = 2 * math.fabs(x)

print(y)
