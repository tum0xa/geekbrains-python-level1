"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""

from random import randint, sample

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 24

# Card
NUM_OF_COLS = 9
NUM_OF_ROWS = 3

CHAR_EMPTY = '  '
CHAR_SEP = '|'
CHAR_CROSS = 'XX'

COL_WIDTH = 6

MAX_BARREL_NUMBER = 90


def barrels_generator(num_of_barrels):
    while num_of_barrels > 0:
        num_of_barrels -= 1
        yield randint(1, MAX_BARREL_NUMBER)


class Card:

    def __init__(self, num_of_cols=NUM_OF_COLS, num_of_rows=NUM_OF_ROWS):
        self._num_of_cols = num_of_cols
        self._num_of_rows = num_of_rows
        self.content = self._get_content()

    def _get_content(self):
        content = {}

        # генерируем содержимое карточки до тех пор, пока
        # карточка не пройдет проверку на корректность
        while True:
            for col in range(1, self._num_of_rows + 1):
                row = {}
                tmp_list = []
                for i in range(1, self._num_of_cols + 1):
                    number = randint(10 * (i - 1) + 1, 10 * i - 1)
                    tmp_list.append(number)
                    row.update({i: f'{number}'.rjust(2)})
                # В строке не более 5 чисел
                tmp_list = sorted(sample(tmp_list, 5))

                for number in row.values():
                    if int(number) not in tmp_list:
                        row.update({int(number) // 10 + 1: CHAR_EMPTY})

                content[col] = row

            if self._check_card(content):
                break

        return content

    # проверка карточки на возможность существования
    def _check_card(self, content):
        cols = [[] for _ in range(9)]

        for col, row in content.items():
            for pos, number in row.items():
                cols[pos - 1].append(number)

        for col in cols:
            # в карточке не может быть пустого столбца и повторяющихся чисел
            if col.count(CHAR_EMPTY) == self._num_of_rows:
                return False
            elif col[0] != CHAR_EMPTY and col.count(col[0]) > 1:
                return False
            elif col[1] != CHAR_EMPTY and col.count(col[1]) > 1:
                return False
            else:
                continue
        return True

    # отрисовка карточки
    def draw(self, title):
        print(title.center(self._num_of_cols * (COL_WIDTH + 1), '-'))
        for row in self.content.values():
            print('|', end='')
            for col in row.values():
                print(col.center(COL_WIDTH), end=CHAR_SEP)
            print('-'.center(SCREEN_WIDTH, '-'))

    # зачеркивание номера в карточке
    def cross_out_number(self, number):
        for row in self.content.values():
            row_numbers = []
            for value in row.values():
                try:
                    value = int(value)
                except ValueError:
                    value = 0
                finally:
                    row_numbers.append(value)
            if number in row_numbers:
                row.update({number // 10 + 1: CHAR_CROSS})
                return True
            else:
                continue
        return False


class Player:

    def __init__(self, name, card=None, is_pc=False):
        self.name = name
        self._card = card
        self.is_pc = is_pc
        print(f'{self.name}', '(Компьютер)' if self.is_pc else '(Человек)', 'сел за стол.')

    def get_card(self, card):
        self._card = card

    def show_card(self):
        self._card.draw(self.name)

    def check_card(self, barrel):
        x = self._card.cross_out_number(barrel)
        if x:
            return True
        else:
            return False


class Game:
    def __init__(self, players):
        self._players = players
        self._bag_of_barrels = barrels_generator(MAX_BARREL_NUMBER)
        self._cards = cards_generator(100)

    def get_barrel(self):
        return next(self._bag_of_barrels)

    def _give_cards_to_players(self):
        for player in self._players:
            player.get_card(next(self._cards))

    def start(self):
        input('Чтобы раздать карточки игрокам нажмите "Enter".')
        self._give_cards_to_players()
        stop = False
        while not stop:
            for player in self._players:
                player.show_card()
            barrel = self.get_barrel()
            print(f'Выпал бочонок с номером {barrel}!')
            for player in self._players:
                if not player.is_pc:
                    choice = input(f'{player.name} - Зачеркнуть номер на карточке? y/n ')
                    check = player.check_card(barrel)
                    if choice == 'y' and check or choice == 'n' and not check:
                        print('Игра продолжается!')
                    else:
                        print(f'Стоп игра! Игрок {player.name} проиграл')
                        stop = True
                        break
                else:
                    player.check_card(barrel)


def cards_generator(num_of_cards):
    while num_of_cards > 0:
        num_of_cards -= 1
        yield Card()


player = Player("Tima")
pc = Player("PC", is_pc=True)

players = [player, pc]

game = Game(players)
game.start()
