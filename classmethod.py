class Service:
    name='class name'
    def __init__(self):
        self.name='object name'
    @staticmethod
    #Декоратор стаикметод нужен для того чтобы из метода обьекта сделать обычную функцию(отменяя передачу и привязку к параметру self)
    def printed():
        print('static method')
    @classmethod
    #Декоратор класс метод нужен для того чтобы из метода обьекта сделать метод привязанный к кдассу(аервый параметр такого метода -сам класс
    def sep(cls,self):
        print(cls.name)
        print(self.name)
s1=Service()
Service.sep(s1)