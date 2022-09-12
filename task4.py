# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

n = int(input())
finish = []
while n > 0:
    finish.append(n % 2)
    n = n//2
    
finish.reverse()
print(*finish)
