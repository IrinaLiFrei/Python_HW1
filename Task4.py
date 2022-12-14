# 1.	Напишите программу, которая по заданному номеру четверти
#  показывает диапазон возможных координат точек в этой четверти (x и y).
quadrant_number = int(input('Enter the quadrant number (from 1 to 4): '))
if quadrant_number < 1 or quadrant_number > 4:
    print('Error. Try again.')
elif quadrant_number == 1:
    print('x = from 0 to +infinity, y = from 0 to +infinity')
elif quadrant_number == 2:
    print('x = from -infinity to 0, y = from 0 to +infinity')
elif quadrant_number == 3:
    print('x = from -infinity to 0, y = from -infinity to 0')
elif quadrant_number == 4:
    print('x = from 0 to +infinity, y = from -infinity to 0')