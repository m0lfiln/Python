#Task 1

total_minutes = int(input("Введите количество минут: "))

hours = total_minutes // 60
minutes = total_minutes % 60

print(hours)
print(minutes)


#Task 2

recommended_hours = int(input())
max_hours = int(input())
actual_hours = int(input())

if actual_hours<recommended_hours:
    print("Недосып")
elif actual_hours<max_hours:
    print("Пересып")
else:
    print("Нормально")


#Task 3

import math

a = float(input())
b = float(input())
c = float(input())

p = (a + b + c) / 2

area = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(area)


#Task 4

figure_type = input()

if figure_type == "треугольник":
    a = float(input())
    b = float(input())
    c = float(input())
    p = (a + b + c) / 2
    area = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(area)
elif figure_type == "прямоугольник":
    width = float(input())
    height = float(input())
    area = width * height
    print(area)
elif figure_type == "круг":
    radius = float(input())
    pi = 3.14
    area = pi * radius ** 2
    print(area)
else:
    print("Неизвестный тип фигуры")


#Task 5

def get_programmer_word(n):
    last_two_digits = n % 100
    last_digit = n % 10

    if last_two_digits in [11, 12, 13, 14]:
        return "программистов"
    elif last_digit == 1:
        return "программист"
    elif last_digit in [2, 3, 4]:
        return "программиста"
    else:
        return "программистов"

for number in [1, 2, 5, 11, 21, 23, 104, 111]:
    print(f"{number} {get_programmer_word(number)}")


#Task 6

ticket_number = input()

if len(ticket_number) != 6:
    print("Некорректный номер билета")
else:
    sum_first_three = sum(int(digit) for digit in ticket_number[:3])
    sum_last_three = sum(int(digit) for digit in ticket_number[3:])
    
    if sum_first_three == sum_last_three:
        print("Счастливый")
    else:
        print("Обычный")