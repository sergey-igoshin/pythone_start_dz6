"""
Реализовать класс Stationery (канцелярская принадлежность).
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return self.title


class Pen(Stationery):
    def draw(self):
        return self.title


class Pencil(Stationery):
    def draw(self):
        return self.title


class Handle(Stationery):
    def draw(self):
        return self.title


stat = Stationery('Запуск отрисовки')
pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')
print(stat.draw())
print(pen.draw())
print(pencil.draw())
print(handle.draw())
