# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.


# Задание - 2
# Давайте усложним предыдущее задание, измените сущности, добавив новый параметр - armor = 1.2
# Теперь надо добавить функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно у вас должно быть 2 функции, одна наносит урон, вторая вычисляет урон по отношению к броне.

# Сохраните эти сущности, полностью, каждую в свой файл,
# в качестве названия для файла использовать name, расширение .txt
# Напишите функцию, которая будет считывать файл игрока и его врага, получать оттуда данные, и записывать их в словари,
# после чего происходит запуск игровой сессии, где сущностям поочередно наносится урон,
# пока у одного из них health не станет меньше или равен 0.
# После чего на экран должно быть выведено имя победителя, и количество оставшихся единиц здоровья.


from random import randint, choice

NAMES = ['Змей Горыныч', 'Соловей разбойник', 'Кощей Бессмертный']

def save_instance(instance):
    """
    Сохранение сущности в файл
    """
    name = instance.get('name')
    
    with open(f'{name}.txt', 'w') as profile:
        for prop in instance:
            profile.write(f'{prop}={instance.get(prop)}\n')
            
def load_instance(instance_name):
    """
    Загрузка сущности из файла
    """
    instance_property = ''
    instance_value = ''
    instance = {}
    
    with open(f'{instance_name}.txt','r') as profile:
        for prop in profile:
            instance_property, instance_value = prop.split('=')
            instance.update({instance_property: instance_value[:-1]})
            
    return instance

def attack(attacker, victim):
    """
    Атака атакующего (attacker) жертвы (victim)
    
    return BOOL: была ли смертельная атака (приведшей к смерти жертвы)
    """
    attacker_name = attacker.get('name')
    victim_name = victim.get('name')
    armor = int(victim.get('armor'))
    damage = int(attacker.get('damage'))*randint(0,120)/100  # Урон с элементом случайности
    damage = int(damage/armor)  # Урон с учетом брони
    health = int(victim.get('health')) - damage
    
    print(f'{attacker_name} ударил {victim_name} и нанес {damage} урона')
    
    victim.update({'health': health})
    
    if health > 0:
        print(f'У {victim_name} осталось {health} очков здоровья!')
        return False
    else:
        print(f'{victim_name} погиб от рук {attacker_name}!')
        return True
   

player_name = input("Введите имя игрока: ")
enemy_name = input("Введите имя противника: ")

player = {'name': player_name,
          'health': 1000,
          'armor': 3,
          'damage': 500} 
          
if enemy_name == '':  # Случайный выбор имени противника
    enemy_name = choice(NAMES)

enemy = {'name': enemy_name,
         'health': randint(50,2000),
         'armor': randint(0,10),
         'damage': randint(1,2000)}


save_instance(player)
save_instance(enemy)

player = load_instance(player_name)
enemy = load_instance(enemy_name)

attacker = player  # первым атакует всегда игрок
victim = enemy

death = False

# Вывод информации о сражающихся
# ~ print(f'{attacker.get("name").ljust(30)} vs. {victim.get("name").ljust(30)}')
# ~ print(f'Здоровье: {str(attacker.get("health")).ljust(30)} Здоровье: {str(victim.get("health")).ljust(20)}')
# ~ print(f'Броня: {str(attacker.get("armor")).ljust(30)} Броня: {str(victim.get("armor")).ljust(30)}')
# ~ print(f'Урон: {str(attacker.get("damage")).ljust(30)} Урон: {str(victim.get("damage")).ljust(30)}')

while True:  # Игровая сессия
    
    death = attack(attacker, victim) 
    if death: # битва на смерть
        break
        
    attacker = choice([player,enemy])  # случайный выбор атакующего
    
    if attacker == player:
        victim = enemy
    else: 
        victim = player

print(f'{attacker.get("name")} победил в этой битве. Осталось зоровья \
{attacker.get("health")}')

    
    
    
    

