"""
Реализовать базовый класс Worker (работник).
определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии
(get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения
атрибутов, вызвать методы экземпляров.
"""


class Worker:
    def __init__(self, *args, **kwargs):
        self.name, self.surname, self.position = args
        self._income = kwargs


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'{sum([self._income["wage"], self._income["bonus"]]):0,} руб.'.replace(",", " ")

    def get_position(self):
        return self.position


info = Position(
    input('Имя: '),
    input('Фамилия: '),
    input('Должность: '),
    wage=int(input('Зарплата: ')),
    bonus=int(input('Премия: '))
)
print(info.get_position(), info.get_full_name(), info.get_total_income())
