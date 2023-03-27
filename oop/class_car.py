
"""
Наследование 
один класс наследует какие-то базовые параметры от другого 
Родительский класс 
Дочерний класс
"""
# родительский класс
class Car:

    def __init__(self) :
        print('Каркас машины создан ')
     

    def wheel(self):
        print("всего 4 колеса ")


# Дочерний класс
class Spotr_Car(Car):

    def __init__(self):
        super().__init__() # она вызывает init родительского класса , тем самым давая базовые параметры 
        print('спорткар создан ')

    def ram(self):
        print('усиленная рама')


# mazda_sport = Spotr_Car() 
# mazda_sport.wheel()
# mazda_sport.ram()
