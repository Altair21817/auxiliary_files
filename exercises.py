from decorators import time_measure_decorator

# Может быть оставлять комментарии, почему где-то так, а не иначе?
# Mock тесты?

"""Задача.
Для заданных коэффициентов уравнения вида ax^2 + bx + c = 0 найти его корни.
Гарантируется, что входными данными будут три целочисленных числа, указанные
через пробел. Ответ необходимо вывести строкой, указав числа через пробел
в порядке их возрастания.
"""

# """Примеры с ответами для тестов со всеми условиями."""
# INPUT_1: str = '0 0 0' # Бесконечное множество решений
# INPUT_2: str = '0 0 5' # Нет решений
# INPUT_3: str = '0 5 5' # Один корень: -1.0
# INPUT_4: str = '2 1 4' # Нет решений
# INPUT_5: str = '2 4 2' # Один корень: -1.0
# INPUT_6: str = '2 5 2' # Два корня: -0.5 и -2.0

# INPUT: str = INPUT_1


# def read_input() -> tuple:
#     """Read input data."""
#     nums: list = INPUT.split()
#     a: int = int(nums[0])
#     b: int = int(nums[1])
#     c: int = int(nums[2])
#     return a, b, c


# def solve_square(a: int, b: int, c: int) -> tuple or int or None:
#     """Solve square equation."""
#     disc: int = b * b - 4 * a * c
#     if disc < 0:
#         return None
#     # Optimize formula: (-b + disc ** 0.5) / (2 * a)
#     disc_sqrt = disc ** 0.5
#     disc_const = -b / (2 * a)
#     x1 = disc_const + disc_sqrt / (2 * a)
#     if disc == 0:
#         return x1
#     x2 = disc_const - disc_sqrt / (2 * a)
#     return x1, x2


# def solve_equation(a, b, c) -> str or int or tuple:
#     """Solve given equation."""
#     if a == 0:
#         if c == 0:
#             return '∞'
#         elif b == 0:
#             return f'Error! Given equation is: {c} = 0'
#         return - b / c
#     return solve_square(a, b, c)


# def reformat_answer(answer: any) -> str or None:
#     """Reformat answer to desire string."""
#     if answer is None or isinstance(answer, str):
#         return answer
#     elif isinstance(answer, tuple):
#         return ' '.join(map(str, sorted(answer)))
#     elif isinstance(answer, float):
#         return str(answer)


# def main():
#     a, b, c = read_input()
#     answer: any = solve_equation(a=a, b=b, c=c)
#     print(reformat_answer(answer=answer))


# if __name__ == '__main__':
#     main()

"""Задача.
Двухмерный остров состоит из столбцов различной высоты. Над островом прошел
дождь и заполнил водой все низины, а не поместившаяся вода утекла в море, не
увеличив его уровень. По ландшафту острова определите, сколько блоков воды
суммарно осталось в низинах. Ответ выведите одним числом.
"""

# """Примеры с ответами для тестов:
# Для острова '3 1 4 3 5 1 1 3 1' ответ будет 7.
#     #
#   #/#
# #/###//#
# #/###//#
# #########

# Для острова '3 1 4 3 5 1 1 2 5 1 1 4 3 2 1' ответ будет 20.
#     #///#
#   #/#///#//#
# #/###///#//##
# #/###//##//###
# ###############
# """

# INPUT_1 = '3 1 4 3 5 1 1 3 1'              # 7
# INPUT_2 = '3 1 4 3 5 1 1 2 5 1 1 4 3 2 1'  # 20
# INPUT_3 = '5 1 5'                          # 4
# INPUT_4 = '1 2 1'                          # 0
# INPUT_5 = '1 1 1'                          # 0
# INPUT_6 = '3 2 1'                          # 0
# INPUT_7 = '1 2 3'                          # 0

# INPUT: str = INPUT_1


# def read_input() -> list:
#     """Read input data."""
#     alts: list = list(map(int, INPUT.split()))
#     return alts


# def get_max_alt_indexes(alts: list) -> tuple:
#     """Get indexes for max values in island altitudes."""
#     max_alt: int = 0
#     max_alt_index: list = []
#     for i in range(len(alts)):
#         if alts[i] > max_alt:
#             max_alt = alts[i]
#             max_alt_index = [i]
#         elif alts[i] == max_alt:
#             max_alt_index.append(i)
#     return max_alt_index


# def count_vol_edge(alts: list, max_alt: int, range: range) -> int:
#     """Count water volume on islands edge (before first maximum altitude)."""
#     volume: int = 0
#     for i in range:
#         alt: int = alts[i]
#         if alt < max_alt:
#             volume += max_alt - alt
#         elif alt > max_alt:
#             max_alt = alt
#     return volume


# def count_vol_mid(alts: list, left_max: int, right_max: int) -> int:
#     """Count water volume between maximum altitudes."""
#     # It's a bit faster than: volume = 0 -> volume += max_alt - alts[i]
#     volume = alts[left_max] * (right_max - left_max - 1)
#     for alt in range(left_max + 1, right_max):
#         volume -= alts[alt]
#     return volume


# def main():
#     alts: list = read_input()
#     max_alt_index: list = get_max_alt_indexes(alts=alts)
#     vol_left: int = 0
#     vol_mid: int = 0
#     vol_right: int = 0
#     if len(max_alt_index) != 1:
#         for i in range(len(max_alt_index) - 1):
#             vol_mid += count_vol_mid(
#                 alts=alts,
#                 left_max=max_alt_index[i],
#                 right_max=max_alt_index[i+1])
#     if max_alt_index[0] != 0:
#         vol_left = count_vol_edge(
#             alts=alts, max_alt=alts[0], range=range(max_alt_index[0] + 1))
#     if max_alt_index[-1] != len(alts):
#         vol_right = count_vol_edge(
#             alts=alts,
#             max_alt=alts[len(alts)-1],
#             range=range(len(alts)-1, max_alt_index[-1], -1))
#     print(vol_left + vol_mid + vol_right)


# if __name__ == '__main__':
#     main()

"""Задача.
Для заданной последовательности буквенных символов без пробелов вывести строку
к виду: символ-количество-символ-количество-сим...
"""

# """Примеры с ответами для тестов со всеми условиями."""
# INPUT_1: str = 'AAABCDD'  # A3BCD2
# INPUT_2: str = 'Z'        # Z
# INPUT_3: str = 'XX'       # X2

# INPUT: str = INPUT_1


# def main():
#     result = []
#     char_fixed = INPUT[0]
#     char_count = 0
#     for char_current in INPUT:
#         if char_current == char_fixed:
#             char_count += 1
#         else:
#             if char_count == 1:
#                 result.append(char_fixed)
#             else:
#                 result.append(f'{char_fixed}{char_count}')
#             char_count = 1
#             char_fixed = char_current
#     if char_count == 1:
#         result.append(char_fixed)
#     else:
#         result.append(f'{char_fixed}{char_count}')
#     print(''.join(result))


# if __name__ == '__main__':
#     main()

"""Задача.
Для каждой из строки (имя пользователя) в массиве вывести список символов,
которые не попадают под паттерн r'[\w.@+-]+', в единственном экземпляре.
"""

# """Примеры с ответами для тестов со всеми условиями."""
# # Username '{, ,}' contains forbidden symbols: {' ', '{', ',', '}'}
# INPUT_1: str = '{, ,}'
# # Username must have one character at least!
# INPUT_2: str = ''

# INPUT = INPUT_1

# from re import sub

# PATTERN = r'[\w.@+-]+'


# def username_check(username: str, pattern: str) -> str:
#     """Печатает список символов, не попадающих под regexp выражение."""
#     forbidden_symbols = set(sub(pattern, '', username))
#     if forbidden_symbols:
#         print(
#             f"Username '{username}' contains forbidden symbols: "
#             f"{forbidden_symbols}")
#     elif username == '':
#         print(f'Username must have one character at least!')
#     else:
#         print(f'Username "{username}" is OK!')


# def main():
#     username_check(username=INPUT, pattern=PATTERN)


# if __name__ == '__main__':
#     main()

"""Задача.
Дано два числа без ведущих нулей, разделенные пробельным символом. Необходимо
проверить, можно ли получить второе число (в т.ч. с ведущим нулем) из первого
перестановкой цифр.
"""

# """Примеры с ответами для тестов со всеми условиями."""
# INPUT_1: str = '134 341'  # True
# INPUT_2: str = '112 111'  # False
# INPUT_3: str = '3 33'     # False

# INPUT = INPUT_3

# DIGITS: int = 10


# def read_input() -> list:
#     """Read input data and return 2 numbers"""
#     return list(map(int, INPUT.split()))


# def create_sorted_nums(num: int) -> list:
#     """Упорядочивает подсчетом цифры в num."""
#     num_digits = [0] * DIGITS
#     while num != 0:
#         num_digits[num % 10] += 1
#         num = num // 10
#     return num_digits


# def main():
#     x, y = read_input()
#     x_digits = create_sorted_nums(x)
#     y_digits = create_sorted_nums(y)

#     print(all(x_digits[i] == y_digits[i] for i in range(DIGITS)))


# if __name__ == '__main__':
#     main()

"""Задача.
На шахматной доске N на N находятся M ладей (ладья бьет клетки на той же
горизонтали или вертикали до ближайшей занятой). Определите, сколько пар ладей
бьют друг друга. Ладьи задаются парами числе I и J, обозначающих координаты.
"""

# chess_rocks = [(2,8), (4,3), (7,5), (7,7), (7,8)]

# def clash_counter(chess_rocks: list[int, int]) -> int:
#     """Принимает на вход список ладей на шахматном поле, в котором для каждой
#     указаны координаты нахождения на шахматной доске, и возвращает количество
#     пар ладей, которые бьют друг друга. Размер поля n на n."""

#     def __axis_check(axis: dict, coordinate_num: int):
#         coordinate = rock[coordinate_num]
#         if coordinate not in axis:
#             axis[coordinate] = 0
#         axis[coordinate] += 1
#         return axis

#     axisx = {}
#     axisy = {}

#     for rock in chess_rocks:
#         axis_x = __axis_check(axis=axisx, coordinate_num=0)
#         axis_y = __axis_check(axis=axisy, coordinate_num=1)

#     # Для малого количества фигур допускается использовать генератор
#     clashes = sum(
#         (axis[key] - 1)
#         for axis in (axis_x, axis_y)
#         for key in axis if axis[key] > 1)

#     # Для большого количества объектов циклы выгоднее генераторов
#     # clashes = 0
#     # for axis in (axis_x, axis_y):
#     #     for key in axis:
#     #         if axis[key] > 1:
#     #             clashes += axis[key] - 1

#     return clashes

# print(clash_counter(chess_rocks))

"""Задача.
Дана строка S. Выведите гистограмму как в примере (для "Hello world!"):

     #
     ##
#########
!,Hdelorw

Пробелы не учитываются, символы отсортированы в порядке увеличения кодов.
"""

# def char_gist(s: str) -> str:
#     """Принимает текст и возвращает гистограмму использования символов."""

#     char_freq = {}

#     for char in s:
#         if char not in FORBIDDEN_CHARS:
#             if char not in char_freq:
#                 char_freq[char] = 0
#             char_freq[char] += 1

#     lines_count = max(char_freq.values())
#     text_lines = [''] * (lines_count + 1)
#     for key in sorted(char_freq):
#         for i in range(1, lines_count + 1):
#             if char_freq[key] >= i:
#                 text_lines[i] += '#'
#             else:
#                 text_lines[i] += ' '
#     for char in sorted(char_freq):
#         text_lines[0] += char
#     text = ''
#     for i in reversed(range(lines_count+1)):
#         text += text_lines[i] + '\n'
#     return text

# S = "Lil' Princess the Best!"

# FORBIDDEN_CHARS = (' ',)

# print(char_gist(S))

# inp = 333826595

# @time_measure_decorator
# def get_factory_1(num):
#      a = 1
#      num_original = num
#      while a < 100:
#           num = num_original
#           answer = []
#           i = 2
#           maximum = num ** (0.5)
#           while i <= maximum:
#                result = divmod(num, i)
#                if result[1] == 0:
#                     answer.append(i)
#                     num //= i
#                else:
#                     i += 1
#           if num > 1:
#                answer.append(num)
#           a += 1
#      return ' '.join(map(str, answer))

# print(get_factory_1(int(inp)))

# @time_measure_decorator
# def get_factory_2(num):
#      a = 1
#      num_original = num
#      while a < 100:
#           num = num_original
#           answer = []
#           i = 2
#           while i * i <= num:
#                result = divmod(num, i)
#                if result[1] == 0:
#                     answer.append(i)
#                     num //= i
#                else:
#                     i += 1
#           if num > 1:
#                answer.append(num)
#           a += 1
#      return ' '.join(map(str, answer))

# print(get_factory_2(int(inp)))


""""Дана матрица. Для заданного элемента нужно вернуть список всех его
соседей в возрастающем порядке через пробел. Соседним считается элемент,
находящийся от текущего на одну ячейку влево, вправо, вверх или вниз.
Диагональные элементы соседними не считаются.

Например, для ячейки {0,0} соседями будут '0 2', для {2,1} - '1, 2, 7, 7'.
1 2 3
0 2 6
7 4 1
2 7 0

- В первой строке задано n — количество строк матрицы.
- Во второй — количество столбцов m. Числа m и n не превосходят 1000.
- В следующих n строках задана матрица. Элементы матрицы — целые числа, по
модулю не превосходящие 1000.
- В последних двух строках записаны координаты элемента,
соседей которого нужно найти. Индексация начинается с нуля.
"""

# INPUT1 = '4'
# INPUT2 = '3'
# INPUT3 = '1 2 3'
# INPUT4 = '0 2 6'
# INPUT5 = '7 4 1'
# INPUT6 = '2 7 0'
# # Правильный ответ для точки {0,0}: '0 2'
# INPUT7 = '0'
# INPUT8 = '0'


# def read_input() -> tuple:
#     """Read input data."""
#     rows = int(input())
#     cols = int(input())
#     matr = []
#     for row in range(rows):
#     	matr.append(list(map(int, input().split())))
#     i = int(input())
#     j = int(input())
#     return rows, cols, matr, i, j


# def find_result(rows, cols, matr, i, j):
#     result = []
#     if rows == 1:
#         pass
#     elif i == 0:
#         result.append(matr[i+1][j])
#     elif i == rows - 1:
#         result.append(matr[i-1][j])
#     else:
#         result.append(matr[i+1][j])
#         result.append(matr[i-1][j])
#     if cols == 1:
#         pass
#     elif j == 0:
#         result.append(matr[i][j + 1])
#     elif j == cols - 1:
#         result.append(matr[i][j - 1])
#     else:
#         result.append(matr[i][j + 1])
#         result.append(matr[i][j - 1])
#     result.sort()
#     return result


# rows, cols, matr, i, j = read_input()
# print(' '.join(map(str, find_result(rows, cols, matr, i, j))))

# def get_input():
# 	return input(), input()


# def find_letter(text_1, text_2):
#     chars_1 = count_chars(text_1)
#     chars_2 = count_chars(text_2)
#     for char in chars_2:
#         if char not in chars_1 or chars_2[char] != chars_1[char]:
#             return char


# def count_chars(text):
#     char_dict = {}
#     for char in text:
#         if char not in char_dict:
#              char_dict[char] = 0
#         char_dict[char] += 1
#     return char_dict


# text_1, text_2 = get_input()
# print(find_letter(text_1, text_2))

"""Улица имеет длину n. Все участки на улице стоят в один ряд. Каждый участок
или пустой, или имеет построенный обитаемый дом.

Необходимо для каждого из участков указать расстояние до ближайшего пустого.
Если участок пустой, эта величина будет равна 0 - расстояние до самого себя.
Числа необходимо вывести в одну строку, разделяя пробелом.

Участки пронумерованы вразнобой с 1. Каждый пустой участок обозначается 0.
В первой строке дана длина улицы n (1 ≤ n ≤ 10^6). В следующей записаны n целых
неотрицательных чисел - номера домов и обозначение пустых участков.
Гарантируется, что в последовательности будет хотя бы один 0, а номера домов
являются целыми числами.

Например, для длины улицы 7 (0 1 5 4 9 0 2) ответ будет: 0 1 2 2 0 1
"""

# Яндекс.Практикум, Python-разработчик: введение в алгоритмы. Финальные задачи.
# A. Ближайший ноль
# Время посылки: 19 мар 2023, 13:45:10
# ID: 84235511
# Выполнил: Свидунович Кирилл, когорта 52

# С исправлениями для первого ревью

# from typing import Tuple


# def get_input() -> Tuple:
#     """Получает значение длины улицы и расположение домов в ряд на ней."""
#     street_len: int = int(input())
#     street: list = [int(_) for _ in input().split()]
#     return street_len, street


# def count_distance(street_len: int, street: list):
#     """Выводит список расстояний до ближайшего 0 для каждого из участков."""
#     result: list = [None] * street_len
#     max_index: int = street_len - 1
#     for plot_before_zero in range(street_len):
#         if street[plot_before_zero] != 0:
#             result[plot_before_zero] = max_index - plot_before_zero
#         else:
#             result[plot_before_zero] = 0
#             last_zero: int = plot_before_zero
#             break
#     if plot_before_zero == max_index:
#         return result
#     if plot_before_zero != 0:
#         dif: int = max_index - plot_before_zero
#         for plot_renew in range(plot_before_zero):
#             result[plot_renew] -= dif
#     i: int = 0
#     for plot in range(plot_before_zero + 1, street_len):
#         if street[plot] != 0:
#             i += 1
#             result[plot] = i
#         else:
#             result[plot] = 0
#             renew_value: int = 0
#             for plot_renew in range(plot - 1, (plot + last_zero) // 2, -1):
#                 renew_value += 1
#                 result[plot_renew] = renew_value
#             last_zero = plot
#             i = 0
#     return result


# def main():
#     street_len, street = get_input()
#     result: list = count_distance(street_len=street_len, street=street)
#     print(' '.join(map(str, result)))


# if __name__ == '__main__':
#     main()

"""Предоставлено поле (кнопки) 4x4. В каждой ячейке указана либо точка, либо
цифра от 1 до 9. В каждый момент времени t (от 1 до 9) игрок должен
одновременно нажать на все кнопки, на которых указана цифра t. Если игрок
сумел нажать все необходимые кнопки - он получает 1 балл. Игрок может
одновременно нажать не более чем на k кнопок за раз.

Необходимо найти максимальное количество баллов, которое может может получить
игрок за игру для заданной конфигурации поля.

В первой строке дано целое число k (1 ≤ k ≤ 5).
В четырёх следующих строках заданы кнопки строки - по 4 символа в каждой без
пробелов. Каждый символ – либо точка, либо цифра от 1 до 9. Символы одной
строки идут подряд и не разделены пробелами.

Например, для k = 3 и матрицы ниже ответ: 2
1 2 3 1
2 . . 2
2 . . 2
2 . . 2
"""

# Яндекс.Практикум, Python-разработчик: введение в алгоритмы. Финальные задачи
# B. Ловкость рук
# Время посылки: 19 мар 2023, 12:47:44
# ID: 84231810
# Выполнил: Свидунович Кирилл, когорта 52

# С исправлениями для первого ревью

# from typing import Dict, Tuple

# GAMERS: int = 2
# FIELD_ROWS: int = 4
# ZERO_CHAR: str = '.'
# T = range(1, 9 + 1)


# def init_input() -> Tuple:
#     """Получает значение k и количество символов на поле."""
#     max_nums_at_time: int = int(input()) * GAMERS
#     chars_count = {str(num): 0 for num in range(1, 10)}
#     chars_count['ZERO_CHAR'] = 0
#     for _ in range(FIELD_ROWS):
#         row: str = input()
#         for char in row:
#             if char != ZERO_CHAR:
#                 chars_count[char] += 1
#     return max_nums_at_time, chars_count


# def count_points(max_nums_at_time: int, chars_count: Dict[str, int]) -> str:
#     """Вычисляет максимальное количество баллов."""
#     result: int = 0
#     for second in T:
#         if 0 < chars_count[str(second)] <= max_nums_at_time:
#             result += 1
#     return result


# def main():
#     max_nums_at_time, chars_count = init_input()
#     print(count_points(
#         max_nums_at_time=max_nums_at_time, chars_count=chars_count))


# if __name__ == '__main__':
#     main()
