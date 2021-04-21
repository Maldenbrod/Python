x = 0
m = float(input("Введите 3 числа. Первое число m:\n "))
if m < 0:
    x = 1
else:
    x = 0
n = float(input("Введите следующее число.Число n:\n "))
if n < 0:
    x = x+1
else:
    x = x
p = float(input("Введите следующее число.Число p:\n "))
if p < 0:
    x = x+1
else:
    x = x
print("Количество отрицательных чисел:", x)
