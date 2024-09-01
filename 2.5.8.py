class Square:
   _a = None

   def __init__(self, a):
    if a > 0:
       self._a = a
    
    @property
    def a(self):
      return self._a
    
    @a.setter
    def a(self, value):
      if value > 0:
        self._a = value

square_1 = Square(5)

print(f'{square_1.a}')