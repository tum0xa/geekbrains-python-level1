# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

DEFAULT_COLOR = 'white'
DEFAULT_SPEED = 60

class TownCar:
    """
    Класс описывающий городскую машину
    """
    def __init__(self, name, speed=0, color=DEFAULT_COLOR, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
        print(f'{self.name} появилась в городе!')

    def go(self):
        self.speed = 60
        print(f'{self.name} поехала и набрала скорость {self.speed}!')
        return True

    def stop(self):
        self.speed = 0
        print(f'{self.name} остановилась!')
        return True

    def turn(self, direction):
        print(f'{self.name} повернула {direction}.')

    def park:
        print(f'{self.name} припарковалась!')
class SportCar:
    """
    Класс описывающий спортивную машину
    """
    def __init__(self, name, speed=0, color=DEFAULT_COLOR, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
        print(f'{self.name} появилась на трассе!')

    def go(self):
        self.speed = 180
        print(f'{self.name} поехала и набрала скорость {self.speed}!')
        return True

    def stop(self):
        self.speed = 0
        print(f'{self.name} остановилась!')
        return True

    def turn(self, direction):
        print(f'{self.name} повернула {direction}.')

    def boost(self):
        self.speed = 320
        print(f'{self.name} разогналась до {self.speed} км/ч!')


class WorkCar:
    """
    Класс описывающий рабочую машину
    """
    def __init__(self, name, speed=0, color=DEFAULT_COLOR, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
        print(f'{self.name} появилась на стройке!')

    def go(self):
        self.speed = 40
        print(f'{self.name} поехала и набрала скорость {self.speed}!')
        return True

    def stop(self):
        self.speed = 0
        print(f'{self.name} остановилась!')
        return True

    def turn(self, direction):
        print(f'{self.name} повернула {direction}.')

    def unload(self):
        print(f'{self.name} выгрузила груз.')


class PoliceCar:
    """
    Класс описывающий полицейскую машину
    """
    def __init__(self, name, speed=0, color=DEFAULT_COLOR, is_police=True):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
        print(f'{self.name} появилась на полицейском участке!')

    def go(self):
        self.speed = 40
        print(f'{self.name} поехала и набрала скорость {self.speed}!')
        return True

    def stop(self):
        self.speed = 0
        print(f'{self.name} остановилась!')
        return True

    def turn(self, direction):
        print(f'{self.name} повернула {direction}.')

    def flasher(self):
        print(f'{self.name} включила мигалку!')

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


