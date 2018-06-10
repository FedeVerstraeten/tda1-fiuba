class cola:
  elems = []

  def __init__(self):
      self.elems = []

  def encola(self, x):
      self.elems.append(x)

  def desencola(self):
      if self.cantidad > 0:
          self.elems.pop(0)

  def fcantidad(self):
      return len(self.elems)

  def fprimero(self):
      if self.cantidad > 0:
          return self.elems[0]

  primero = property (fget = fprimero)
  cantidad = property (fget = fcantidad)
