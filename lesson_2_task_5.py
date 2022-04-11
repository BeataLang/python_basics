import math

# Задаем список цен, проверяем его id
prices = [17, 26.5, 24.99, 2, 18, 0.7, 36, 124, 23, 3.55]
print(', '.join(map(str, prices)), id(prices))

# Сортируем список в порядке возрастания и проверяем id - совпадает
prices.sort()
print(prices, id(prices))

# Сортируем список в обратную сторону и проверяем id - совпадает
prices.sort(reverse = True)
print(prices, id(prices))

# Создаем список из пяти самых высоких цен и сортируем его в порядке возрастания
highest_prices = prices[0:5]
highest_prices.sort(reverse = False)
print(highest_prices)

# Оформляем список в заданном формате, добавляем разбивку на нули и копейки
for element in prices:
    total_price = element * 100
    rouble = math.floor(total_price // 100)
    kopeyka = math.floor(total_price % 100)
    element = (f'{rouble} руб {kopeyka:02} кк')
    print(element)
    # Получается все красиво, с нулями, но не в строку через запятую!

