import math
basic_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

hours = ('"' + '0' + basic_list[1] + '"')
minutes = ('"' + basic_list[3] + '"')
weather = ('"' + basic_list[8] + '"')

max_width = 3

# Не понимаю, как добавить 0 после + в "+5 градусов": вариант {weather:+0{max_width}} не работает

result = f'в {hours} часов {minutes} минут температура воздуха была {weather:{max_width}} градусов'

print(result)