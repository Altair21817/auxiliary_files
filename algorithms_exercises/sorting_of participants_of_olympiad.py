"""
Было проведено соревнование по спортивному программированию.

Каждый участник имеет уникальный логин. Когда соревнование закончится, к нему
будут привязаны два показателя: количество решённых задач P и размер штрафа F.

При сравнении двух участников выше будет тот, у которого решено больше задач.
При равенстве числа решённых задач первым идёт участник с меньшим штрафом.
Если же и штрафы совпадают, то первым будет тот, у которого логин идёт раньше
в алфавитном (лексикографическом) порядке.

В задаче запрещены сортировки, требующие O(n) и более памяти.

В первой строке задано число участников n, 1 ≤ n ≤ 100 000.
В каждой из следующих n строк задана информация про одного из участников:
- уникальным логином (строкой из маленьких латинских букв длиной не более 20)
- числом решённых задач P
- штрафом Fi

Выведите по порядку логины отсортированных участников по одному в строке.
"""

"""Примеры с ответами для тестов со всеми условиями."""
INPUT_1: list[int, str] = [
    5,
    'alla 4 100',    # gena
    'gena 6 1000',   # timofey
    'gosha 2 90',    # alla
    'rita 2 90',     # gosha
    'timofey 4 80']  # rita

INPUT_2: list[int, str] = [
    5,
    'alla 0 0',     # alla
    'allab 0 0',    # allab
    'allac 0 0',    # allac
    'allad 0 0',    # allad
    'allae 0 0']    # allae

INPUT_3: list[int, str] = [
    5,
    'alla 0 10',    # timofey
    'gena 0 9',     # rita
    'gosha 0 8',    # gosha
    'rita 0 7',     # gena
    'timofey 0 0']  # alla

INPUT: list[int, str] = INPUT_1


class Participant:

    def __init__(self, username, exercises, penalty):
        self.username = username
        self.exercises = exercises
        self.penalty = penalty

    def __gt__(self, other):
        return self.__compare_tuple() < other.__compare_tuple()

    def __lt__(self, other):
        return self.__compare_tuple() > other.__compare_tuple()

    def __repr__(self):
        return (
            f'Participant(\'{self.username}\', {self.exercises}, '
            f'{self.penalty})')

    def __str__(self):
        return (
            f'Participant @{self.username} solved {self.exercises} tasks '
            f'with a penalty of {self.penalty}')

    def __compare_tuple(self) -> tuple:
        return (-self.exercises, self.penalty, self.username)


def in_place_quick_sort(arr: list[Participant], left: int, right: int) -> None:
    if left >= right:
        return
    pivot: Participant = arr[(left + right) // 2]
    left_index: int = left - 1
    right_index: int = right + 1
    while 1:
        left_index += 1
        while pivot < arr[left_index]:
            left_index += 1
        right_index -= 1
        while pivot > arr[right_index]:
            right_index -= 1
        if left_index >= right_index:
            break
        arr[left_index], arr[right_index] = arr[right_index], arr[left_index]
    in_place_quick_sort(arr, right_index + 1, right)
    in_place_quick_sort(arr, left, right_index)
    return


def main() -> None:
    users_count: int = INPUT[0]
    users: list = [None] * users_count
    for i in range(users_count):
        user: list[str] = INPUT[i+1].split()
        users[i] = Participant(
            username=user[0], exercises=int(user[1]), penalty=int(user[2]))
    in_place_quick_sort(arr=users, left=0, right=users_count-1)
    for user in users:
        print(user.username)


if __name__ == '__main__':
    main()