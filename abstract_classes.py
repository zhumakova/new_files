import abc
"""Создать абстрактный класс Мебель с обязательными метода для дочерних классов: комфорт стройка"""
class Furniture(abc.ABC):

    @abc.abstractmethod
    def comfort(self):
        pass
    @abc.abstractmethod
    def building(self):
        pass
class Chair(Furniture):
    def comfort(self):
        print('chair comfort')

    def building(self):
        print('chair building')


class Table(Furniture):
    def comfort(self):
        print('table comfort')

    def building(self):
        print('table building')