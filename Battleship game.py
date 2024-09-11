class FieldExceptions:
    pass

class FieldOutOfBorderExc(FieldExceptions):
    def __str__(self):
        return "Капитан, вы пытаетесь выстрелить за пределы поля боя!"

class FieldOccupiedExc(FieldExceptions):
    def __str__(self):
        return "Капитан, вы уже стреляли по этим координатам!"
    
class FieldWrongShipExc(FieldExceptions):
    pass

class Dot:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return other.x == self.x and other.y == self.y
    
    def __repr__(self):
        return f"Dot ({self.x}, {self.y})"
        
class Ship:
    def __init__(self, bow, l, o):
        self.bow = bow
        self.l = l # длина
        self.o = o # ориентация: 0 - вертикальный, 1 - горизонтальный
        self.lives = 1

    @property
    def dots(self):
        ship_dots = []
        for i in range(self.l):
            cur_x = self.bow.x
            cur_y = self.bow.y

            if self.o == 0:
                cur_x += i
            
            elif self.o == 1:
                cur_y += i
            
            ship_dots.append(Dot(cur_x, cur_y))
        
        return ship_dots
    
    def shooten(self, shot):
        return shot in self.dots
        




class Fields:
