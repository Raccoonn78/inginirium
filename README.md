# inginirium

### Репозиторий для повторения материала 



#### str - string - строка 
#### int- integer - числовые 
#### bool - True False
#### float - числа с точкой 
#### list - список (массив) []
#### dict - словарь  {ключ: значение}
#### tuple - кортеж ()
#### set - множество {}  все элементы уникальны
#### NoneType - None 


### циклы 
for 
while

### условия 
if 
elif
else

### анонимные функции
lambda 

pass -пустышка 

map('функция', иттерируемый объект)  - преобразовывает 
filter('функция', иттерируемый объект) - фильтрует 
all() - возвращает True если все значения верны, False если есть хоть один False
any() - вернет True если есть хоть один верный, False если все не верны 


*args и **kwargs
*args - принимает неограниченное кол-во атрибутов и помещает их в кортеж
**kwargs - принимает неограниченное кол-во атрибутов в виде словаря ( a=10,b={1:2})

def one(*args, **kwargs):
    pass

def two(*args):
    pass
    
two(1,1,1,1,1,1,1,1,1,11,1,4)

def three(**kwargs):
    pass
    
three(a=123456,b={1:'qwert'},c=[1,1,1],d='qwerty)



class A:

    def __init__(self) -> None: # метод конструктор (магический метод )
        pass

    def get_number(self) : # метод
        pass


   # @classmethod  # работает с атрибутами класса

    #@staticmethod # работает только внутри класса 
    def __str__(self) -> str: # вывод экзмепляра
        pass
    def __add__(self): # сложение
        pass
    def __mul__(self):# умножение
        pass
    def __truediv__(self): # деление 
        pass
    def __floordiv__(self): # целочисленное деление
        pass
    def __sub__(self): # вычитание
        pass 
    def __radd__(self):# когда слагаемые поменялись местами 

        pass
    # и так же все эти магические методы имеют вторые названия с буквой r 
    # 


test=A() # экземпляр класса 
test.get_number()# вызов метода
