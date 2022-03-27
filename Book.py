class Book:

  def __init__(self, code, title, serial, numD, numB):
    self.code = code
    self.title = title
    self.serial = serial
    self.numD = numD
    self.numB = numB



  def show_book(self):

      print(f'''
    Cota: {self.code}
    Título: {self.title}
    Serial: {self.serial}
    Disponibilidad: {self.numD}
    Prestado: {self.numB}
    ''')
