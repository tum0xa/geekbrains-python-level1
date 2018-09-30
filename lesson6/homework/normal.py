# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

from random import choice


def set_random_name():
    name = ''
    for _ in range(10):
        name += str(chr(randint(65, 90)))
    return name


class Person:

    def __init__(self, name, health=100, damage=2, armor=1):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor
        print(f'{self.name}:\nhp:{self.health}\ndmg:{self.damage}\narm:{self.armor}\n')

    def attack(self, victim=None):

        # Если забыл указать Person кого бить, то будем считать что Person занялся самоистязанием.
        if victim == None:
            victim = self

        damage = self._calc_damage(victim.armor)
        victim.health -= damage
        print(f'{self.name} ударил {victim.name} и причинил {damage} очков урона!')
        print(f' У {victim.name} осталось {victim.health} очков здоровья.')

    def _calc_damage(self, armor):
        damage = self.damage / armor
        if damage <= 1:
            damage = 1
        return int(damage)


class Player(Person):
    pass


class Enemy(Person):
    pass


class Battle:

    def __init__(self, participants):
        self.participants = participants

    def battle(self):
        while len(self.participants) > 1:
            attacker = choice(self.participants)
            victim = choice(self.participants)

            attacker.attack(victim)

            if victim.health <= 0:
                print(f'{victim.name} пал в этой эпичной битве!')
                self.participants.pop(self.participants.index(victim))
        else:
            print('Битва завершилась!')
            return participants[0]


if __name__ == '__main__':

    from random import randint
    participants = []
    for _ in range(randint(2, 100)):
        person = Person(set_random_name(), health=randint(100, 500), damage=randint(20, 100), armor=randint(1, 100))
        participants.append(person)
    # print(participants)
    my_epic_battle = Battle(participants)

    winner = my_epic_battle.battle()

    # player = Player('Lolo', health=randint(100, 500), damage=randint(20, 100), armor=randint(1, 100))
    # enemy = Enemy('Spider', health=randint(50, 1000), damage=randint(20, 200), armor=randint(1, 100))

    # attacker = None
    # victim = None
    #
    # while True:
    #
    #     if attacker == player:
    #         attacker = enemy
    #         victim = player
    #     else:
    #         attacker = player
    #         victim = enemy
    #
    #     attacker.attack(victim)
    #
    #     if victim.health <= 0:
    #         print(f'{victim.name} погиб с честью.')
    #         break


    print(f'Победил {winner.name}! Осталось {winner.health} очков здоровья.')
    input()
