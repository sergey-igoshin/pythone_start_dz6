"""
Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop,
turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите
методы и покажите результат.
"""
import random

class Car:

    def __init__(self, *args):
        self.speed, self.color, self.name, self.is_police = args

    def go(self):
        return 'начала движение,'

    def stop(self):
        return 'остановилась,'

    def turn(self, direction):
        return f'повернула на {direction},'

    def show_speed(self):
        return f'текущая скорость {self.speed} км/ч,'

    def car_color(self):
        return f'цвет {self.color},'

    def car_name(self):
        return f'{self.name},'

    def car_is_police(self):
        if self.is_police:
            return 'нет нарушений ПДД'
        else:
            return 'есть нарушения ПДД'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'текущая скорость {self.speed} км/ч, превышение скорости на {self.speed - 60} км/ч,'
        else:
            return f'текущая скорость {self.speed} км/ч,'


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'текущая скорость {self.speed} км/ч, превышение скорости на {self.speed - 40} км/ч,'
        else:
            return f'текущая скорость {self.speed} км/ч,'


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


town = TownCar(60, 'красный', 'Toyota', False)
sport = SportCar(150, 'черный', 'BMW', False)
work = WorkCar(80, 'белый', 'VW', True)
police = PoliceCar(120, 'белый', 'Mercedes', True)
car_turn = ['лево', 'право']
print(town.car_name(), town.car_color(), town.go(), town.show_speed(), town.turn(random.choice(car_turn)),
      town.stop(), town.car_is_police())
print(sport.car_name(), sport.car_color(), sport.go(), sport.show_speed(), sport.turn(random.choice(car_turn)),
      sport.stop(), sport.car_is_police())
print(work.car_name(), work.car_color(), work.go(), work.show_speed(), work.turn(random.choice(car_turn)),
      work.stop(), work.car_is_police())
print(police.car_name(), police.car_color(), police.go(), police.show_speed(), police.turn(random.choice(car_turn)),
      police.stop(), police.car_is_police())
