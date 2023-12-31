# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

            # Решение1

n = int(input('Введите трехзначное число: '))
с = n % 10
n = n //10
b = n % 10
a = n // 10
print(a + b + с)

            # Решение2

n = input('Введите трехзначное число: ')
if len(n) == 3:
    print(int(n[0])+int(n[1]) + int(n[2]))
else:
    print('Введено неверное число')

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

s = int(input('Введите общую сумму журавликов: '))
kate = 2/3*s
petr = 1/4*kate
serg = petr
print(f'Петя = {petr}, Катя = {kate},  Сережа = {serg}')


# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

n = input('Введите номер билета: ')
first_half = int(n[0]) + int(n[1]) + int(n[2])
second_half = int(n[3]) + int(n[4]) + int(n[5])
if first_half==second_half:
    print ('Билет - счастливый')
else:
    print ('Билет - несчастливый')

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один 
# разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

n=int(input('Введите длину шоколадки: '))
m=int(input('Введите ширину шоколадки: '))
k=int(input('Введите кол-во долек для отлома:'))

if k % n == 0 or k % m ==0:
     print('Yes')
else:
     print('No')