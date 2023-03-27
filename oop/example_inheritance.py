class G: # класс отвечающий за создания каких-либо рисунков (родительский класс)
    name='G'

    def set_coords(self, x1,y1,x2,y2):
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2

class L(G): # класс для создания линий (дочерний класс )
    name ='L'
    def draw(self):
        print('Рисует линии')

class R(G): # класс для создания линий  (дочерний класс )

    def draw(self):
        print('Рисует квадраты')

   
l =L()
r=R()
g=G()

l.set_coords(1,2,3,4)
r.set_coords(5,6,7,8)
print(l.name)
print(r.name)
l.draw()
r.draw()
print(l.__dict__)
print(r.__dict__)

