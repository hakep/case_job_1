from random import randint


# Дан одномерный массив А размерности N.
# Найти сумму отрицательных элементов, расположенных между максимальным и минимальным.

print('Дан одномерный массив А размерности N.')
print('Найти сумму отрицательных элементов, расположенных между максимальным и минимальным.')
print('\n')


def getNumber():
    while True:
        len_f = input(
            "Введите размерность одномерного массива (целое положительное число): ")
        if len_f.isdigit() and int(len_f) > 0:
            return len_f


len_f = getNumber()
arr_a = []

# диапазон для создания случайных чисел, для заполнения одномерного массива
min_number = -10
max_nymber = 10

for i in range(int(len_f)):  # заполнение случайными числами массива arr_a
    arr_a.append(randint(min_number, max_nymber))

print(arr_a)

min_value = min(arr_a)
max_value = max(arr_a)

print("Минимальное значение: " + str(min_value) +
      " его индекс: " + str(arr_a.index(min_value)))

print("Максимальное значение: " + str(max_value) +
      " его индекс: " + str(arr_a.index(max_value)))

# Выявляю минимальный и максимальный индекс
if arr_a.index(min_value) < arr_a.index(max_value):
    min_index = arr_a.index(min_value)
    max_index = arr_a.index(max_value)
else:
    min_index = arr_a.index(max_value)
    max_index = arr_a.index(min_value)

print("Получаем срез массива, в котором будем суммировать отрицательные элементы")
print(arr_a[min_index:max_index])

sum_list = 0

# складываю отрицательные элементы
for item in arr_a[min_index:max_index]:
    if item < 0:
        sum_list += item
    else:
        continue

print("\nСумма отрицательных элементов равна: " + str(sum_list))
