# 2.	Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
a_x = float(input('Enter the 1st number: '))
a_y = float(input('Enter the 2nd number: '))
b_x = float(input('Enter the 3rd number: '))
b_y = float(input('Enter the 4th number: '))

distance = ((b_x-a_x)**2 + (b_y-a_y)**2) **0.5
print(f'Distance between point a and point b = {round(distance, 2)}')