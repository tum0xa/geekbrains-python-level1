# Задача - 1
# Вам необходимо создать завод по производству мягких игрушек для детей.
# Вам надо продумать структуру классов,
# чтобы у вас был класс, который создает игрушки на основании:
#  Названия, Цвета, Типа (животное, персонаж мультфильма)
# Опишите процедуры создания игрушки в трех методах:
# -- Закупка сырья, пошив, окраска
# Не усложняйте пусть методы просто выводят текст о том, что делают.
# В итоге ваш класс по производству игрушек должен вернуть объект нового класса Игрушка.


class Toy:

    def __init__(self, name='Noname', color=None, sort=None):
        self.name = name
        self.color = color
        self.sort = sort
        print(f'')


class ToyFactory:

    def __init__(self, name):
        self.name = name

    def _purchase_of_raw_materials(self, name):
        print(f'Закуплено сырье для {name}')

    def _fabrication(self, name):
        print(f'Пошив {name}')

    def _painting(self, name, color):
        print(f'Идет покраска {name} в {color} ')

    def make_toy(self, sort, name, color):
        self._purchase_of_raw_materials(name)
        self._fabrication(name)
        self._painting(name, color)

        if sort == 'Животное':
            toy = Animal(name=name, color=color)
        elif sort == 'Персонаж':
            toy = Character(name=name, color=color)
        else:
            toy = Toy(name=name, color=color, sort=sort)

        print(f'Фабрика {self.name} произвела игрушку {toy.name}\nТип: {toy.sort}\nЦвет: {toy.color}\n')
        return toy


# Задача - 2
# Доработайте нашу фабрику, создайте по одному классу на каждый тип, теперь надо в классе фабрика
# исходя из типа игрушки отдавать конкретный объект класса, который наследуется от базового - Игрушка


class Animal(Toy):
    def __init__(self, name=None, color=None):
        super().__init__(name=name, color=color, sort='Животное')


class Character(Toy):
    def __init__(self, name=None, color=None):
        super().__init__(name=name, color=color, sort='Персонаж')


if __name__ == '__main__':

    toy_factory = ToyFactory('LLC Toy Factory')
    elephant = toy_factory.make_toy('Животное', 'Слон',color='Серый')
    three_heads_fire_breathing_snake = toy_factory.make_toy('Персонаж', 'Змей Горыныч', color='Зеленый')
    tank = toy_factory.make_toy('Танк', 'Т-34', 'Темно-зеленый')
