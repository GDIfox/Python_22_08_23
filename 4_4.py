# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12


setA = set(input('Введите числа: '))
# setA = {2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2}
setB = set(input('Введите числа: '))
# setB = {3, 6, 9, 12, 15, 18}
res = setA & setB
print(*sorted(res))