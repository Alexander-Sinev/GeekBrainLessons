'''
class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width
    
    def full_mass(self):
        ma = Road()
        return self._length * self._width

ma = Road()
print(ma.full_mass(), mass = int(input('Enter 1 metr asphalt mass: ')), higth = int(input('Enter asphalt higth: ')))
'''

class Road:
    def __init__(self, _length, _width, _mass, _hight):
        self._length = _length
        self._width = _width
        self._mass = _mass
        self._hight = _hight

    def full_mass(self):
        return f'{(self._length * self._width * self._mass * self._hight) / 1000} ton'



r = Road(int(input('Enter the road length: ')),
         int(input('Enter the road width: ')),
         int(input('Enter the asphalt mass: ')),
         int(input('Enter the road hight: ')))
print(r.full_mass())
