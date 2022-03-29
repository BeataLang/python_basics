day_seconds = 86400
hour_seconds = 3600
minute_seconds = 60

duration = int(input("Введите время в секундах: "))

days = duration // 86400
seconds = duration - (days * day_seconds)
hours = seconds // 3600
seconds = seconds - (hours * hour_seconds)
minutes = seconds // 60
seconds = seconds % 60

if days > 0:
    print(f'{days} дн {hours} час {minutes} мин {seconds} сек')
elif hours > 0:
    print(f'{hours} час {minutes} мин {seconds} сек')
elif minutes > 0:
    print(f'{minutes} мин {seconds} сек')
else:
    print(f'{seconds} сек')