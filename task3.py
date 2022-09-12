# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

n = int(input())
arr = []
for i in range(n):
    arr.append(float(input()))

print(arr)

part = []

for i in arr:
    j=i-int(i)
    part.append(j)
    
print(part)

print(max(part)-min(part))
