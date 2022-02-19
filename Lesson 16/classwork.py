import math
#1
#def hello_name(name) :
#    print(f"Привет {name}")
#name = str(input("Введите имя: "))
#hello_name(name)
#2
#def string(msg, n) :
#    print(msg*n)
#msg = (input("строку пожалуйста"))
#n = int(input("число"))
#string(msg, n)
#3
#def max_number(number_1, number_2) :
#    if number_1 > number_2 :
#        print(f"{number_1} > {number_2}")
#    elif number_2 > number_1 :
#        print(f"{number_2} > {number_1}")
#    elif number_1 == number_2 :
#        print(f"{number_1} = {number_2}")
#number_1 = float(input("Число 1:"))
#number_2 = float(input("Число 2:"))
#max_number(number_1, number_2)
#4
#a = float(input("Number 1: "))
#b = float(input("Number 2: "))
#c = float(input("Number 3: "))
#print(max(a, b, c))
#5
#def triangle(x, y, z):
#    if x + y > z and x + z > y and y + z > x:
#        print("Треугольник существует")
#    else:
#        print("Треугольник не существует")
#x = float(input("x = "))
#y = float(input("y = "))
#z = float(input("z = "))
#triangle(x, y, z)
#6
#def words(a, b) :
#    print(f"{a} {b}")
#a = str(input("1 срока"))
#b = str(input("2 срока"))
#words(a, b)
#7
#def operations(a, b, c) :
#    if c == "+" :
#        rint(round(a+b), 2)
#    elif c == "-" :
#        rint(round(a-b), 2)
#    elif c == "*" :
#        rint(round(a*b), 2)
#    elif c == "/" :
#        rint(round(a/b), 2)
#    else :
#        print("Unknown operation")
#a = float(input("Number 1: "))
#b = float(input("Number 2: "))
#c = input("Operation: ")
#operations(a, b, c)
#8
#def html(tag, info):
#    print(f"{tag}:{info.title()}\n <{tag}>{info}<{tag}>")
#tag = input("Tag:")
#info = input("Info:")
#html(tag, info)
#9
#def season(month_number):
#    if month_number == 1 or month_number == 2 or month_number == 12 :
#        print("Это зима")
#    elif month_number == 3 or month_number == 4 or month_number == 5 :
#        print("Это весна")
#    elif month_number == 6 or month_number == 7 or month_number == 8 :
#        print("Это лето")
#    elif month_number == 9 or month_number == 10 or month_number == 11 :
#        print("Это осень")
#month_number = int(input("Номер месяца:"))
#season(month_number)
#10
#def pictures(a):
#    for i in a:
#        print("*" * i)
#pictures([2,7,1,4,2,3,9,3] )
#11
#def ones(a):
#    if a % 2 == 0 :
#        print("Число парное")
#    else :
#        print("Число непарное")
#a = int(input("Number:"))
#ones(a)
#12
#def first_last(numbers):
#    b = [numbers[0], numbers[-1]]
#    print(b)
#numbers = [5, 16, 72, 29, 11, 217, 112]
#first_last(numbers)
#13
#def fact(k, p = 1, i = 1) :
#    while i <= k :
#        p *= i
#        i += 1
#    print(p)
#k = int(input("Введите факториал"))
#fact(k)
#14

def triangle(side_1, side_2, side_3):
    p = (side_1 + side_2 + side_3)/2
    print(math.sqrt(p*(p-side_1)*(p-side_2)*(p-side_3)))
          
def check_triangle(side_1, side_2, side_3):
    if side_1 + side_2 > side_3 and side_1 + side_3 > side_2 and side_2 + side_3 > side_1:
        return True
    else:
        return False
def circle(r):
    print(math.pi * math.pow(r, 2))
def rectangle(a, b):
    print(a*b)
def checker_of_figure(name_of_figure):
    if name_of_figure == "triangle" or name_of_figure == "треугольник" :
        side_1 = int(input("1 сторона"))
        side_2 = int(input("2 сторона"))
        side_3 = int(input("1 сторона"))
        if check_triangle(side_1, side_2, side_3): 
            triangle(side_1, side_2, side_3)
        else :
            print("Треугольник не может существовать")
    elif name_of_figure == "circle" or name_of_figure == "круг" :
        r = int(input("Радиус круга"))
        circle(r)
    elif name_of_figure == "rectangle" or name_of_figure == "прямоугольник" :
        a = int(input("1 сторона прямоугольника"))
        b = int(input("2 сторона прямоугольника"))
        rectangle(a, b)
checker_of_figure(input("Введите название фигуры: "))

    
        
        
            
