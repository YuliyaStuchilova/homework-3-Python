# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

print(arr)
sum = 0
i=0
while i < len(arr):
    if i % 2 == 1:
        sum = sum+arr[i]
    i += 1
print(sum)