 n = 1
 x = 10
 while x <= 20:
     x = x * 1.1
     n += 1
    print(f"Количество дней {n}, Кол-во км {x}")
     print(f"Больше 20 км пробежит на {n} дней")
y = x2

x = 1
while x <= 10:
    y = x ** 2
    print(f"x: {x} y: {y}\n")
    x += 1



print("k! = 1*2*3*4*5*6......*k")
k = int(input("Введите факториал: "))
p = 1
i = 1
while i <= k:
    p = p * i
    i += 1
    print(p)



print("s = 1 + 2 + 3 + 4 + 5 +.... + n")
s = 0
n = int(input("Enter n: "))
for x in range(1, n + 1):
    s += x
    print(s)
