a = float(input("Введите сторону треугольника: "))
b = float(input("Введите сторону треугольника: "))
c = float(input("Введите сторону треугольника: "))

if a + b > c and  b + c > a and a + c > b :
    print("Треугольник может существовать")
    
    if  (a == b or a == c or b == c) and (a != c or a != b or b != c) :
        print("Треугольник равнобедренный")

    if  a == b and a == c   :
        print("Треугольник равносторонний")

    if a != b and a != c and b != c :
        print("Треугольник разносторонний")
    
else :
    print("Треугольник не может существовать")


