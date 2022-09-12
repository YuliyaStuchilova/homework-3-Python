# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

print(arr)

mult = 0
i = 0
if len(arr) % 2 == 1:
    while i <= len(arr)//2:
        mult = arr[i]*arr[len(arr)-1-i]
        i += 1
        print(mult, end=' ')
else:
    while i < len(arr)//2:
        mult = arr[i]*arr[len(arr)-1-i]
        i += 1
        print(mult, end=' ')
