# 2.	Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Enter the first positive or negative number: '))
y = int(input ('Enter the second positive or negative number: '))
if x == 0 or y == 0:
    print('Number should not be zero')
elif x > 0 and y > 0:
    print('The point is in the 1st quadrant')
elif x < 0 and y > 0:
    print('The point is in the 2nd quadrant')
elif x < 0 and y < 0:
    print('The point is in the 3rd quadrant')
elif x > 0 and y < 0:
    print('The point is in the 4th quadrant')