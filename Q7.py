from color import ColorPoint

class AdvancePoint(ColorPoint): #we are inheriting from ColorPoint
  def __init__(self, x, y, color):
    #super().__init__(x,y, color) #would all the parent

    self._x = x
    self._y = y
    self._color = color