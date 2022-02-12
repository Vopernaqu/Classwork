x = float(input())
y = float(input())

if x > 0 and y > 0 :
    print("Первая четверть")

if x < 0 and y > 0 :
    print("Вторая четверть")

if x < 0 and y < 0 :
    print("Третья четверть")

if x > 0 and y < 0 :
    print("Четвёртая четверть")

if x == 0 or y == 0 :
    print("Никакая четверть")
