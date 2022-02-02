import math

x = float(input())
p = math.pi
if x > p and x < p/4 :
    y = -(math.cos(x - p))**2
    print(y)

elif x >= p/4 and x <= 1 :
    y = math.sqrt(abs(x + 1))
    print(y)
elif x > 1 :
    y = 1/(x-1)
    print(y)
else :
    print("error")
    
