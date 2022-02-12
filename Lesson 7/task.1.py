while True:
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    message = input("Вам не надоело ?")
    if message == "out":
        break
    print(f"Привет {name} {surname}")
