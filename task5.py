# Задайте число. Составьте список чисел Фибоначчи, в том числе для 
# отрицательных индексов.(Доп)

# Пример:

# - для k = 8 список будет выглядеть 
# так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

k=int(input())

f1=1
f2=1
i=0
fib=[]
fib.insert(1,1)
fib.append(1)
while i<k-2:

    sum=f1+f2
    fib.append(sum)
    f1=f2
    f2=sum
    i+=1

print(fib)
