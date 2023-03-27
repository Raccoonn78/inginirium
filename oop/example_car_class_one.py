
class Car:

    def __init__(self, style, brand ,price) :
        self.style=style
        self.brand=brand
        self.price=price
    
    def start(self):
        return f"{self.brand} {self.style}, за {self.price}$ поехала"

    def stop(self):
        return f"{self.brand} {self.style}, за {self.price}$ остановилась"
        
    def left(self):
        return f"{self.brand} {self.style}, за {self.price}$ повернула на лево"
        

    def right(self):
        return f"{self.brand} {self.style}, за {self.price}$ повернула на право"
    
    def repair_l(self):
        return f'{self.brand} за {self.price} наваливает боком по кргу'
        
    def repair_r(self):
        return f'{self.brand} за {self.price} не получилось навалить боком и влепилась в столб '
        
    

name_car= input('Введите название машины ')
price_car= input('Введиет стоимость машины')
mazda = Car('sport',name_car,price_car )


print(mazda.start()) # дальше она поворачивает на лево , потом на право и в конце останавливается 
print(mazda.left())
print(mazda.right())
print(mazda.stop())

drift = int(input('Введите чтобы машина наваливала боком  1 или 2 '))


if drift== 1:
    print(mazda.repair_l())
    
else:
    print(mazda.repair_r())
    
