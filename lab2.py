# TODO Найдите количество книг, которое можно разместить на дискете
import math
volume = 1.44 * (1024 ** 2)
volume_book = 100 * 50 * 25 * 4
result = math.floor(volume / volume_book)
print(f'Количество книг, помещающихся на дискету: {result}' )
