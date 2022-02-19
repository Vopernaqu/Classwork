#def number(t, r):
#    print(t * r)
#
#item = input("Введите символ или слово: ")
#n = int(input("введите кол-во символов"))
#number(int(input("введите кол-во символов"))) #вызов функции
#number(item, n)
#
#
#def describe_pet(animal_type, pet_name):
#    # Выводит информацию о животном.
#    print(f"\nУ меня есть {animal_type}.")
#    print(f"Мой {animal_type} и его зовут {pet_name.title()}.")
#
#describe_pet("хомяк", "гарри")
#describe_pet("собака", "вилли")



#def user(name, surname, age) :
#    r = f"\tЕго зовут {name}, \n\tЕго фамилия {surname},\n\tЕму {age}"
#    return r
#user_name = input()
#user_surname = input()
#user_age = input()
#
#result = user(user_name, user_surname, user_age)
#print(result)

def user_info(name, surname, age) :
    r = f"\tЕго зовут {name}, \n\tЕго фамилия {surname},\n\tЕму {age}"
    return r
while True :
    user_name = input()
    user_surname = input()
    user_age = input()
    result = user_info(user_name, user_surname, user_age)
    if user_name == "out" or user_surname == "out" or user_age == "out" :
        break
    print(result)
    
