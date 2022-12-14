# 1.	Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

day_num = int(input('Enter any number: '))
if day_num < 0 or day_num > 7:
    print('Error')
elif day_num == 1:
    print('Today is Monday')
elif day_num == 2:
    print('Today is Tuesday')
elif day_num == 3:
    print('Today is Wednesday')
elif day_num == 4:
    print('Today is Thursday')
elif day_num == 5:
    print('Today is Friday')
elif day_num == 6:
    print('Today is Saturday')
elif day_num == 7:
    print('Today is Sunday')
