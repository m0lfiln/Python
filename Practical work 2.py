#Task 1

x = int(input("Число: "))
print(x * 8)


#Task 2 

print("Расчет объема данных")
a = int(input("Введите первый параметр: "))
b = int(input("Введите второй параметр: "))
c = int(input("Введите третий параметр: "))
x = a * b * c
y = x / 1024
print(f"{a} * {b} * {c} = {x}")
print(f"{x} / 1024 = {y}")
print("Итог:", y)