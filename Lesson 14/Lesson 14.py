# def message(name, age):
#     print(f"Hello, {name}, age: {age}")
#message()

#y = f(x)

#def summ(c, b):
#    a = c + b #7
#    return a #7
#c = int(input("c ="))
#b = int(input("b ="))
#y = summ(c, b)
#print(y)

#Основной код программы
#n = input('Введите свое имя--')
#i = input('Введите свой возраст--')
#message(n, i)




def pet(animal_type, name_pet) :
#    print(f"У меня есть {animal_type}")
#    print(f"Его зовут {name_pet}")
    mess = f"У меня есть {animal_type}. Его зовут {name_pet}."
    return mess.upper()
y = pet("Dog", "Lalli")
print(y)
