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
    def __init__(self, hid = False, size = 6):
        self.hid = hid
        self.size = size

        self.count = 0 #колличество поражённых кораблей

        self.field = [ ["O"]*size for _ in range(size) ]

        self.busy = [] #занятые клетки - кораблями или же те, по уоторым уже стреляли
        self.ships = [] #занятые клетки только кораблями

    def __str__(self):
        res = "" #здесь будет храниться вся доска
        res += "  | 1 | 2 | 3 | 4 | 5 | 6 |"
        for i, row in enumerate(self.field):
            res += f"\n{i+1} | " + " | ".join(row) + " |"
        
        if self.hid:
            res = res.replace("■", "O")
        return res
    
    def out(self, d): # проверяет, за пределами ли точка, d - это точка, которую проверяем
        return not((0<= d.x < self.size) and (0<= d.y < self.size))
    
    def contour(self, ship, verb = False): #verb - нужно ли ставить точки вокруг кораблей (появятся после уничтожения корабля)
        near = [
            (-1, -1), (-1, 0) , (-1, 1),
            (0, -1), (0, 0) , (0 , 1),
            (1, -1), (1, 0) , (1, 1)
        ]
        for d in ship.dots:
            for dx, dy in near:
                cur = Dot(d.x + dx, d.y + dy)
                if not(self.out(cur)) and cur not in self.busy:
                    if verb:
                        self.field[cur.x][cur.y] = "."
                    self.busy.append(cur)
    
    def add_ship(self, ship):
        for d in ship.dots:
            if self.out(d) or d in self.busy:
                raise FieldWrongShipExc()
        for d in ship.dots:
            self.field[d.x][d.y] = "■"
            self.busy.append(d)
        
        self.ships.append(ship)
        self.contour(ship)

    def shot(self, d):
        if self.out(d):
            raise FieldWrongShipExc()
        
        if d in self.busy:
            raise FieldWrongShipExc()
        
        self.busy.append(d)
        
        for ship in self.ships:
            if d in ship.dots:
                ship.lives -= 1
                self.field[d.x][d.y] = "X"
                if ship.lives == 0:
                    self.count += 1
                    self.contour(ship, verb = True)
                    print("Корабль уничтожен!")
                    return False
                else:
                    print("Корабль ранен!")
                    return True
        
        self.field[d.x][d.y] = "."
        print("Мимо!")
        return False
    def begin(self):
        self.busy = []