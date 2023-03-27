
# родительский класс
class Bird:
    
    def __init__(self):
        print("Птица готова")
        self.qwe=0

    def whoisThis(self):
        print("Птица")

    def swim(self):
        print("Плывет быстрее")

# дочерний класс
class Penguin(Bird): # внутри скобок нужно указать сам ролительский класс 
# если при вызове метода в дочернем классе такого нет , то этот меотд будет  искаться в родительском методе и сработает там 
    def __init__(self):
        # вызов функции super() 
        super().__init__() # вызывает init из ролительского класса 
        print("Пингвин готов")

    def whoisThis(self):
        print("Пингвин")

    def run(self):
        print("Бежит быстрее")

class Ostrich(Bird): # страус 
    def __init__(self):  
        super().__init__() 
        print("Страус готов")

    def whoisThis(self):
        print("Счастливчик страус")

    def run(self):
        print("Бегает быстрее всех")

    def notfly(self):
        print("Счастливчик страус не летает")
        print('====================================',self.qwe)

    pass

ostri = Ostrich() 
# ostri.whoisThis() 
# ostri.run() 
ostri.notfly() 



class Sparrow(Bird):

    def __init__(self): # вызывается автоматически при создании экзмепляра класса 
        # вызов функции super() 
        super().__init__() # вызывается так же автоматически как обычный __init__ только в родительском класса 
        print("Воробей готов")

    def whoisThis(self):# какой-то метод 
        print("Воробей")
    
    def whoisThis_real(self):# какой-то метод 
        print("Капитан Воробей")


    def run(self):# какой-то метод 
        print("Летит быстрее")
    
peggy = Penguin() #1 > init класса Penguin
peggy.whoisThis() # 2 
peggy.swim() # 
peggy.run()




sparr=Sparrow()
sparr.whoisThis()
sparr.whoisThis_real()
sparr.run()

